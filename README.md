# projeto-cbr-psi
Criação de um CBR em Python utilizando a biblioteca CBRkit.

O trabalho consiste no desenvolvimento de um sistema de Raciocínio Baseado em Casos. A base de casos utilizada refere-se a problemas relacionados à psicologia, sendo as features do problema:



| Tipo       | Feature                  | Medida de similaridade                          |
| ---------- | ------------------------ | ----------------------------------------------- |
| Numérica   | age                      | -                                               |
| Categórica | gender                   | -                                               |
| Numérica   | anxiety_score            | -                                               |
| Numérica   | depression_score         | -                                               |
| Numérica   | stress_level             | distância                                       |
| Numérica   | sleep_quality            | distância                                       |
| Numérica   | sleep_hours              | -                                               |
| Categórica | social_support           | codificação ordinal                             |
| Categórica | physical_activity        | codificação ordinal                             |
| Numérica   | symptom_duration_months  | -                                               |
| Numérica   | gad7_estimate            | distância                                       |
| Numérica   | phq9_estimate            | distância                                       |
| Categórica | panic_symptoms           | codificação ordinal                             |
| Categórica | concentration_difficulty | codificação binária                             |
| Numérica   | irritability_level       | -                                               |
| Categórica | appetite_change          | -                                               |
| Categórica | prior_treatment          | -                                               |
| Categórica | current_medication       | -                                               |
| Categórica | trauma_history           | -                                               |
| Categórica | substance_use_risk       | -                                               |
| Numérica   | work_or_study_impairment | distância                                       |
| Numérica   | bmi_estimate             | -                                               |
| Categórica | comorbid_profile         | -                                               |
| Categórica | clinical_severity        | -                                               |
| String     | main_issue               | Coeficiente de similaridade (Índice de Jaccard) |
