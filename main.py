appfile="../t4.log.gz"

import pandas as pd
import json
import datetime as dt

# Use the plotly.offline module to use plotly without a cloud account
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly import tools
init_notebook_mode()

all=pd.read_json(appfile, lines=True)
all['Time']=all['asctime'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S,%f").timestamp())

asks=all[(all['message']=='RealTimeBars') & (all['typ']=='ASK')]

asks=asks[['asctime', 'Time', 'Close', 'ma_slow', 'ma_med', 'ma_fast']]

positions_raw=all[all['message']=='cpos_id msg']

positions=positions_raw[['asctime','Time','qty','act_qty','lastavgFillPrice']]

#['ascti{"asctime": "2019-04-19 15:15:54,527", "levelname": "INFO", "name": "root",
 #"funcName": "order_rsp", "message": "cpos_id msg", "orderId": "0", "tstop_orderId": "0",
 #"notify": false, "term_ord_cnt": 1, "client": "fx9.aud", "secID": "AUD.USD", "qty": -25000,
 #"pricelmt": 0.001, "price": 0.71507, "tstop_offset": 0.002, "tstoplmt": 0.001, "act_qty": -25000,
 #"lastavgFillPrice": 0.71485, "cpos_id": "fx9.aud:1555686951"}
#          me','Time',]]


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
fig['layout'].update(height=1000, width=1000, title='Viz Demo',plot_bgcolor="rgb(242,242,242,0)")
iplot(fig)

fig.write_html("viz_demo.html")
