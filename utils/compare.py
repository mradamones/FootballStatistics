from math import sqrt

import numpy as np
import pandas as pd


def normalize(tab):
    numeric = tab.apply(pd.to_numeric, errors='coerce')
    numeric = numeric.dropna(axis=1)
    numeric = (numeric - numeric.min()) / (numeric.max() - numeric.min())
    numeric = numeric.fillna(0)
    return numeric


def similar_manhattan(tab, idx):
    winner = 0
    min_diff = float('inf')
    normalized = normalize(tab)
    for i in range(len(normalized)):
        if i != idx:
            sample = normalized.iloc[idx]
            other = normalized.iloc[i]
            diff = (sample - other).abs()
            avg_diff = diff.mean()
            if avg_diff < min_diff:
                min_diff = avg_diff
                winner = tab.iloc[i]
    return winner, min_diff


def similar_euclidean(tab, idx):
    winner = 0
    min_diff = 1
    normalized = normalize(tab)
    for i in range(len(tab)):
        if i != idx:
            diff = np.power(normalized.iloc[idx] - normalized.iloc[i], 2)
            sum_diff = diff.sum()
            avg_diff = np.sqrt(sum_diff) / len(diff)
            if avg_diff < min_diff:
                min_diff = avg_diff
                winner = tab.iloc[i]
    return winner, min_diff


def similar_pearson(tab, idx):
    winner = 0
    max_pearson = 0
    normalized = normalize(tab)
    for i in range(len(tab)):
        if i != idx:
            avg_sample = normalized.iloc[idx].mean()
            avg_current = normalized.iloc[i].mean()
            pearson = ((normalized.iloc[idx] - avg_sample) * (normalized.iloc[i] - avg_current)).sum() / (np.std(normalized.iloc[idx]) * np.std(normalized.iloc[i]))
            if pearson > max_pearson:
                max_pearson = pearson
                winner = tab.iloc[i]
    return winner, max_pearson


def similar_avg(tab, idx):
    winner = 0
    min_diff = float('inf')
    normalized = normalize(tab)
    for i in range(len(tab)):
        if i != idx:
            diff = abs((normalized.iloc[i].mean() - normalized.iloc[idx].mean()))
            if diff < min_diff:
                min_diff = diff
                winner = tab.iloc[i]
    return winner, min_diff


def similar_cosine(tab, idx):
    winner = 0
    min_diff = -1
    normalized = normalize(tab)
    for i in range(len(tab)):
        if i != idx:
            sam = normalized.iloc[idx]
            comp = normalized.iloc[i]
            dot_product = np.dot(sam, comp)
            norm1 = np.linalg.norm(sam)
            norm2 = np.linalg.norm(comp)
            diff = dot_product / (norm1 * norm2)
            if diff > min_diff:
                min_diff = diff
                winner = tab.iloc[i]
    return winner, min_diff


# goalkeeping, adv_goalkeeping, play_time, misc, standard, passing, pass_types, defense, possession, shooting, creation = gd.get_all_tables()
# mids = gd.get_mids(standard, shooting, passing, pass_types, creation, defense, possession, misc, play_time)
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
# print("Lowest Euclidean difference: " + str(100 * min_diff_3) + "%")
#
# bellingham4, min_diff_4 = similar_pearson(mids, 68)
# print(bellingham4)
# print("Highest pearson correlance: " + str(100 * min_diff_4) + "%")

# bellingham5, min_diff_5 = similar_cosine(mids, 68)
# print(bellingham5)
# print("Highest cosine similarity: " + str(100*((min_diff_5 + 1)/2)) + "%")
