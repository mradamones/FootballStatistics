from utils import constant
import pandas as pd


def get_all_tables():
    goalkeeping = get_table(constant.goalkeeping, constant.goalkeeping_cols)
    adv_goalkeeping = get_table(constant.adv_goalkeeping, constant.adv_goalkeeping_cols)
    play_time = get_table(constant.play_time, constant.play_time_cols)
    misc = get_table(constant.miscellaneous, constant.miscellaneous_cols)
    standard = get_table(constant.standard_stats, constant.standard_cols)
    passing = get_table(constant.passing, constant.passing_cols)
    pass_types = get_table(constant.pass_types, constant.pass_types_cols)
    defense = get_table(constant.defense, constant.defense_cols)
    possession = get_table(constant.possession, constant.possession_cols)
    shooting = get_table(constant.shooting, constant.shooting_cols)
    creation = get_table(constant.creation, constant.creation_cols)
    return goalkeeping, adv_goalkeeping, play_time, misc, standard, passing, pass_types, defense, possession, shooting, creation


def get_table(html, columns):
    table = pd.read_html(html)
    table = table[0]
    table.columns = table.columns.droplevel()
    table.columns = columns
    table.pop('Matches')
    table = table[table.index % 26 != 25]
    return table


def get_gks(goalkeeping, adv_goalkeeping, misc, play_time):
    # goalkeeping = get_table(constant.goalkeeping, constant.goalkeeping_cols)
    # adv_goalkeepers = get_table(constant.adv_goalkeeping, constant.adv_goalkeeping_cols)
    # play_time = get_table(constant.play_time, constant.play_time_cols)
    # misc = get_table(constant.miscellaneous, constant.miscellaneous_cols)
    misc = misc.drop(columns=['Crs', 'Int', 'TklW'])
    gks = goalkeeping.merge(adv_goalkeeping,
                            on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'GA', 'PKA'],
                            how='left')
    # gks = gks.merge(play_time, on=['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MP', 'Min', '90s', 'Starts'], how='left')
    gks = gks.merge(misc, on=['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    gks = gks.loc[:, ~gks.columns.duplicated()]
    gks.pop('Rk_y')
    gks = gks.rename(columns={'Rk_x': 'Rk'})
    return gks.fillna(0)


def get_def(standard, passing, pass_types, defense, possession, misc, play_time):
    # standard = get_table(constant.standard_stats, constant.standard_cols)
    # passing = get_table(constant.passing, constant.passing_cols)
    # pass_types = get_table(constant.pass_types, constant.pass_types_cols)
    # defense = get_table(constant.defense, constant.defense_cols)
    # possession = get_table(constant.possession, constant.possession_cols)
    # play_time = get_table(constant.play_time, constant.play_time_cols)
    # misc = get_table(constant.miscellaneous, constant.miscellaneous_cols)
    misc = misc.drop(columns=['Crs', 'Int', 'TklW'])
    defs = standard.loc[standard['Pos'].isin(['DF', 'DF,MF', 'DF,FW'])]
    defs = defs.merge(defense, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    defs = defs.merge(passing,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Ast', 'xAG', 'PrgP'],
                      how='left')
    defs = defs.merge(pass_types, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'],
                      how='left')
    defs = defs.merge(possession,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'PrgC', 'PrgR'],
                      how='left')
    # defs = defs.merge(play_time, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left') #check joining
    defs = defs.merge(misc, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'CrdY', 'CrdR'],
                      how='left')
    return defs.fillna(0)


def get_mids(standard, shooting, passing, pass_types, creation, defense, possession, misc, play_time):
    # standard = get_table(constant.standard_stats, constant.standard_cols)
    # shooting = get_table(constant.shooting, constant.shooting_cols)
    # passing = get_table(constant.passing, constant.passing_cols)
    # pass_types = get_table(constant.pass_types, constant.pass_types_cols)
    # creation = get_table(constant.creation, constant.creation_cols)
    # defense = get_table(constant.defense, constant.defense_cols)
    # possession = get_table(constant.possession, constant.possession_cols)
    # play_time = get_table(constant.play_time, constant.play_time_cols)
    # misc = get_table(constant.miscellaneous, constant.miscellaneous_cols)
    misc = misc.drop(columns=['Crs', 'Int', 'TklW'])
    mids = standard.loc[standard['Pos'].isin(['MF', 'MF,DF', 'MF,FW'])]
    mids = mids.merge(passing,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Ast', 'xAG', 'PrgP'],
                      how='left')
    mids = mids.merge(pass_types, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'],
                      how='left')
    mids = mids.merge(shooting, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Gls', 'PK',
                                    'PKattOff', 'xG', 'npxG'], how='left')
    mids = mids.merge(creation, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    mids = mids.merge(defense, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    mids = mids.merge(possession,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'PrgC', 'PrgR'],
                      how='left')
    # mids = mids.merge(play_time, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    mids = mids.merge(misc, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'CrdY', 'CrdR'],
                      how='left')
    return mids.fillna(0)


def get_fwds(standard, shooting, passing, pass_types, creation, possession, misc, play_time):
    # standard = get_table(constant.standard_stats, constant.standard_cols)
    # shooting = get_table(constant.shooting, constant.shooting_cols)
    # passing = get_table(constant.passing, constant.passing_cols)
    # pass_types = get_table(constant.pass_types, constant.pass_types_cols)
    # creation = get_table(constant.creation, constant.creation_cols)
    # possession = get_table(constant.possession, constant.possession_cols)
    # play_time = get_table(constant.play_time, constant.play_time_cols)
    # misc = get_table(constant.miscellaneous, constant.miscellaneous_cols)
    misc = misc.drop(columns=['Crs', 'Int', 'TklW'])
    offs = standard.loc[standard['Pos'].isin(['FW', 'FW,DF', 'FW,MF'])]
    offs = offs.merge(shooting, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Gls', 'PK',
                                    'PKattOff', 'xG', 'npxG'], how='left')
    offs = offs.merge(passing,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'Ast', 'xAG', 'PrgP'],
                      how='left')
    offs = offs.merge(pass_types, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'],
                      how='left')
    offs = offs.merge(creation, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    offs = offs.merge(possession,
                      on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'PrgC', 'PrgR'],
                      how='left')
    # offs = offs.merge(play_time, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s'], how='left')
    offs = offs.merge(misc, on=['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'CrdY', 'CrdR'],
                      how='left')
    return offs.fillna(0)

# TODO - dopisać pobieranie widoków najlepszych strzelców, g+a, czystych kont/obronionych strzałów, podań, wygranych pojedynków główkowych do main menu (po 10 najlepszych
# TODO - klasyfikator
# TODO - PCA dla cech najważniejszych