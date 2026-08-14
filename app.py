import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   MAIN APPLICATION
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 15% 5%,
            rgba(37, 99, 235, 0.22),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(14, 165, 233, 0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #07111f 0%,
            #0b1729 45%,
            #0f1f35 100%
        );

    color: #e5e7eb;
}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}


/* ============================================================
   TOP STREAMLIT HEADER
   ============================================================ */

[data-testid="stHeader"] {
    background: rgba(7, 17, 31, 0.85);
}


/* ============================================================
   MAIN HEADER
   ============================================================ */

.main-header {
    background:
        linear-gradient(
            135deg,
            #111827 0%,
            #172554 45%,
            #2563eb 100%
        );

    padding: 2.5rem 2.7rem;

    border-radius: 22px;

    margin-bottom: 1.5rem;

    border: 1px solid rgba(96, 165, 250, 0.25);

    box-shadow:
        0 15px 40px rgba(0, 0, 0, 0.35);
}

.main-header h1 {
    color: #ffffff;

    font-size: 2.5rem;

    margin-bottom: 0.45rem;

    font-weight: 750;
}

.main-header p {
    color: #bfdbfe;

    font-size: 1.05rem;

    margin-bottom: 0;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #0b1424 0%,
            #0f1d32 100%
        );

    border-right: 1px solid #243b5a;
}


/* Sidebar text */

section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}


/* Sidebar headings */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff;
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-title {
    font-size: 1.4rem;

    font-weight: 700;

    color: #f8fafc;

    margin-top: 1.2rem;

    margin-bottom: 0.25rem;
}

.section-description {
    color: #94a3b8;

    font-size: 0.92rem;

    margin-bottom: 1rem;
}


/* ============================================================
   NORMAL TEXT
   ============================================================ */

.stMarkdown p {
    color: #cbd5e1;
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

label {
    font-weight: 550 !important;

    color: #cbd5e1 !important;
}


/* ============================================================
   SELECT BOXES
   ============================================================ */

[data-baseweb="select"] > div {

    background-color: #172235 !important;

    border: 1px solid #334155 !important;

    border-radius: 10px !important;

    color: #f8fafc !important;
}


/* Select text */

[data-baseweb="select"] span {
    color: #f8fafc !important;
}


/* Dropdown arrow */

[data-baseweb="select"] svg {
    fill: #94a3b8 !important;
}


/* ============================================================
   NUMBER INPUT
   ============================================================ */

[data-testid="stNumberInput"] input {

    background-color: #172235 !important;

    color: #f8fafc !important;

    border: 1px solid #334155 !important;

    border-radius: 10px !important;
}


/* Number input buttons */

[data-testid="stNumberInput"] button {

    background-color: #1e293b !important;

    color: #cbd5e1 !important;

    border-color: #334155 !important;
}


/* ============================================================
   HELP TEXT
   ============================================================ */

.stCaption {
    color: #94a3b8 !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: #263852 !important;
}


/* ============================================================
   HOW DOES THIS WORK
   ============================================================ */

[data-testid="stExpander"] {

    background-color: rgba(15, 29, 50, 0.75);

    border: 1px solid #2b4363;

    border-radius: 12px;
}


/* ============================================================
   PREDICT BUTTON
   ============================================================ */

.stButton > button {

    width: 100%;

    height: 3.2rem;

    border-radius: 11px;

    font-size: 1rem;

    font-weight: 650;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #3b82f6
        );

    color: white;

    border: 1px solid #60a5fa;

    box-shadow:
        0 8px 20px rgba(37, 99, 235, 0.25);

    transition: all 0.2s ease;
}


/* Button hover */

.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #1d4ed8,
            #2563eb
        );

    border-color: #93c5fd;

    transform: translateY(-1px);

    box-shadow:
        0 10px 25px rgba(37, 99, 235, 0.35);
}


/* ============================================================
   METRIC
   ============================================================ */

