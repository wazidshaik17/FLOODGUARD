"""
ML Model Training Pipeline for FLOODGUARD
Trains Random Forest Regressor & Classifier for Hilly Flash Flood Prediction.

DISCLAIMER:
This model is trained on synthetic hydrological data simulating hilly terrain.
Performance metrics reflect synthetic validation and must not be construed as
certified operational benchmarks for live disaster management deployment.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

def train_and_export():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ml_root = os.path.dirname(base_dir)
    datasets_dir = os.path.join(ml_root, 'datasets')
    models_dir = os.path.join(ml_root, 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    # Import generator
    import sys
    sys.path.append(datasets_dir)
    from generate_dataset import generate_synthetic_flood_data
    
    csv_file = os.path.join(datasets_dir, 'synthetic_flood_dataset.csv')
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = generate_synthetic_flood_data(6000)
        df.to_csv(csv_file, index=False)
        
    feature_cols = [
        'rainfall_intensity',
        'rainfall_accum_24h',
        'soil_moisture',
        'water_level',
        'rate_of_rise',
        'terrain_slope',
        'elevation',
        'drainage_proximity',
        'historical_flood_index',
        'forecast_rain_3h'
    ]
    
    X = df[feature_cols]
    y_reg = df['risk_score']
    y_clf = df['risk_level']
    
    X_train, X_test, y_reg_train, y_reg_test, y_clf_train, y_clf_test = train_test_split(
        X, y_reg, y_clf, test_size=0.2, random_state=42, stratify=y_clf
    )
    
    print("Training Random Forest Regressor & Classifier...")
    regressor = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    regressor.fit(X_train, y_reg_train)
    
    classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    classifier.fit(X_train, y_clf_train)
    
    # Evaluations
    y_reg_pred = regressor.predict(X_test)
    y_clf_pred = classifier.predict(X_test)
    
    r2 = float(r2_score(y_reg_test, y_reg_pred))
    mae = float(mean_absolute_error(y_reg_test, y_reg_pred))
    rmse = float(root_mean_squared_error(y_reg_test, y_reg_pred))
    
    acc = float(accuracy_score(y_clf_test, y_clf_pred))
    prec = float(precision_score(y_clf_test, y_clf_pred, average='weighted', zero_division=0))
    rec = float(recall_score(y_clf_test, y_clf_pred, average='weighted', zero_division=0))
    f1 = float(f1_score(y_clf_test, y_clf_pred, average='weighted', zero_division=0))
    
    importances = dict(zip(feature_cols, [float(x) for x in regressor.feature_importances_]))
    # Sort by importance
    importances = dict(sorted(importances.items(), key=lambda item: item[1], reverse=True))
    
    metrics = {
        'model_name': 'Random Forest Flash Flood Predictor (Hilly Terrain)',
        'trained_at': datetime.utcnow().isoformat() + 'Z',
        'is_demo_dataset': True,
        'disclaimer': 'Trained on synthetic hydrological and geomorphological data. For research & demonstration purposes only.',
        'features': feature_cols,
        'regression_metrics': {
            'r2_score': round(r2, 4),
            'mae': round(mae, 3),
            'rmse': round(rmse, 3)
        },
        'classification_metrics': {
            'accuracy': round(acc, 4),
            'precision': round(prec, 4),
            'recall': round(rec, 4),
            'f1_score': round(f1, 4)
        },
        'feature_importances': importances
    }
    
    # Save artifacts
    bundle = {
        'regressor': regressor,
        'classifier': classifier,
        'features': feature_cols,
        'metadata': metrics
    }
    
    model_path = os.path.join(models_dir, 'flood_risk_model.joblib')
    metadata_path = os.path.join(models_dir, 'model_metadata.json')
    
    joblib.dump(bundle, model_path)
    with open(metadata_path, 'w') as f:
        json.dump(metrics, f, indent=2)
        
    print(f"\n================ MODEL TRAINING COMPLETE ================")
    print(f"Artifacts saved to: {model_path}")
    print(f"Metadata saved to: {metadata_path}")
    print(f"R2 Score: {metrics['regression_metrics']['r2_score']}")
    print(f"Classification Accuracy: {metrics['classification_metrics']['accuracy'] * 100:.2f}%")
    print(f"F1 Score: {metrics['classification_metrics']['f1_score']:.4f}")
    print("\nFeature Importances:")
    for k, v in importances.items():
        print(f"  {k:25s}: {v*100:.1f}%")
    print("=========================================================\n")
    
    return metrics

if __name__ == '__main__':
    train_and_export()
