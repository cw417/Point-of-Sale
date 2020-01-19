from datetime import datetime
import pandas as pd
import json
import os

csv_fp = 'sales.csv'
excel_fp = 'sales.xlsx'


def get_dict(json_fp):
    with open(json_fp) as json_data:
        dict = json.load(json_data)
        json_data.close()
        return dict

def make_csv(total, pay_type, csv_filepath):
    data_layout = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data_layout, columns = ['Total', 'Pay Type', 'Date'])
    csv = df.to_csv(csv_filepath, mode='a', header=True)

def append_csv(total, pay_type, csv_filepath):
    data_layout = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data_layout)
    csv = df.to_csv(csv_filepath, mode='a', header=False)

def check_csv(total, pay_type, csv_filepath):
    if not os.path.isfile(csv_filepath):
        make_csv(total, pay_type, csv_filepath)
    else:
        append_csv(total, pay_type, csv_filepath)

def make_excel(total, pay_type, excel_filepath):
    data_layout = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data_layout, columns = ['Total', 'Pay Type', 'Date'])
    append_csv = df.to_excel(excel_filepath, header=True)

def concat_from_excel(excel_fp, new_df):
    data = pd.read_excel(excel_fp)
    df = pd.DataFrame(data)
    frames = [df, new_df]
    comb = pd.concat(frames, sort=True)
    return comb

def concat_from_csv(excel_fp, new_df):
    data = pd.read_csv(csv_fp)
    df = pd.DataFrame(data)
    frames = [df, new_df]
    comb = pd.concat(frames, sort=True)
    return comb

def concat_from_file(fp, new_df):
    """Concatenates existing dataframe
    in .csv or .xlsx with new_df."""
    if fp.lower().endswith('csv'):
        output_df = concat_from_csv(fp, new_df)
        return output_df
    elif fp.lower().endswith('xlsx'):
        output_df = concat_from_excel(fp, new_df)
        return output_df
    else:
        print("File type not available. \nPlease use .csv or .xlsx")