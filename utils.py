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