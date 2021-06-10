import os 
project_root = f'{os.path.dirname(os.path.abspath(__file__))}/..'
import numpy as np 
import pandas as pd 
import time
import json
import pickle 
from datetime import datetime, timezone, timedelta
date = datetime.now(timezone(timedelta(hours=+9), 'JST')).strftime('%Y-%m-%d %H:%M:%S')
# mecab_dic = '/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
import requests

import sys
sys.path.append(f'{project_root}/lib')
from text_processor import TextProcessor as TP
import csv
from db_accessor import clsDbAccessor

try:
    config = json.load(open(f'{project_root}/src/config.json'))
except Exception as e:
    print('failed: load config')
    raise e


slack_url = ''

import logging
logging.basicConfig(filename=f'{project_root}/log/important_{date}.log', level=logging.ERROR)

local_df_path = f'{project_root}/data/local_df.pickle'

def load_local_df():
    try:
        with open(local_df_path, 'rb') as f:
            local_df = pickle.load(f)#.set_index('tw_id', drop=False)
        return local_df
    except Exception as e:
        print('failed: load local_df')
        raise e 

def update_tbl_twitter(df, columns):
    dba = clsDbAccessor()
    for i in df.index:
        row = df.loc[i]
        tw_id = row['tw_id']
        sql = f"UPDATE tbl_twitters SET " + ', '.join([f"{col}='{row[col]}'" for col in columns if row[col] is not np.nan]) + f" WHERE tw_id={tw_id};"
        try:
            dba.execNonQuery(sql)
        except:
            continue
    print("コミット")
    dba.commit()
    dba.close()


