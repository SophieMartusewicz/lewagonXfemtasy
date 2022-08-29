import os
import pandas as pd

def read_data():
    '''path = os.path.join(
        os.environ.get('LOCAL_DATA_PATH'), 'raw_data.xlsx'
    )'''
    path = os.path.join('..', 'raw_data', 'raw_data.xlsx')
    df = pd.read_excel(path)
    return df

print(read_data())
