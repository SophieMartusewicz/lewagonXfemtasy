import os
import pandas as pd

def read_data():
    '''path = os.path.join(
        os.environ.get('LOCAL_DATA_PATH'), 'raw_data.xlsx'
    )'''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'raw_data', 'raw_data.xlsx')
    #print(os.__file__)
    print(path)

    #path = '/Users/pat3/code/SophieMartusewicz/lewagonXfemtasy/raw_data/raw_data.xlsx'
    #path = '../../raw_data/raw_data.xlsx'
    #print(path)
    df = pd.read_excel(path)
    return df

#print(read_data())
