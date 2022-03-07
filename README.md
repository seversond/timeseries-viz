# Introduction

I was confronted with a relatively complex set of timeseries data and events.
They were intertwined. I needed to do some diagnostics on the incoming data and the events. This
visualization with Plotly provided tooltips and finegrained zoom that made it easy to create
a highly sophisticated diagnostic visualization tool.  The index.html
file here can be downloaded and viewed local or served from any webserver as a standalone
file.  Viewing these
artifacts directly from github.com at the moment is not possible.

The other example of note here is the use of highly flexible json logging data.
This code demonstrates the use of code to mine this complex structure and produce
meaning full data. A example of some of these json artifacts are below.

# More Detail

The python code reads the json_data.log.gz file.  It pulls out a key set of records
to produce the required data for the plot.  One the plot is produced it is added
to the template.html file and written as index.html.  The index.html file can stand alone.
It does use bootstap and plotly cdn references, which save on download time
and will speed rendering.  But can become obsolete.

# Highly Flexible Data Storage

```
{"asctime": "2019-04-22 01:52:44,441", "levelname": "INFO", "name": "root", "funcName": "setup_logging", "message": "start of log"}
{"asctime": "2019-04-22 01:52:44,442", "levelname": "DEBUG", "name": "root", "funcName": "main", "message": "config", "environ": "paper", "stratName": "fx9.aud", "stratType": "fx9", "stratDescription": "AUD USD momentum - triple ma", "bars_port": "5564", "barsrq_port": "5565", "order_recv_port": "5570", "order_resp_port": "5569", "secID": "AUD.USD", "orderQty": 25000, "comment": "fparm,mparm,sparm,stopp,tstop,sdwin,sdfilter,sdrange", "maFast": 400, "maMed": 8000, "maSlow": 8000, "stop_delta": 0.002, "tstop_offset": 0.002, "sdWin": 1000, "sdFilter": 1e-09, "sdWin_slow": 7000, "tstoplmt": 0.001, "pricelmt": 0.001, "magicnum": 14109}
{"asctime": "2019-04-22 01:52:44,443", "levelname": "INFO", "name": "root", "funcName": "setup_mq", "message": "mq setup"}
{"asctime": "2019-04-22 01:52:44,443", "levelname": "INFO", "name": "root", "funcName": "main", "message": "connect starting now"}
{"asctime": "2019-04-22 01:52:44,443", "levelname": "INFO", "name": "root", "funcName": "__init__", "message": "bars rcv socket setup"}
{"asctime": "2019-04-22 01:52:44,444", "levelname": "INFO", "name": "root", "funcName": "__init__", "message": "order rcv socket setup"}
{"asctime": "2019-04-22 01:52:44,453", "levelname": "INFO", "name": "root", "funcName": "__init__", "message": "wd timer setup"}
{"asctime": "2019-04-22 13:18:24,660", "levelname": "DEBUG", "name": "root", "funcName": "run", "message": "order response", "dat": "{\"orderId\": \"0\", \"tstop_orderId\": \"0\", \"notify\": false, \"term_ord_cnt\": 3, \"client\": \"fx9.aud\", \"secID\": \"AUD.USD\", \"qty\": 0, \"pricelmt\": 0.001, \"price\": 0.71348, \"tstop_offset\": 0.002, \"tstoplmt\": 0.001, \"act_qty\": 0, \"lastavgFillPrice\": 0.71348, \"cpos_id\": \"fx9.aud:1555938991\"}"}
{"asctime": "2019-04-22 13:18:24,661", "levelname": "INFO", "name": "root", "funcName": "order_rsp", "message": "cpos_id msg", "orderId": "0", "tstop_orderId": "0", "notify": false, "term_ord_cnt": 3, "client": "fx9.aud", "secID": "AUD.USD", "qty": 0, "pricelmt": 0.001, "price": 0.71348, "tstop_offset": 0.002, "tstoplmt": 0.001, "act_qty": 0, "lastavgFillPrice": 0.71348, "cpos_id": "fx9.aud:1555938991"}
{"asctime": "2019-04-22 13:18:24,661", "levelname": "INFO", "name": "root", "funcName": "order_rsp", "message": "out of position"}
```
