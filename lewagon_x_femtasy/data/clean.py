import pandas as pd

def clean_data(df):

    # Rename unnamed column to 'fantasies'
    df = df.rename(columns={'Unnamed: 11': 'fantasies'})

    # Drop Row-duplicates
    df = df.drop_duplicates()

    # Split 'Session Breakups' into single parts
    df['Session Breakups_date'] = df['Session Breakups'].str[:9]
    df['Session Breakups_breakup'] = df['Session Breakups'].str.slice(start=10)

    df = split_score(df)

    df = voice_popularity(df)

    return df


def split_score(df):
    def user_kinks(value):
        if value >100:
            return str(value)[1:]
        else:
            return 0
    df['user_intensity'] = pd.to_numeric(df['Kinkiness Score'].apply(lambda x: str(x)[0]))
    df['user_kinks'] = pd.to_numeric(df['Kinkiness Score'].apply(lambda x: user_kinks(x)))

    return df


def voice_popularity(df):
    df['voice_popularity'] = df['Anonymized Voice IDs'].apply(lambda x: df['Anonymized Voice IDs'].value_counts()[x])
    return df
