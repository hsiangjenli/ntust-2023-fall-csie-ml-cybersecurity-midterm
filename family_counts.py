import pandas as pd

df = pd.read_csv('motif_reports.csv', encoding='ISO-8859-1')

print(df["Reported family"].value_counts().head(10))