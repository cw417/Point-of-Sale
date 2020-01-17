from datetime import datetime
import pandas as pd
import json
import os

csv_fp = 'sales.csv'

def make_pandas(total, pay_type, csv_filepath):
    data_layout = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data_layout, columns = ['Total', 'Pay Type', 'Date'])
    make_csv = df.to_csv(csv_filepath, mode='a', header=True)

def append_pandas(total, pay_type, csv_filepath):
    data_layout = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data_layout)
    append_csv = df.to_csv(csv_filepath, mode='a', header=False)

def pd_check(total, pay_type, csv_filepath):
    if not os.path.isfile(csv_filepath):
        make_pandas(total, pay_type, csv_filepath)
    else:
        append_pandas(total, pay_type, csv_filepath)

def get_dict(json_fp):
    with open(json_fp) as json_data:
        dict = json.load(json_data)
        json_data.close()
        return dict

    