import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Dropout Risk Prediction",
    page_icon="🎓",
    layout="wide"
)

MODEL_PATH = "student_dropout_brf_model.pkl"

APPLICATION_MODE_OPTIONS = [
    "1st phase - general contingent",
    "Ordinance No. 612/93",
    "1st phase - special contingent (Azores Island)",
    "Holders of other higher courses",
    "Ordinance No. 854-B/99",
    "International student (bachelor)",
    "1st phase - special contingent (Madeira Island)",
    "2nd phase - general contingent",
    "3rd phase - general contingent",
    "Ordinance No. 533-A/99, item b2) (Different Plan)",
    "Ordinance No. 533-A/99, item b3) (Other Institution)",
    "Over 23 years old",
    "Transfer",
    "Change of course",
    "Technological specialization diploma holders",
    "Change of institution/course",
    "Short cycle diploma holders",
    "Change of institution/course (International)"
]

COURSE_OPTIONS = [
    "Biofuel Production Technologies",
    "Animation and Multimedia Design",
    "Social Service (evening attendance)",
    "Agronomy",
    "Communication Design",
    "Veterinary Nursing",
    "Informatics Engineering",
    "Equinculture",
    "Management",
    "Social Service",
    "Tourism",
    "Nursing",
    "Oral Hygiene",
    "Advertising and Marketing Management",
    "Journalism and Communication",
    "Basic Education",
    "Management (evening attendance)"
]

HIGH_RISK_COURSES = [
    "Biofuel Production Technologies",
    "Equinculture",
    "Informatics Engineering",
    "Management (evening attendance)",
    "Basic Education",
    "Agronomy"
]


@st.cache_resource
def load_model_bundle(path: str):
    return joblib.load(path)


def classify_risk(score: float, medium_threshold: float, high_threshold: float) -> str:
    if score >= high_threshold:
        return "High Risk"
    elif score >= medium_threshold:
        return "Medium Risk"
    return "Low Risk"


def prepare_input(df: pd.DataFrame, selected_features: list) -> pd.DataFrame:
    df = df.copy()

    for col in [
        "Tuition_fees_up_to_date",
        "Debtor",
        "Scholarship_holder",
        "Application_mode",
        "Course"
    ]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    return df[selected_features].copy()


def recommend_intervention(row: pd.Series) -> str:
    actions = []

    # faktor finansial
    if str(row["Tuition_fees_up_to_date"]).strip().lower() == "no":
        actions.append("Intervensi finansial dan tindak lanjut administrasi")

    if str(row["Debtor"]).strip().lower() == "yes":
        actions.append("Konseling administrasi pembayaran")

    if (
        str(row["Scholarship_holder"]).strip().lower() == "no"
        and str(row["Tuition_fees_up_to_date"]).strip().lower() == "no"
    ):
        actions.append("Evaluasi bantuan biaya atau beasiswa")

    # faktor akademik semester 1
    if pd.notna(row["Curricular_units_1st_sem_approved"]) and row["Curricular_units_1st_sem_approved"] <= 3:
        actions.append("Tutoring akademik semester 1")

    if pd.notna(row["Curricular_units_1st_sem_grade"]) and row["Curricular_units_1st_sem_grade"] < 12:
        actions.append("Pendampingan belajar semester 1")

    # faktor akademik semester 2
    if pd.notna(row["Curricular_units_2nd_sem_approved"]) and row["Curricular_units_2nd_sem_approved"] <= 3:
        actions.append("Tutoring akademik semester 2")

    if pd.notna(row["Curricular_units_2nd_sem_grade"]) and row["Curricular_units_2nd_sem_grade"] < 12:
        actions.append("Pendampingan belajar semester 2")

    # faktor usia
    if pd.notna(row["Age_at_enrollment"]) and row["Age_at_enrollment"] >= 23:
        actions.append("Pendampingan individual dan fleksibilitas studi")

    # faktor jalur masuk
    risky_modes = [
        "Over 23 years old",
        "Transfer",
        "Change of course",
        "Change of institution/course",
        "Change of institution/course (International)"
    ]
    if str(row["Application_mode"]).strip() in risky_modes:
        actions.append("Monitoring akademik jalur masuk khusus")

    # faktor program studi
    if str(row["Course"]).strip() in HIGH_RISK_COURSES:
        actions.append("Koordinasi intensif dengan program studi")

    if not actions:
        return "Monitoring rutin"

    return "; ".join(list(dict.fromkeys(actions)))


