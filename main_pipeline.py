import time
from datetime import datetime
from data.fetch_data import fetch_stock_data
from features.feature_engineering import prepare_features
from models.train_model import train_model
from evaluation.evaluate import is_model_better
from deployment.register_model import register_model
from utils.telegram_notify import send_telegram_message

def main():
    send_telegram_message("🚀 Pipeline iniciado!")

    # Entrenamiento con notificación periódica
    start_time = datetime.now()
    last_notify = start_time

    clf, acc, f1 = None, None, None
    
    # Simulamos entrenamiento largo con 3 iteraciones para ejemplo
    for i in range(3):
        clf, acc, f1 = train_model(df)
        now = datetime.now()
        elapsed = (now - last_notify).seconds
        if elapsed >= 3600 or i == 0:  # si pasó 1 hora o es la primera iteración
            notifier.send_message(f"⏳ Iteración {i+1} completada: Accuracy={acc:.3f}, F1={f1:.3f}")
            last_notify = now

    # Validar si el modelo es mejor que el último registrado
    model_name = "stock_classifier"
    if is_model_better(f1, model_name):
        run_id = mlflow.active_run().info.run_id  # asumiendo run activo en train_model()
        register_model(run_id, model_name)
        send_telegram_message(f"✅ Nuevo modelo registrado con F1={f1:.3f}")
    else:
        send_telegram_message("❌ Modelo no mejora el anterior. No se registra.")

    send_telegram_message("🏁 Pipeline finalizado.")

if __name__ == "__main__":
    main()

