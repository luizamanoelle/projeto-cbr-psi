import cbrkit

# carregando a base de casos a partir do arquivo CSV
casebase = cbrkit.loaders.file("cbr_psychology_110_cases_clinical.csv")

#teste 
print("Casos carregados:", len(casebase))

#separação dos problemas e soluções
problems = [  "age", "gender", "anxiety_score", "depression_score",
    "stress_level", "sleep_quality", "sleep_hours",
    "social_support", "physical_activity",
    "symptom_duration_months", "gad7_estimate", "phq9_estimate",
    "panic_symptoms", "concentration_difficulty",
    "irritability_level", "appetite_change",
    "prior_treatment", "current_medication",
    "trauma_history", "substance_use_risk",
    "work_or_study_impairment", "bmi_estimate",
    "comorbid_profile", "clinical_severity",
    "main_issue"]

solutions = ["intervention_type",
    "intensity",
    "weekly_frequency",
    "recommendation_text"]