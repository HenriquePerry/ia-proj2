# IA Project 2 — Discount Recommendation POC

This project is a Proof of Concept (POC) for an AI-assisted discount recommendation system for a supplement brand.

The main objective is to help the company decide when it makes sense to offer discounts to customers in order to maximize customer acquisition and retention while avoiding unnecessary discounts for already loyal customers.

---

# Project Goal

Develop a machine learning model capable of recommending:

- No discount
- Small discount
- Large discount

based on customer behavior and purchase patterns using synthetic data.

---

# Problem Description

Many supplement and fitness brands apply generic discounts to all customers, reducing profit margins unnecessarily.

This project proposes an intelligent system capable of identifying:
- loyal customers who likely do not require discounts,
- new customers who may need incentives,
- inactive customers who may benefit from retention campaigns.

The goal is to optimize discount allocation through Machine Learning.

---

# Final Product (B2B — Business-to-Business)

The final product will be a web application designed for internal company use.

The application helps the supplement company answer the question:

> "Should we offer a discount to this customer?"

---

# How the System Works

## Customer Information (Inputs)

The user inserts customer-related information such as:

- Number of purchases per year
- Average spending
- Months since last purchase
- New customer status
- Purchase frequency

---

## AI Recommendation (Outputs)

After analyzing the customer, the system provides:

- Recommended discount percentage
- Customer classification
- Customer retention probability
- Risk of customer abandonment

---

# Example Workflow

## Input

| Feature | Example |
|---|---|
| Purchases per year | 2 |
| Average spending | 35€ |
| Months since last purchase | 4 |
| New customer | Yes |

---

## Output

```text
Recommended Discount: 15%
Retention Probability: High
Customer Risk Level: Medium