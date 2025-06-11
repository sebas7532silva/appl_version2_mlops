import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

def train_model(df: pd.DataFrame):
    """
    Entrena un modelo RandomForestClassifier y registra el experimento en MLflow.
    """
    features = ['return', 'ma_5', 'ma_10', 'volatility', 'ma_diff', 'volume_change']
    target = 'target'
    
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    clf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=7)
    
    with mlflow.start_run():
        clf.fit(X_train, y_train)
        
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        # Log params and metrics
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # Log model
        mlflow.sklearn.log_model(clf, artifact_path="model")

    return clf, acc, f1

