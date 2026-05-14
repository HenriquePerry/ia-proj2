"""Shared utility functions for the project."""

from __future__ import annotations


DISCOUNT_LABELS = {
    0: "No discount",
    1: "Small discount",
    2: "Large discount",
}


def format_recommendation(prediction: int) -> str:
    """Convert a numeric model prediction into a user-friendly label."""
    return DISCOUNT_LABELS.get(prediction, "Unknown recommendation")
