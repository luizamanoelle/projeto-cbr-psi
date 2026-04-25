import pandas as pd
import utils

mappings = {
    "social_support": {
        "low": 0,
        "medium": 1,
        "high": 2
    },
    "physical_activity": {
        "none": 0,
        "low": 1,
        "moderate": 2,
        "high": 3
    },
    "panic_symptoms": {
        "no": 0,
        "yes": 1
    },
    "concentration_difficulty": {
        "no": 0,
        "yes": 1
    },
    "work_or_study_impairment": {
        "low": 0,
        "moderate": 1,
        "high": 2
    }
}

cb = pd.read_csv("cbr_psychology_110_cases_clinical.csv")


cb = utils.remove_features(cb, ["age", "gender", "anxiety_score", "depression_score", "sleep_hours",
                                "symptom_duration_months", "irritability_level", "appetite_change",
                                "prior_treatment", "current_medication", "trauma_history", "substance_use_risk",
                                "bmi_estimate", "comorbid_profile", "clinical_severity"])

cb = utils.encode_ordinal(cb, mappings)


cb.to_csv("novo_arquivo.csv", index=False)
