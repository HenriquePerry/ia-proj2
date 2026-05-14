"""Streamlit entry point for the discount recommendation demo."""

from __future__ import annotations

import streamlit as st

from src.utils import format_recommendation


def main() -> None:
    st.set_page_config(page_title="Discount POC", page_icon="💊", layout="centered")
    st.title("Discount Recommendation POC")
    st.write("This app will recommend a discount level for a customer profile.")

    customer_type = st.selectbox("Customer type", ["New", "Occasional", "Regular"])
    purchases_last_6_months = st.slider("Purchases in last 6 months", 0, 20, 3)

    if st.button("Get recommendation"):
        if customer_type == "New":
            prediction = 2
        elif customer_type == "Occasional":
            prediction = 1 if purchases_last_6_months < 4 else 0
        else:
            prediction = 0

        st.success(format_recommendation(prediction))


if __name__ == "__main__":
    main()
