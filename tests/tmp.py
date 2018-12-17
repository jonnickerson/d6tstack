import importlib
import d6tstack.utils
importlib.reload(d6tstack.utils)

import time
import yaml

config = yaml.load(open('tests/.test-cred.yaml'))

cfg_uri_psql = config['rds']
cfg_uri_psql = config['wlo']

import pandas as pd
import sqlalchemy

sqlengine = sqlalchemy.create_engine(cfg_uri_psql)
print(pd.read_sql_table('benchmark',sqlengine).head())

dft = pd.read_sql_table('benchmark',sqlengine)
dft.shape

# cursor = sqlengine.cursor()
sql = sqlengine.execute("SELECT * FROM benchmark;")
dft2 = pd.DataFrame(sql.fetchall())
dft2.shape
sql.keys()

importlib.reload(d6tstack.utils)

start_time = time.time()
dft2 = d6tstack.utils.pd_from_sqlengine(cfg_uri_psql, "SELECT * FROM benchmark;")
assert dft2.shape==(100000, 23)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
dft = pd.read_sql_table('benchmark',sqlengine)
assert dft.shape==(100000, 23)
print("--- %s seconds ---" % (time.time() - start_time))

d6tstack.utils.test()

