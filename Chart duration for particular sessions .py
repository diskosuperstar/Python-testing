import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import dcc
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import cx_Oracle
dsn = cx_Oracle.makedsn('database name', 'port', service_name='service_name')
orcl = cx_Oracle.connect(user='INSERT USER', password='INSERT PASSWORD', dsn=dsn)

alegro = """SELECT
    sess_name,
    trunc(sess_end) date1,
    sess_dur / 3600 as duration,
    nb_row,
    nb_ins,
    nb_upd,
    nb_del
FROM
    snp_session
WHERE
        sess_name = 'CUSTOM_SILOS_PKG_TABLE_WATCHER_SCHEMA_SWAP' --remove this for all sessions
    AND context_code = 'GLOBAL' -- change depending on the context
ORDER BY
    sess_end DESC"""

dr1 = pd.read_sql(alegro,orcl)
fig = px.line(dr1, x='DATE1', y='DURATION')
fig.show()