[data-testid="stMetric"] {

    background: rgba(15, 29, 50, 0.8);

    padding: 1rem;

    border-radius: 14px;

    border: 1px solid #2b4363;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

[data-testid="stMetricValue"] {
    color: #f8fafc !important;
}


/* ============================================================
   INFO / SUCCESS / WARNING / ERROR
   ============================================================ */

[data-testid="stAlert"] {

    border-radius: 12px;

    border-width: 1px;
}


/* ============================================================
   PROGRESS BAR
   ============================================================ */

[data-testid="stProgressBar"] {

    background-color: #1e293b;

    border-radius: 20px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #64748b;

    font-size: 0.82rem;

    margin-top: 2rem;

    padding-top: 1rem;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #07111f;
}

::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #475569;
}

</style>
""", unsafe_allow_html=True)
# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("customer_churn_model.pkl")


model = load_model()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 📊 Churn Predictor")

    st.markdown("---")

    st.markdown("### About the project")

    st.write(
        """
        This application uses Machine Learning to estimate
        the likelihood that a telecom customer may leave
        the company.
        """
    )

    st.markdown("### 🤖 Model")

    st.info(
        """
        **Logistic Regression**

        The model was trained using customer demographics,
        services, contract information and billing data.
        """
    )

    st.markdown("### 📈 Evaluation")

    st.write("Accuracy: **80.55%**")
    st.write("ROC-AUC: **0.8421**")
    st.write("Churn F1-score: **0.60**")

    st.markdown("---")

    st.markdown("### 🛠️ Technologies")

    st.write(
        """
        • Python  
        • Pandas  
        • Scikit-learn  
        • Streamlit  
        • Machine Learning
        """
    )


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="main-header">
<h1>📊 Customer Churn Predictor</h1>
<p>Identify customers who may be at risk of leaving and understand their estimated churn probability.</p>
</div>
""", unsafe_allow_html=True)
# ============================================================
# HOW TO USE
# ============================================================

