from __future__ import annotations

import pickle

from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.dummy import DummyClassifier

 
FEATURES = [
    "compras_ano",
    "gasto_medio",
    "meses_sem_comprar",
    "novo_cliente",
    "idade",
    "usa_descontos",
]
TARGET = "desconto"


def train_model(dataset: pd.DataFrame):
    """Train and evaluate 3 classifiers + a baseline.
 
    Returns a dict with the best model and all results.
    """
    
    X = dataset[FEATURES]
    y = dataset[TARGET]
    
    # division of the dataset in parts 
    # 80% training; 20% testing
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=6, random_state=42),
        "Naive Bayes": GaussianNB(),
        "Neural Network": MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42),
        "Baseline":       DummyClassifier(strategy="most_frequent", random_state=42),
    }
    
    results = {}
    best_model = None
    best_accuracy = -1
    
    for name, algo in models.items():
        algo.fit(x_train, y_train)
        y_pred = algo.predict(x_test)
        acc = accuracy_score(y_test, y_pred)
        
        results[name] = {
            "model" : algo,
            "accuracy" : acc,
            "report" : classification_report(y_test, y_pred, output_dict=True),
            "confusion" : confusion_matrix(y_test, y_pred).tolist()
        }
        
        print(f"\n── {name} ──")
        print(f"Accuracy: {acc:.3f}")
        print(classification_report(y_test, y_pred))
        
        if name != "Baseline" and acc > best_accuracy:
            best_accuracy = acc
            best_model = algo
    
    print(f"\nBest model: {type(best_model).__name__} ({best_accuracy:.3f} accuracy)")
    print(f"Baseline accuracy: {results['Baseline']['accuracy']:.3f}")
 
    return {"best_model": best_model, "results": results}



# ── Inference ──────────────────────────────────────────────────────────────────
 
def predict(model, inputs: dict) -> tuple[int, dict]:
    """Run inference on a single customer profile.
 
    Returns (predicted_class, probability_dict).
    """
    X = pd.DataFrame([inputs])[FEATURES]
    prediction = int(model.predict(X)[0])
    probabilities = {
        int(cls): round(float(prob), 3)
        for cls, prob in zip(model.classes_, model.predict_proba(X)[0])
    }
    return prediction, probabilities
 

def save_model(model, output_path: str | Path) -> Path:
    """Persist the trained model artifact."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "wb") as f:
        pickle.dump(model, f)
    
    print(f"Model saved to {output_path}")
    return output_path


def load_model(model_path: str | Path):
    """Load a saved model artifact."""
    with open(Path(model_path), "rb") as f:
        return pickle.load(f)
    
    
if __name__ == "__main__":
    import sys
 
    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/clientes.csv"
    model_path = sys.argv[2] if len(sys.argv) > 2 else "data/model.pkl"
 
    print(f"Loading dataset from {data_path}...")
    df = pd.read_csv(data_path)
 
    output = train_model(df)
    save_model(output["best_model"], model_path)
