import argparse
from feature_extractor import extract_features
from model.classifier import load_model
import pandas as pd

def classify_domains(domain_list):
    features = extract_features(domain_list)
    model = load_model()
    predictions = model.predict(features)
    return pd.DataFrame({
        "domain": domain_list,
        "prediction": predictions
    })

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input file with domains (one per line)")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        domains = [line.strip() for line in f.readlines()]

    results = classify_domains(domains)
    results.to_csv("data/output.csv", index=False)
    print("Classification complete. Results saved to data/output.csv.")
