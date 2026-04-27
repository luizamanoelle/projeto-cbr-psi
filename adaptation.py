# receber o novo paciente (query) e o caso mais similar recuperado, e retornar uma solução adaptada
def adapt_solution(query, retrieved_case):   
    # pegamos a solução do caso recuperado como ponto de partida pra definir a solução adaptada
    adapted_solution = {
        "intervention_type": retrieved_case["intervention_type"],
        "intensity": int(retrieved_case["intensity"]),
        "weekly_frequency": int(retrieved_case["weekly_frequency"]),
        "recommendation_text": retrieved_case["recommendation_text"]
    }

    # se o novo paciente tem um nivel de ansiedade 2 pontos maior que o caso recuperado, aumentamos a intensidade da intervenção em 1 (máximo 5).
    if query["gad7_estimate"] > retrieved_case["gad7_estimate"] + 2:
        adapted_solution["intensity"] = min(5, adapted_solution["intensity"] + 1)
    # se for 2 pontos menor, diminuímos a intensidade em 1 (mínimo 1).
    elif query["gad7_estimate"] < retrieved_case["gad7_estimate"] - 2:
         adapted_solution["intensity"] = max(1, adapted_solution["intensity"] - 1)

   # se o novo paciente tem um nível de estresse alto (7 ou mais), mas o caso recuperado tinha uma frequência semanal baixa (<3), aumentamos a frequência para pelo menos 3 sessões semanais.
    if query["stress_level"] >= 7 and adapted_solution["weekly_frequency"] < 3:
        adapted_solution["weekly_frequency"] = 3

    return adapted_solution