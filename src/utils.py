"""Shared utility functions for the project."""

from __future__ import annotations


DISCOUNT_LABELS = {
    0:  "No Discount",
    10: "Small Discount",
    15: "Large Discount",
}


def format_recommendation(prediction: int) -> str:
    """Convert a numeric model prediction into a user-friendly label."""
    return DISCOUNT_LABELS.get(prediction, "Unknown recommendation")
