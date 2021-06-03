import plotly.figure_factory as ff
import pandas as p

df = p.read_csv('.\projectData.csv')

figure = ff.create_distplot([df["AvgRating"].to_list()],["Result"],show_hist=False)
figure.show()

