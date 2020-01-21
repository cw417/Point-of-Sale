from datetime import datetime
import pandas as pd
import json
import os

csv_fp = 'sales.csv'
excel_fp = 'sales.xlsx'
json_fp = "sales.json"

def get_dict(json_fp):
    with open(json_fp) as json_data:
        dict = json.load(json_data)
        json_data.close()
        return dict

def write_json(dict, json_fp):
    json.dump(dict, open(json_fp, 'a'), indent=4, sort_keys=True)

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
    excel = df.to_excel(excel_filepath, header=True)

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

""" def get_write_excel(excel_fp, new_df):
    df = concat_from_excel(excel_fp, new_df)
    excel =  """


def sales_df(total, pay_type):
    data = [[total, pay_type, datetime.today()]]
    df = pd.DataFrame(data)
    return df


##
##
##


def sale_to_ledger(sale, json_fp):
    json.dump(sale, open(json_fp, 'a'), indent=4, sort_keys=True)




def check_nums(nums):
    # Checks to see if items in list are digits, and returns list of items that are
    num_list = []
    for num in nums:
        if isinstance(num, int) == True or isinstance(num, float):
            num = float(num)
            num_list.append(num)
    return num_list

def add_total(total_list):
    # Adds up items in a list, and returns the total
    total = 0
    for num in total_list:
        total += num
    return total

def make_sale(item, price):
    sale = {item: price}
    return sale

def add_to_sale(sale, item, price):
    sale[item] = price
    return sale


# Flow of defs: two fields-->submit_button-->calls make_sale()--> if sale exists, add_to_sale()
# Total button: button --> look in sale dict --> get k,v --> grab 'price' keys --> add values to list


def check_nums(nums):
    # Checks to see if items in list are digits, and returns list of items that are
    num_list = []
    for num in nums:
        try:
            num = float(num)
            num_list.append(num)
        except ValueError:
            continue
    return num_list

            


