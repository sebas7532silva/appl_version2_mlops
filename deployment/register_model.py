import mlflow
from mlflow.tracking import MlflowClient
from mlflow.exceptions import MlflowException

def register_model(run_id: str, model_name: str = "stock_classifier"):
    """
    Registra el modelo en el MLflow Model Registry.
    Si el modelo registrado no existe, lo crea primero.
    Luego crea una nueva versión y promueve el modelo a 'Staging'.
    """
    client = MlflowClient()

    # Verificar si el modelo ya está registrado
    try:
        client.get_registered_model(model_name)
    except MlflowException:
        print(f"Modelo '{model_name}' no encontrado en el registro. Creando modelo registrado...")
        client.create_registered_model(model_name)
        print(f"Modelo '{model_name}' creado.")

    # Crear nueva versión del modelo
    result = client.create_model_version(
        name=model_name,
        source=f"runs:/{run_id}/model",
        run_id=run_id
    )
    print(f"Modelo registrado: name={model_name}, version={result.version}")

    # Promover automáticamente a 'Staging'
    client.transition_model_version_stage(
        name=model_name,
        version=result.version,
        stage="Staging"
    )
    print(f"Modelo promovido a 'Staging'")


