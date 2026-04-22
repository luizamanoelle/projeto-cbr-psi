import cbrkit

# carregando a base de casos a partir do arquivo CSV
casebase = cbrkit.loaders.file("cbr_psychology_110_cases_clinical.csv")

print("Casos carregados:", len(casebase))
