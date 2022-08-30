import os
import pandas as pd

def read_data():
    '''path = os.path.join(
        os.environ.get('LOCAL_DATA_PATH'), 'raw_data.xlsx'
    )'''
    path = os.path.join(os.path.dirname(__file__)[:-4], 'raw_data', 'raw_data.xlsx')
    df = pd.read_excel(path)
    return df

#print(os.path.getcwd(__file__))
#print(os.path.dirname(__file__))
#pwd or cwd

print(read_data())
