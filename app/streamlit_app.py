from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.utils import format_recommendation

st.set_page_config(
    page_title="Discount Advisor for Nutrystore",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.result-box {
    border-radius: 12px;
    padding: 1.5rem 2rem;
    margin-top: 0.5rem;
    font-size: 1.05rem;
    line-height: 1.6;
}
.result-0 { background:#e8f5e9; border-left:5px solid #2e7d32; color:#1b5e20; }
.result-1 { background:#fff8e1; border-left:5px solid #f9a825; color:#7c5400; }
.result-2 { background:#fce4ec; border-left:5px solid #c62828; color:#7f0000; }
</style>
""", unsafe_allow_html=True)

st.title("💊 Discount Advisor for Nutrystore")
st.caption("ML-powered discount recommendation")
st.divider()

@st.cache_resource
def get_model():
    try:
        from src.model import load_model
        return load_model("data/model.pkl")
    except (NotImplementedError, FileNotFoundError):
        return None

model = get_model()

# ── Inputs ─────────────────────────────────────────────────────────────────────
st.subheader("Customer Profile")

col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Customer age", min_value=16, max_value=100, value=30)

with col2:
    novo_cliente = st.radio(
        "Customer type",
        options=[False, True],
        format_func=lambda x: "Existing" if not x else "New",
        horizontal=True,
    ) == True


if not novo_cliente:
    st.divider()
    st.caption("Purchase history")
    col3, col4 = st.columns(2)

    with col3:
        compras_ano = st.number_input(
            "Purchases per year",
            min_value=0, max_value=50, value=4,
            help="Total number of orders in the last 12 months",
        )
        gasto_medio = st.number_input(
            "Average order value (€)",
            min_value=0, max_value=500, value=60,
        )
    with col4:
        meses_sem_comprar = st.slider(
            "Months since last purchase",
            min_value=0, max_value=24, value=3,
        )
        usa_descontos = st.toggle(
            "Has responded to discounts before",
            value=False,
            help="Did this customer use a discount when previously offered?",
        )
else:
    # new customer: set sensible defaults, no history available
    compras_ano       = 0
    gasto_medio       = 0
    meses_sem_comprar = 0
    usa_descontos     = False

st.divider()


EXPLANATIONS = {
    0: "✅ Loyal customer: no incentive needed.",
    10: "⚠️ A small discount may help retain this customer.",
    15: "🔴 High churn risk: a strong offer is recommended.",
}
CSS_CLASSES = {0: "result-0", 1: "result-1", 2: "result-2"}

if st.button("Get Recommendation", type="primary", use_container_width=True):
    inputs = {
        "compras_ano":       compras_ano,
        "gasto_medio":       gasto_medio,
        "meses_sem_comprar": meses_sem_comprar,
        "novo_cliente":      int(novo_cliente),
        "idade":             idade,
        "usa_descontos":     int(usa_descontos),
    }

    if model is not None:
        import pandas as pd
        prediction = int(model.predict(pd.DataFrame([inputs]))[0])
    else:
        st.warning("Model not trained yet.")
    

    st.subheader("Recommendation")
    st.markdown(f"""
    <div class="result-box {CSS_CLASSES.get(prediction, 'result-1')}">
        <strong style="font-size:1.35rem">{format_recommendation(prediction)}</strong><br/>
        {EXPLANATIONS.get(prediction, '')}
    </div>
    """, unsafe_allow_html=True)