def predict_dropout(
    df: pd.DataFrame,
    model,
    selected_features: list,
    medium_threshold: float,
    high_threshold: float
) -> pd.DataFrame:
    input_df = prepare_input(df, selected_features)

    probabilities = model.predict_proba(input_df)[:, 1]
    predicted_label = (probabilities >= high_threshold).astype(int)

    result = input_df.copy()
    result["DropoutRiskScore"] = probabilities
    result["PredictedDropout"] = predicted_label
    result["RiskCategory"] = result["DropoutRiskScore"].apply(
        lambda x: classify_risk(x, medium_threshold, high_threshold)
    )
    result["RecommendedIntervention"] = result.apply(recommend_intervention, axis=1)

    return result


# =========================
# MAIN APP
# =========================
st.title("🎓 Student Dropout Risk Prediction")
st.markdown(
    "Aplikasi ini digunakan untuk memprediksi risiko dropout mahasiswa "
    "berdasarkan model **Balanced Random Forest**."
)

# load model
try:
    model_bundle = load_model_bundle(MODEL_PATH)
    model = model_bundle["model"]
    selected_features = model_bundle["selected_features"]
    medium_threshold = float(model_bundle["medium_threshold"])
    high_threshold = float(model_bundle["high_threshold"])
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

with st.sidebar:
    st.header("Informasi Model")
    st.write("**Algoritma:** Balanced Random Forest (Calibrated)")
    st.write(f"**Medium threshold:** {medium_threshold:.4f}")
    st.write(f"**High threshold:** {high_threshold:.4f}")

    st.write("**Fitur yang digunakan:**")
    for f in selected_features:
        st.write(f"- {f}")

st.subheader("Input Data Mahasiswa")

with st.form("single_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        cu2_approved = st.number_input(
            "Curricular_units_2nd_sem_approved",
            min_value=0,
            max_value=30,
            value=0,
            step=1
        )

        cu2_grade = st.number_input(
            "Curricular_units_2nd_sem_grade",
            min_value=0.0,
            max_value=20.0,
            value=0.0,
            step=0.1
        )

        cu1_approved = st.number_input(
            "Curricular_units_1st_sem_approved",
            min_value=0,
            max_value=30,
            value=0,
            step=1
        )

        cu1_grade = st.number_input(
            "Curricular_units_1st_sem_grade",
            min_value=0.0,
            max_value=20.0,
            value=0.0,
            step=0.1
        )

        tuition_status = st.selectbox(
            "Tuition_fees_up_to_date",
            options=["yes", "no"],
            index=0
        )

    with col2:
        debtor_status = st.selectbox(
            "Debtor",
            options=["no", "yes"],
            index=0
        )

        scholarship_status = st.selectbox(
            "Scholarship_holder",
            options=["no", "yes"],
            index=0
        )

        age_enrollment = st.number_input(
            "Age_at_enrollment",
            min_value=15,
            max_value=80,
            value=18,
            step=1
        )

        application_mode = st.selectbox(
            "Application_mode",
            options=APPLICATION_MODE_OPTIONS,
            index=0
        )

        course = st.selectbox(
            "Course",
            options=COURSE_OPTIONS,
            index=0
        )

    submitted = st.form_submit_button("Prediksi Risiko")

if submitted:
    single_df = pd.DataFrame([{
        "Curricular_units_2nd_sem_approved": cu2_approved,
        "Curricular_units_2nd_sem_grade": cu2_grade,
        "Curricular_units_1st_sem_approved": cu1_approved,
        "Curricular_units_1st_sem_grade": cu1_grade,
        "Tuition_fees_up_to_date": tuition_status,
        "Debtor": debtor_status,
        "Scholarship_holder": scholarship_status,
        "Age_at_enrollment": age_enrollment,
        "Application_mode": application_mode,
        "Course": course
    }])

    result_df = predict_dropout(
        df=single_df,
        model=model,
        selected_features=selected_features,
        medium_threshold=medium_threshold,
        high_threshold=high_threshold
    )

    result = result_df.iloc[0]

    st.subheader("Hasil Prediksi")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Dropout Risk Score", f"{result['DropoutRiskScore']:.2%}")
    with m2:
        st.metric("Risk Category", result["RiskCategory"])
    with m3:
        st.metric("Predicted Dropout", "Yes" if result["PredictedDropout"] == 1 else "No")

    if result["RiskCategory"] == "High Risk":
        st.error("Mahasiswa termasuk kategori High Risk.")
    elif result["RiskCategory"] == "Medium Risk":
        st.warning("Mahasiswa termasuk kategori Medium Risk.")
    else:
        st.success("Mahasiswa termasuk kategori Low Risk.")

    st.markdown("### Rekomendasi Intervensi")
    st.write(result["RecommendedIntervention"])

    st.markdown("### Data Input")
    st.dataframe(single_df, use_container_width=True)