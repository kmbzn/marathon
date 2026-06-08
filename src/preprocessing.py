import pandas as pd
import numpy as np


def time_to_seconds(time_str):
    if pd.isna(time_str) or str(time_str).strip() in ['-', '', 'nan']:
        return None
    parts = str(time_str).strip().split(':')
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return None


def load_and_clean(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, index_col=0)

    split_cols = ['5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K', '40K', 'Official Time']
    for col in split_cols:
        df[col + '_s'] = df[col].apply(time_to_seconds)

    df = df.dropna(subset=['Official Time_s', '5K_s', '10K_s', '30K_s', '40K_s'])
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['Fatigue_Index'] = ((df['40K_s'] - df['30K_s']) / 10) / (df['10K_s'] / 10)

    seg_paces = pd.DataFrame({
        '0-5K':   df['5K_s'] / 5,
        '5-10K':  (df['10K_s'] - df['5K_s']) / 5,
        '10-15K': (df['15K_s'] - df['10K_s']) / 5,
        '15-20K': (df['20K_s'] - df['15K_s']) / 5,
        '20-25K': (df['25K_s'] - df['20K_s']) / 5,
        '25-30K': (df['30K_s'] - df['25K_s']) / 5,
        '30-35K': (df['35K_s'] - df['30K_s']) / 5,
        '35-40K': (df['40K_s'] - df['35K_s']) / 5,
    })
    df['Pacing_Variance'] = seg_paces.std(axis=1)

    df['Gender_bin'] = (df['M/F'] == 'M').astype(int)

    df['AgeGroup'] = pd.cut(df['Age'], bins=[17, 29, 39, 49, 59, 82],
                            labels=['18-29', '30-39', '40-49', '50-59', '60+'])
    return df


FEATURE_COLS = [
    'Age', 'Gender_bin', 'Fatigue_Index', 'Pacing_Variance',
    '5K_s', '10K_s', '15K_s', '20K_s', 'Half_s', '25K_s', '30K_s',
]
TARGET_COL = 'Official Time_s'
