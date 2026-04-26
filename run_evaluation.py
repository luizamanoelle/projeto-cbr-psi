#começa muito semelhante ao main.py mas rodamos só para avaliar o sistema usando o método Leave-One-Out, e no final calculamos as métricas de avaliação.

import pandas as pd
import cbrkit
from collections import defaultdict
import utils
import adaptation
import evaluation

df = pd.read_csv("novo_arquivo.csv")

weights = {
    "main_issue": 0.25,
    "gad7_estimate": 0.15,
    "phq9_estimate": 0.15,
    "stress_level": 0.1,
    "sleep_quality": 0.1,
    "social_support": 0.1,
    "physical_activity": 0.05,
    "panic_symptoms": 0.05,
    "concentration_difficulty": 0.025,
    "work_or_study_impairment": 0.025
}

ranges = utils.get_ranges(df, weights.keys())

def similarity_cbr(x, y):
    return utils.global_similarity(x, y, weights, ranges)

casebase = cbrkit.loaders.file("novo_arquivo.csv")
retriever = cbrkit.retrieval.build(similarity_cbr)

# variaveis
total_casos = len(casebase)
acertos_exatos = 0
erro_adaptacao_total = 0.0

# dicionários para contagem de Verdadeiros Positivos, Falsos Positivos e Falsos Negativos por classe de intervenção
vp = defaultdict(int) 
fp = defaultdict(int) # pra quando deu algo que nao estava no caso real
fn = defaultdict(int) # pra quando nao deu algo que estava no caso real

print(f"Validação Leave-One-Out para {total_casos} casos")

# leave-one-out: para cada caso na base, vamos usá-lo como consulta 
for query_id, query_case in casebase.items():
    
    # remove o caso da consulta da base de casos para simular o Leave-One-Out
    casebase_without_query = {k: v for k, v in casebase.items() if k != query_id}
    
    # busca o vizinho mais similar usando a função de similaridade personalizada
    result = cbrkit.retrieval.apply_query(casebase_without_query, query_case, retriever)
    #pega so o caso mais similar
    best_case_id = result.ranking[0]
    best_case = casebase[best_case_id]
    
    # adapta a solucao c nossa função de adaptação, passando a query e o caso mais similar recuperado
    solucao_adaptada = adaptation.adapt_solution(query_case, best_case)
    
    # pega a solução real do caso de consulta para comparar com a solução adaptada 
    intervencao_sugerida = solucao_adaptada["intervention_type"]
    intervencao_real = query_case["intervention_type"]
    
    # calcula o erro de adaptação usando a matriz de similaridade entre intervenções do módulo de avaliação que criamos, onde o valor é a similaridade entre a intervenção sugerida e a intervenção real. O erro é 1 - similaridade, ou seja, se sugeriu exatamente o que era, o erro é 0, e se sugeriu algo completamente diferente (similaridade 0), o erro é 1.
    score_matriz = evaluation.intervention_similarity.get(intervencao_real, {}).get(intervencao_sugerida, 0.0)
    
    erro_atual = 1.0 - score_matriz
    erro_adaptacao_total += erro_atual
    
    # distribuição de acertos e erros para cálculo de métricas de avaliação
    if intervencao_sugerida == intervencao_real:
        acertos_exatos += 1
        vp[intervencao_real] += 1
    else:
        fp[intervencao_sugerida] += 1
        fn[intervencao_real] += 1

########## calculo das métricas de avaliação ##########
accuracy = acertos_exatos / total_casos
erro_medio_adaptacao = erro_adaptacao_total / total_casos

precision_total = 0
recall_total = 0

# para calcular a precisão e recall macro, precisamos considerar todas as classes de intervenção presentes na base, mesmo aquelas que não foram previstas ou que não estavam presentes no caso real, para isso usamos os dicionários de VP, FP e FN que preenchemos durante o loop. A precisão para cada classe é VP / (VP + FP) e o recall é VP / (VP + FN). Depois fazemos a média dessas precisões e recalls para obter o macro-precision e macro-recall.
todas_classes = set(vp.keys()).union(set(fp.keys())).union(set(fn.keys()))

for c in todas_classes:
    p = vp[c] / (vp[c] + fp[c]) if (vp[c] + fp[c]) > 0 else 0
    r = vp[c] / (vp[c] + fn[c]) if (vp[c] + fn[c]) > 0 else 0
    precision_total += p
    recall_total += r

#A média Macro soma a nota que ele tirou em Terapia com a nota que ele tirou em Exercício e divide por 2. Ela trata todas as doenças com a mesma importância, forçando o sistema a ser bom em tudo. Já a média Micro soma todos os acertos e erros e depois calcula a precisão e recall, dando mais peso para as classes mais frequentes. Como temos um cenário com muitas classes e algumas podem ser raras, a média Macro é mais adequada para avaliar o desempenho geral do sistema em todas as classes, enquanto a média Micro poderia ser distorcida por classes muito frequentes. Por isso optamos por calcular a média Macro aqui.
macro_precision = precision_total / len(todas_classes) if todas_classes else 0
macro_recall = recall_total / len(todas_classes) if todas_classes else 0

# para calcular o F1-Score Macro, usamos a fórmula 2 * (precision * recall) / (precision + recall). Se a soma de precisão e recall for 0, definimos o F1 como 0 para evitar divisão por zero. 
# o f1-score é a medica entre a precisão e o recall, ele é baixo se o sistema tiver baixa precisão ou baixo recall, e só é alto se ambos forem altos. Ele é útil para ter uma visão geral do desempenho do sistema considerando tanto os acertos quanto os erros.
if (macro_precision + macro_recall) > 0:
    macro_f1 = 2 * (macro_precision * macro_recall) / (macro_precision + macro_recall)
else:
    macro_f1 = 0

# resultados da avaliação
print("\n" + "..••°°°°••..°°••....••°°"*3)
print("RESULTADOS DA AVALIAÇÃO DO SISTEMA CBR")
print("..••°°°°••..°°••....••°°"*3)
print(f"Método utilizado: Leave-One-Out ({total_casos} iterações)")
print(f"Accuracy (Acurácia): ........ {accuracy:.4f} ({(accuracy*100):.1f}%)")
print(f"Precision (Macro): .......... {macro_precision:.4f}")
print(f"Recall (Macro): ............. {macro_recall:.4f}")
print(f"F1-Score (Macro): ........... {macro_f1:.4f}")
print(f"Erro Médio de Adaptação: .... {erro_medio_adaptacao:.4f}")
print("="*50)