import cbrkit
import utils
from cbrkit.similarity import linear, euclidean, numeric
from cbrkit.similarity.numeric import interval

# carregando a base de casos a partir do arquivo CSV
casebase = cbrkit.loaders.file("cbr_psychology_110_cases_clinical.csv")

#teste 
print("Casos carregados:", len(casebase))

#separação dos problemas e soluções
problems = [  "stress_level", "sleep_quality",
    "social_support", "physical_activity", "gad7_estimate", "phq9_estimate",
    "panic_symptoms", "concentration_difficulty", "irritability_level",
    "work_or_study_impairment", "clinical_severity",
    "main_issue"]

solutions = ["intervention_type",
    "intensity",
    "weekly_frequency",
    "recommendation_text"]

similarity_config = {
    "stress_level": interval(min, max),
    "sleep_quality": interval(min,max),
   # "social_support": ,
    "physical_activity": ,
    "gad7_estimate": interval(min,max),
    "phq9_estimate": interval(min,max),
    "panic_symptoms":,
    "concentration_difficulty":,
    "main_issue": jaccard_similarity,
    "work_or_study_impairment": interval(min, max),
}

# similaridade global

# PESOS :
# main_issue: 0.25
# gad7_estimate: 0.15
# phq9_estimate: 0.15

# stress_level: 0.1
# sleep_quality: 0.1
# social_support: 0.1

# physical_activity: 0.05
# panic_symptoms: 0.05

# concentration_difficulty: 0.025
# work_or_study_impairment: 0.025