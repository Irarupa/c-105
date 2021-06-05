import pandas as pd
import plotly.express as px
import statistics 

df_graph = pd.read_csv('data.csv')

mean = statistics.mean(df_graph[''].tolist())
