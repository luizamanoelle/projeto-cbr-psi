from turtle import pd
import pandas as pd

import cbrkit
import utils
import adaptation

# carregamos a nova base de casos filtrada
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


# vai achar os valores mínimos e máximos das colunas numéricas para a função de similaridade
ranges = utils.get_ranges(df, weights.keys())

# função de similaridade personalizada para o CBRkit que aceita só dois casos
def similarity_cbr(x, y):
    return utils.global_similarity(x, y, weights, ranges)

# carregando a base de casos com o cbrkit
casebase = cbrkit.loaders.file("novo_arquivo.csv")

# buscar os casos mais parecidos com o problema atual dentro da base de casos usando nossa função de similaridade.
retriever = cbrkit.retrieval.build(similarity_cbr)

######### TESTE ############
# pegamos um caso específico da base para ser nossa consulta (query)
query_id = list(casebase.keys())[3] 
query = casebase[query_id]

# criamos uma nova base de casos sem o caso da query para simular o Leave-One-Out
casebase_without_query = {k: v for k, v in casebase.items() if k != query_id}

# aplicamos a consulta para recuperar os casos mais similares
result = cbrkit.retrieval.apply_query(casebase_without_query, query, retriever)

print("\n" + ".・。.・゜✭・." * 5 )
print(f"Caso de Consulta: {query_id}")
print(f"Problema principal: {query['main_issue']}")
print(".・。.・゜✭・."* 5 + "\n"  )

# o cbrkit retorna uma lista de casos ordenados por similaridade, vamos pegar os 3 mais similares pra mostrar
top_3_casos = result.ranking[:3]

for case_id in top_3_casos:
    # busca o score de similaridade do caso recuperado com a query
    score = result.similarities[case_id]
    
    # se for retornado um objeto, convertemos para float por segurança 
    score_float = float(score) 
    
    case_data = casebase[case_id]
    print(f"Caso Recuperado: {case_id} | Score de Similaridade: {score_float:.4f}")
    print(f"Problema principal do recuperado: {case_data['main_issue']}")
    print(f"Intervenção recomendada neste caso: {case_data['intervention_type']}")
    print(".・゜゜・　　・゜゜・．" * 5 )

#########################

# pegamos o id do caso mais similar e seu conteúdo para passar para a função de adaptação
best_case_id = top_3_casos[0]
best_case_data = casebase[best_case_id]

# chama a função de adaptação passando a query e o caso mais similar recuperado, e recebe a solução adaptada
solucao_final = adaptation.adapt_solution(query, best_case_data)

print("\n" + "︵‿︵‿︵‿︵"*2)
print(" SOLUÇÃO ADAPTADA")
print( "︵‿︵‿︵‿︵"*2)
print(f"Caso base utilizado: {best_case_id}")
print(f"Tipo de Intervenção: {solucao_final['intervention_type']}")
print(f"Intensidade: {solucao_final['intensity']}")
print(f"Frequência Semanal: {solucao_final['weekly_frequency']}")
print(f"Recomendação Final:\n{solucao_final['recommendation_text']}")
