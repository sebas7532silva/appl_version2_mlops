import mlflow
from mlflow.tracking import MlflowClient

def is_model_better(new_f1_score: float, model_name: str) -> bool:
    """
    Compara el nuevo modelo con el último registrado en MLflow.
    Devuelve True si es mejor, False si no.
    """
    client = MlflowClient()

    try:
        latest_version = client.get_latest_versions(name=model_name, stages=["Production", "Staging"])
        if not latest_version:
            print("No previous model found, accepting new model.")
            return True

        # Tomamos la última versión registrada en cualquier etapa
        run_id = latest_version[0].run_id
        old_f1_score = float(client.get_run(run_id).data.metrics['f1_score'])

        print(f"Previous F1 Score: {old_f1_score}, New F1 Score: {new_f1_score}")
        return new_f1_score > old_f1_score
    
    except Exception as e:
        print(f"Error during model comparison: {e}")
        return True

