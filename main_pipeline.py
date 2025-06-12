import time
import mlflow
from datetime import datetime
from features.feature_engineering import prepare_features
from models.train_model import train_model
from evaluation.evaluate import is_model_better
from deployment.register_model import register_model
from utils.telegram_notify import send_telegram_message
from data.fetch_data import get_crypto_price

def main():
    send_telegram_message("🚀 Pipeline iniciado!")

    clf, acc, f1 = None, None, None
    df_raw = get_crypto_price()
    df = prepare_features(df_raw)
    
    clf, acc, f1, run_id = train_model(df)
    
    model_name = "stock_classifier"
    if is_model_better(f1, model_name):
        register_model(run_id, model_name)
        send_telegram_message(f"✅ Nuevo modelo registrado con F1={f1:.3f}")
    else:
        send_telegram_message("❌ Modelo no mejora el anterior. No se registra.")
    
    try:
        production_model_uri = "models:/stock_classifier/Staging"
        model = mlflow.pyfunc.load_model(production_model_uri)

        last_features = df.drop(columns=["target"]).iloc[[-1]]
        prediction = model.predict(last_features)[0]
        
        next_day = (datetime.utcnow().date()).isoformat()
        pred_msg = f"🔮 Predicción para {next_day}: " + ("📈 SUBE" if prediction == 1 else "📉 BAJA")
        send_telegram_message(pred_msg)
    except Exception as e:
        send_telegram_message(f"⚠️ Error al cargar modelo o hacer la predicción: {str(e)}")

    send_telegram_message("🏁 Pipeline finalizado.")

if __name__ == "__main__":
    main()

