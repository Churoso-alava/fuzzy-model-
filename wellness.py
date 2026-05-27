"""
Wellness (Hooper modificado) para evaluación pre-entrenamiento.
"""

from __future__ import annotations


def calcular_wellness(
    sueno: int,
    fatiga: int,
    estres: int,
    dolor: int,
    humor: int,
) -> float:
    """
    Calcula el indice de wellness normalizado W_norm en [0, 1] basado en el
    Cuestionario de Hooper Modificado (5 items, escala Likert 1-7).

    Items descendentes (1=optimo): sueno, fatiga, estres, dolor.
        w_i = (7 - valor) / 6.0

    Item ascendente (7=optimo): humor.
        w_humor = (valor - 1) / 6.0

    W_norm = media aritmetica de los 5 componentes normalizados.
    W_norm = 1.0 optimo | W_norm = 0.0 pesimo.
    """
    items = {"sueno": sueno, "fatiga": fatiga, "estres": estres, "dolor": dolor, "humor": humor}
    for nombre, val in items.items():
        if not (1 <= val <= 7):
            raise ValueError(f"Item '{nombre}' fuera del rango Hooper [1, 7]. Recibido: {val}")

    w_sueno = (7 - sueno) / 6.0
    w_fatiga = (7 - fatiga) / 6.0
    w_estres = (7 - estres) / 6.0
    w_dolor = (7 - dolor) / 6.0
    w_humor = (humor - 1) / 6.0
    return (w_sueno + w_fatiga + w_estres + w_dolor + w_humor) / 5.0
