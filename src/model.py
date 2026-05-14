"""Model training and inference helpers for the discount recommendation POC."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def train_model(dataset: pd.DataFrame):
    """Train the recommendation model from a dataset.

    Replace this placeholder with the chosen classifier and preprocessing pipeline.
    """
    raise NotImplementedError("Model training is not implemented yet.")


def save_model(model, output_path: str | Path) -> Path:
    """Persist the trained model artifact."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError("Model saving is not implemented yet.")


def load_model(model_path: str | Path):
    """Load a saved model artifact."""
    raise NotImplementedError("Model loading is not implemented yet.")
