from evaluation.evaluate import is_model_better

def test_is_model_better_no_previous():
    # Suponemos que no hay modelo previo y devuelve True
    assert is_model_better(0.8, "modelo_que_no_existe")

def test_is_model_better_with_previous(monkeypatch):
    # Simulamos MLflow con monkeypatch o mock (esto requiere pytest-mock o unittest.mock)
    # Aquí solo mostramos la idea simplificada:
    pass
