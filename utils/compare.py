import pandas as pd
from utils import get_data as gd


def normalize(tab):
    numeric = tab.apply(pd.to_numeric, errors='coerce')
    numeric = numeric.dropna(axis=1)
    numeric = (numeric - numeric.min()) / (numeric.max() - numeric.min())
    return numeric


def similar_manhattan(tab, idx):
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


def similar_euclidean(tab, idx):
    sample = tab.loc[idx]
    print(sample)
    winner = 0
    min_diff = 1
    normalized = normalize(tab)
    for i in range(len(tab)):
        if not tab.iloc[i].equals(tab.iloc[idx]):
            diff = pow((normalized.loc[idx] - normalized.loc[i]), 2)
            avg_diff = diff.mean()
            if avg_diff < min_diff:
                min_diff = avg_diff
                winner = tab.iloc[i]
    return winner, min_diff


def similar_pearson(tab, idx):
    sample = tab.loc[idx]
    print(sample)
    winner = 0
    max_pearson = 0
    normalized = normalize(tab)
    for i in range(len(tab)):
        if i != idx:
            # pearson = pow((normalized.loc[idx] - normalized.loc[i]), 2)
            avg_sample = normalized.loc[idx].mean()
            avg_current = normalized.loc[i].mean()
            pearson = ((normalized.loc[idx] - avg_sample) * (normalized.loc[i] - avg_current)).sum() / (
                        len(normalized.columns) - 1)
            abs_pearson = abs(pearson)
            if abs_pearson > max_pearson:
                max_pearson = abs_pearson
                winner = tab.iloc[i]
    return winner, max_pearson

# TODO - create cosinus similarity
def similar_avg(tab, idx):
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


# mids = gd.get_mids()
#
# bellingham1, min_diff_1 = similar_manhattan(mids, 68)
# print(bellingham1)
# print("Lowest manhattan difference: " + str(100 * min_diff_1) + "%")
#
# bellingham2, min_diff_2 = similar_avg(mids, 68)
# print(bellingham2)
# print("Lowest average difference: " + str(100 * min_diff_2) + "%")
#
# bellingham3, min_diff_3 = similar_euclidean(mids, 68)
# print(bellingham3)
# print("Lowest euclidean difference: " + str(100 * min_diff_3) + "%")
#
# bellingham4, min_diff_4 = similar_pearson(mids, 68)
# print(bellingham4)
# print("Highest pearson correlance: " + str(100 * min_diff_4) + "%")
# TODO - stworzyć kilka jakościowych statystyk, np (CrdY+3*CrdR)/Min