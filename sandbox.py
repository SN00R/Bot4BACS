import pandas as pd
import numpy as np


df_truth = pd.read_csv("/Users/noor/Bot4BACS/Testo_Cal/2023-09-07-16-48-42.csv")

df_truth = df_truth.dropna()

print(df_truth)