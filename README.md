# 🧠📈 Bitcoin Predictor: MLOps Pipeline con CI/CD y Notificaciones en Tiempo Real 🚀

> Predicción automatizada del comportamiento del Bitcoin usando aprendizaje automático, un pipeline de MLOps completo y alertas directas a Telegram. Todo corre solito... como por arte de magia 🤖✨

---

## 🗂 Descripción

Este proyecto implementa un sistema MLOps completo que:
- Extrae datos financieros relevantes del mercado de Bitcoin
- Aplica técnicas de ingeniería de características y preprocesamiento
- Entrena y evalúa modelos de clasificación para predecir el comportamiento del precio
- Versiona automáticamente los modelos con MLflow
- Notifica los resultados directamente a tu cuenta de **Telegram**
- Se ejecuta automáticamente cada hora vía **GitHub Actions**

Todo esto sin necesidad de intervención manual. Solo siéntate y recibe los resultados. 📲💡

---

## 🧠 ¿Qué predice este modelo?

El modelo predice si el **precio de Bitcoin subirá o bajará**, con base en indicadores como:

- `ma_5`, `ma_10`: medias móviles
- `volatility`: volatilidad reciente
- `ma_diff`: diferencia entre medias móviles
- `volume_change`: cambio porcentual en volumen
- `return`: rendimiento anterior

---

## ⚙️ Tecnologías utilizadas

| Herramienta         | Uso                                                       |
|---------------------|-----------------------------------------------------------|
| **Python 3.9**      | Lenguaje principal del proyecto                           |
| **pandas / scikit-learn** | Análisis de datos, procesamiento, entrenamiento de modelos |
| **pytest**          | Pruebas automáticas                                       |
| **MLflow**          | Registro, versionado y gestión de modelos ML              |
| **GitHub Actions**  | Automatización CI/CD y ejecuciones cada hora              |
| **Telegram API**    | Notificaciones automáticas de éxito o fallo               |

---

## 📦 Estructura del repositorio

```bash
.
├── main_pipeline.py                # Pipeline principal: ejecuta todo el flujo
├── fetch_data/                    # Módulo de obtención de datos
├── features/                      # Ingeniería de características
├── models/                        # Entrenamiento y predicción
├── deployment/
│   └── register_model.py          # Registro del modelo en MLflow
├── tests/                         # Pruebas unitarias con pytest
├── utils/
│   └── telegram_notify.py         # Script para enviar mensajes a Telegram
├── requirements.txt
└── .github/workflows/ci_cd.yml    # Pipeline CI/CD automatizado
