# funções de apoio

# coeficiente de similaridade pra main_issue
def jaccard_similarity(a, b):
    set_a = set(a.lower().split())
    set_b = set(b.lower().split())
    
    intersection = set_a & set_b
    union = set_a | set_b
    
    if len(union) == 0:
        return 0
    
    return len(intersection) / len(union)

# exclui as features que não serão utilizadas 
def remove_features(df, features_to_remove):
    return df.drop(columns=features_to_remove, errors="ignore")

# faz codificação ordinal/binária
def encode_ordinal(df, mappings):
    df = df.copy()
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)
    return df

# pega valores mínimos e máximos das colunas pra função de similaridade
def get_ranges(df, columns):
    ranges = {}
    
    for col in columns:
        col_data = df[col].dropna()
        ranges[col] = (col_data.min(), col_data.max())
    
    return ranges

# faz similaridade da distância normalizada
def numeric_similarity(a, b, min_val, max_val):
    if max_val == min_val:
        return 1.0  
    
    return 1 - abs(a - b) / (max_val - min_val)

# similaridade por igualdade
def categorical_similarity(a, b):
    return 1.0 if a == b else 0.0

# similaridade global
def global_similarity(case1, case2, weights, ranges):
    sim_total = 0.0
    
    for attr, w in weights.items():
        val1 = case1[attr]
        val2 = case2[attr]
        
        if attr == "main_issue":
            sim = jaccard_similarity(val1, val2)
        
        elif attr == "concentration_difficulty" | attr == "panic_symptoms":
            sim = categorical_similarity(val1, val2)    
            
        else:
            min_val, max_val = ranges[attr]
            sim = numeric_similarity(val1, val2, min_val, max_val)
        
        sim_total += w * sim
    
    return sim_total