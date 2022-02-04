import pandas as pd
import json
import datetime as dt
import jinja2

# Use the plotly.offline module to use plotly without a cloud account
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly import tools

appfile="json_data.log.gz"
all=pd.read_json(appfile, lines=True)
all['Time']=pd.to_datetime(all.asctime, infer_datetime_format=True)
asks=all[(all['message']=='RealTimeBars') & (all['typ']=='ASK')]
asks=asks[['asctime', 'Time', 'Close', 'ma_slow', 'ma_med', 'ma_fast']]
positions_raw=all[all['message']=='cpos_id msg']
positions=positions_raw[['asctime','Time','qty','act_qty','lastavgFillPrice']]
del all   # save memory
long=positions[(positions['qty']==positions['act_qty']) & (positions['qty']>0)]
short=positions[(positions['qty']==positions['act_qty']) & (positions['qty']<0)]
exits=positions[(positions['qty']==positions['act_qty']) & (positions['qty']==0)]

# Create traces
price = go.Scatter(
    x = asks['Time'],
    y = asks['Close'],
    mode = 'lines',
    name = 'Price',
    opacity = 0.5,
    line = dict(
        width = 1)
)
slow = go.Scatter(
    x = asks['Time'],
    y = asks['ma_slow'],
    mode = 'lines',
    name = 'Slow',
    line = dict(
        width = 1)
)
fast = go.Scatter(
    x = asks['Time'],
    y = asks['ma_fast'],
    mode = 'lines',
    name = 'Fast',
    line = dict(
        width = 1)
)
entr_long = go.Scatter(
    x = long['Time'],
    y = long['lastavgFillPrice'],
    mode = 'markers',
    name = 'Entry',
    marker = dict(
         color = 'green',
          size = 9,
          symbol = 'triangle-up'
        )
)
entr_short = go.Scatter(
    x = short['Time'],
    y = short['lastavgFillPrice'],
    mode = 'markers',
    name = 'Entry',
    marker = dict(
          color = 'red',
          size = 9,
          symbol = 'triangle-down'
        )
)
exit = go.Scatter(
    x = exits['Time'],
    y = exits['lastavgFillPrice'],
    mode = 'markers',
    name = 'Exit',
    opacity = 0.5,
    marker = dict(
          color = 'rgb(0, 0, 0)',
          size = 9,
          symbol = 'square'
        )
)
data=[price,slow,fast,entr_long,entr_short,exit]
fig = go.Figure(data=data)
fig['layout'].update(height=800, width=800 ,plot_bgcolor="rgb(242,242,242,0)")
iplot(fig)

fig.write_html("viz_demo.html",full_html=False,include_plotlyjs='cdn')

with open("viz_demo.html") as file:
    plot_data = file.read().replace("\n", " ")

subs = jinja2.Environment(
              loader=jinja2.FileSystemLoader('./')
              ).get_template('template.html').render(plot=plot_data)
# lets write the substitution to a file
with open('index.html','w') as f:
    f.write(subs)