with st.expander("ℹ️ How does this work?"):

    st.markdown("""
    ### Simple 3-step process

    **1️⃣ Enter customer information**

    Provide details about the customer's services,
    contract and billing.

    **2️⃣ Run the prediction**

    Click **Predict Churn Risk**.

    **3️⃣ Understand the result**

    The model will estimate the probability that
    the customer may leave the company.

    ### Risk levels

    🟢 **Low Risk** — probability below 30%

    🟠 **Medium Risk** — probability between 30% and 60%

    🔴 **High Risk** — probability above 60%

    > The prediction is an ML-based estimate and should
    > be used as a decision-support tool rather than a
    > guaranteed outcome.
    """)


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Tell us about the customer and their relationship with the company.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col2:
    senior_citizen = st.selectbox(
        "Senior citizen?",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

with col3:
    tenure = st.number_input(
        "Customer tenure",
        min_value=0,
        max_value=72,
        value=12,
        step=1,
        help="Number of months the customer has been with the company."
    )

st.caption("💡 Tenure means how long the customer has been using the service.")


col1, col2, col3 = st.columns(3)

with col1:
    partner = st.selectbox(
        "Has a partner?",
        ["Yes", "No"]
    )

with col2:
    dependents = st.selectbox(
        "Has dependents?",
        ["Yes", "No"]
    )

with col3:
    phone_service = st.selectbox(
        "Uses phone service?",
        ["Yes", "No"]
    )


st.divider()


# ============================================================
# SERVICES
# ============================================================

st.markdown(
    '<div class="section-title">📡 Services Used</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Select the services currently used by the customer.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    multiple_lines = st.selectbox(
        "Multiple phone lines",
        ["No", "Yes", "No phone service"]
    )

with col2:
    internet_service = st.selectbox(
        "Internet service",
        ["DSL", "Fiber optic", "No"]
    )

with col3:
    online_security = st.selectbox(
        "Online security",
        ["Yes", "No", "No internet service"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    online_backup = st.selectbox(
        "Online backup",
        ["Yes", "No", "No internet service"]
    )

with col2:
    device_protection = st.selectbox(
        "Device protection",
        ["Yes", "No", "No internet service"]
    )

with col3:
    tech_support = st.selectbox(
        "Technical support",
        ["Yes", "No", "No internet service"]
    )


col1, col2 = st.columns(2)

with col1:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

with col2:
    streaming_movies = st.selectbox(
        "Streaming movies",
        ["Yes", "No", "No internet service"]
    )


st.divider()


# ============================================================
# ACCOUNT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">💳 Account & Billing</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Enter information related to the customer account and payments.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contract type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ],
        help="How long the customer's current contract lasts."
    )

with col2:
    paperless_billing = st.selectbox(
        "Paperless billing?",
        ["Yes", "No"]
    )

with col3:
    payment_method = st.selectbox(
        "Payment method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Monthly bill",
        min_value=0.0,
        max_value=1000.0,
        value=70.0,
        step=1.0,
        help="Approximate amount charged every month."
    )

with col2:
    total_charges = st.number_input(
        "Total amount paid so far",
        min_value=0.0,
        max_value=100000.0,
        value=840.0,
        step=10.0,
        help="Approximate total amount charged since the customer joined."
    )


st.divider()


# ============================================================
# PREDICT BUTTON
# ============================================================

predict_button = st.button(
    "🔍  Predict Customer Churn Risk",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    customer_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    # Make prediction
    prediction = model.predict(customer_data)[0]
    probability = model.predict_proba(customer_data)[0][1]


    # ========================================================
    # DETERMINE RISK LEVEL
    # ========================================================

    if probability < 0.30:

        risk_level = "LOW RISK"
        risk_icon = "🟢"

        risk_message = (
            "This customer currently shows characteristics "
            "associated with a lower likelihood of churn."
        )

    elif probability < 0.60:

        risk_level = "MEDIUM RISK"
        risk_icon = "🟠"

        risk_message = (
            "This customer shows some characteristics "
            "associated with potential churn."
        )

    else:

        risk_level = "HIGH RISK"
        risk_icon = "🔴"

        risk_message = (
            "This customer shows characteristics associated "
            "with a higher likelihood of leaving."
        )


    # ========================================================
    # PREDICTION RESULT
    # ========================================================

    st.markdown("## 🎯 Prediction Result")

    result_col1, result_col2 = st.columns([1, 2])

    with result_col1:

        if probability < 0.30:

            st.success("### 🟢 LOW RISK")

        elif probability < 0.60:

            st.warning("### 🟠 MEDIUM RISK")

        else:

            st.error("### 🔴 HIGH RISK")


    with result_col2:

        st.metric(
            label="Estimated Churn Probability",
            value=f"{probability:.1%}"
        )


    st.progress(
        float(probability),
        text=f"Churn probability: {probability:.1%}"
    )


    st.info(risk_message)


    # ========================================================
    # BUSINESS RECOMMENDATION
    # ========================================================

    if probability >= 0.60:

        st.error(
            """
            ### 💡 Recommended Action

            Consider prioritizing this customer for a retention
            review. The business could investigate their contract,
            service experience, billing pattern and support needs.
            """
        )

    elif probability >= 0.30:

        st.warning(
            """
            ### 💡 Recommended Action

            Consider monitoring this customer and reviewing their
            recent service experience or engagement.
            """
        )

    else:

        st.success(
            """
            ### 💡 Recommended Action

            No immediate high-risk signal was detected. Continue
            normal customer engagement and service monitoring.
            """
        )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.markdown("---")

with st.expander("🤖 About the Machine Learning Model"):

    st.markdown(
        """
        This project compares multiple classification algorithms
        and uses **Logistic Regression** as the final prediction model.

        **Model Performance:**

        | Metric | Score |
        |---|---:|
        | Accuracy | 80.55% |
        | ROC-AUC | 84.21% |
        | Churn Recall | 56% |
        | Churn F1-score | 60% |

        The model was trained using customer demographic,
        service, contract and billing information.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📊 Customer Churn Prediction • "
    "End-to-End Machine Learning Project • "
    "Python • Scikit-learn • Streamlit"
)