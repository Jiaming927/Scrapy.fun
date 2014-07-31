import plotly
import plotly.plotly as py
from plotly.graph_objs import *

# Fill in with your personal username and API key
# or, use this public demo account
py.sign_in('Python-Demo-Account', 'gwt101uhh0')

data = Data([
    Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[20, 14, 23]
    )
])

plot_url = py.plot(data, filename='basic-bar')