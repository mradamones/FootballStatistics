import pandas as pd


def get_golden_boot(df):
    gb = df.loc[:, ['Player', 'Pos', 'Nation', 'Squad', 'Comp', 'Age', 'Gls']]
    gb['Gls'] = gb['Gls'].astype(int)
    gb = gb.sort_values('Gls', ascending=False).iloc[:15].reset_index(drop=True)
    gb = gb.rename(columns={"Pos": "Position", "Comp": "Competition", "Gls": "Goals"})
    return gb


def get_ga(df):
    ga = df.loc[:, ['Player', 'Pos', 'Nation', 'Squad', 'Comp', 'Age', 'G+A']]
    ga['G+A'] = ga['G+A'].astype(int)
    ga = ga.sort_values('G+A', ascending=False).iloc[:15].reset_index(drop=True)
    ga = ga.rename(columns={"Pos": "Position", "Comp": "Competition", "G+A": "Goals + Assists"})
    return ga


def get_glove(df):
    gg = df.loc[:, ['Player', 'Pos', 'Nation', 'Squad', 'Comp', 'Age', 'CS']]
    gg['CS'] = gg['CS'].astype(int)
    gg = gg.sort_values('CS', ascending=False).iloc[:15].reset_index(drop=True)
    gg = gg.rename(columns={"Pos": "Position", "Comp": "Competition", "CS": "Clean Sheets"})
    return gg


def get_passes(df):
    cmp = df.loc[:, ['Player', 'Pos', 'Nation', 'Squad', 'Comp', 'Age', 'CmpTotal']]
    cmp['CmpTotal'] = cmp['CmpTotal'].astype(int)
    cmp = cmp.sort_values('CmpTotal', ascending=False).iloc[:15].reset_index(drop=True)
    cmp = cmp.rename(columns={"Pos": "Position", "Comp": "Competition", "CmpTotal": "Completed passes"})
    return cmp
