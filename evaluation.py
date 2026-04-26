# matriz de similaridade pra avaliar a acurácia da solução apresentada
intervention_similarity = {
    "therapy": {"therapy": 1, "combined": 0.8, "exercise": 0.3, "psychoeducation": 0.5, "sleep_hygiene": 0.2},
    "exercise": {"therapy": 0.3, "combined": 0.7, "exercise": 1, "psychoeducation": 0.4, "sleep_hygiene": 0.6},
    "psychoeducation": {"therapy": 0.5, "combined": 0.7, "exercise": 0.4, "psychoeducation": 1, "sleep_hygiene": 0.4},
    "combined": {"therapy": 0.8, "combined": 1, "exercise": 0.7, "psychoeducation": 0.7, "sleep_hygiene": 0.7},
    "sleep_hygiene": {"therapy": 0.2, "combined": 0.7, "exercise": 0.6, "psychoeducation": 0.4, "sleep_hygiene": 1}
}