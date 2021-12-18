import pandas as pd
import plotly.figure_factory as ff
import csv
df=pd.read_csv("proData.csv")
graph=ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating"])
graph.show()