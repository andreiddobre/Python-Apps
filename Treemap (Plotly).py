#pip install plotly
import plotly.graph_objects as treePlot

fig = treePlot.Figure(treePlot.Treemap(
    labels = ["A","B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
    ))

fig.show()

#original code inspired by clcoding.com
