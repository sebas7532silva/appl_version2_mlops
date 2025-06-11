import mlflow
from mlflow.tracking import MlflowClient

def register_model(run_id: str, model_name: str = "stock_classifier"):
    """
    Registra el modelo en el MLflow Model Registry.
    """
    client = MlflowClient()
    
    result = client.create_model_version(
        name=model_name,
        source=f"runs:/{run_id}/model",
        run_id=run_id
    )
    print(f"Modelo registrado: name={model_name}, version={result.version}")
    
    # Opcional: promoverlo a Staging o Production automáticamente
    client.transition_model_version_stage(
        name=model_name,
        version=result.version,
        stage="Staging"
    )
    print(f"Modelo promovido a 'Staging'")

