import pandas as pd
import numpy as np
import os
import datetime

def play_percentage(df):
    df['play_percentage'] = df['play_duration'] / df['story_duration']
    return df