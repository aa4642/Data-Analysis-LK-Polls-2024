import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv('results_2024.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="LS_polls.html")

profile1 = ProfileReport(df, minimal=True)
profile1.to_file(output_file="LS_polls1.html")
