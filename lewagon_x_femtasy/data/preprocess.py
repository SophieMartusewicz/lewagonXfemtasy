import pandas as pd
import numpy as np
import os
import datetime
import itertools

def play_percentage(df):
    df['play_percentage'] = df['play_duration'] / df['story_duration']
    return df

def session_id(df):
    df_users_grouped = pd.DataFrame( df.groupby(['user', 'timestamp']).count()['longterm'] ).sort_values(by=['user', 'timestamp'])
    df_users_grouped = df_users_grouped.reset_index(level=1)
    df_users_grouped[0] = np.nan
    df_users_grouped = df_users_grouped.rename(columns={0: 'time_diff_user'})
    df_users_grouped['session_id'] = np.nan
    df_users_grouped = df_users_grouped.drop(labels='longterm', axis=1)
    
    #['time_diff_user'] = users_grouped['timestamp'].diff()
    tmp_list = []
    for user in df_users_grouped.index.unique():
        if type(df_users_grouped.loc[user]['timestamp']) == pd.Timestamp:
            #users_grouped.loc[user]['time_diff_user'] = 0
            tmp_list.append(pd.NaT)
        elif type(df_users_grouped.loc[user]['timestamp']) == pd.Series:
            tmp_list.append(list(df_users_grouped.loc[user]['timestamp'].diff()))
            #users_grouped.loc[user]['timestamp'].diff()
            
    def transform(nested_list):
        regular_list = []
        for ele in nested_list:
            if type(ele) is list:
                regular_list.append(ele)
            else:
                regular_list.append([ele])
        return regular_list

    tmp_list = transform(tmp_list)
    tmp_list = list(itertools.chain(*tmp_list))
    tmp_list
    df_users_grouped['time_diff_user'] = tmp_list
    #type(users_grouped['time_diff_user'].loc['004cfed8fb50838bfa26107fdc9cb3e09dbeb209c991169e40366a0e291ac8f4'][0])
    df_users_grouped = df_users_grouped.reset_index()#['time_diff_user'].isnull()
    #users_grouped['time_diff_user'].fillna(pd.Timedelta(seconds=0))
    df_users_grouped['time_diff_user'] = df_users_grouped['time_diff_user'].fillna(datetime.timedelta(0))
    
    SESSION_LENGTH = datetime.timedelta(minutes=30)

    session_id_counter = 0
    for idx in df_users_grouped.index:
        if (df_users_grouped['user'] != df_users_grouped['user'].shift(1))[idx] or (df_users_grouped['time_diff_user'] > SESSION_LENGTH)[idx]:
            session_id_counter += 1
        df_users_grouped['session_id'].iloc[idx] = session_id_counter
    df_users_grouped = df_users_grouped.astype({'session_id': 'int'})
    df_users_grouped
    
    df = pd.merge(df, df_users_grouped, how='right', on=['user', 'timestamp'])
    return df