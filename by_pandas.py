import pandas as pd
from utils import get_data as gd


def normalize(tab):
    numeric = tab.apply(pd.to_numeric, errors='coerce')
    numeric = numeric.dropna(axis=1)
    numeric = (numeric - numeric.min()) / (numeric.max() - numeric.min())
    return numeric


def find_similar(tab, idx):
    sample = tab.loc[idx]
    print(sample)
    winner = 0
    min_diff = 1
    normalized = normalize(tab)
    for i in range(len(tab)):
        if not tab.iloc[i].equals(tab.iloc[idx]):
            diff = (normalized.loc[idx] - normalized.loc[i]).abs()
            avg_diff = diff.mean()
            if avg_diff < min_diff:
                min_diff = avg_diff
                winner = tab.iloc[i]
    return winner, min_diff


def find_similar_avg(tab, idx):
    sample = tab.loc[idx]
    print(sample)
    winner = 0
    min_diff = 1
    normalized = normalize(tab)
    for i in range(len(tab)):
        if not tab.iloc[i].equals(tab.iloc[idx]):
            diff = abs((normalized.iloc[i].mean() - normalized.iloc[idx].mean()))
            if diff < min_diff:
                min_diff = diff
                winner = tab.iloc[i]
    return winner, min_diff


mids = gd.get_mids()

bellingham1, min_diff_1 = find_similar(mids, 65)
print(bellingham1)
print("Lowest difference: " + str(100 * min_diff_1) + "%")

bellingham2, min_diff_2 = find_similar_avg(mids, 65)
print(bellingham2)
print("Lowest difference: " + str(100 * min_diff_2) + "%")
# TODO - stworzyć kilka jakościowych statystyk, np (CrdY+3*CrdR)/Min
