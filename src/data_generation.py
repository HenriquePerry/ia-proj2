"""Synthetic data generation for the discount recommendation POC."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def generate_synthetic_data(n_samples: int = 1000, random_state: int = 42) -> pd.DataFrame:
    """Return a synthetic customer dataset.

    Replace this placeholder with the final feature engineering rules and target logic.
    """
    raise NotImplementedError("Synthetic data generation is not implemented yet.")


def save_dataset(output_path: str | Path, n_samples: int = 1000, random_state: int = 42) -> Path:
    """Generate and save the synthetic dataset to CSV."""
    dataset = generate_synthetic_data(n_samples=n_samples, random_state=random_state)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(output_path, index=False)
    return output_path
