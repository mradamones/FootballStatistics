# URLs
standard_stats = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'
goalkeeping = 'https://fbref.com/en/comps/Big5/keepers/players/Big-5-European-Leagues-Stats'
adv_goalkeeping = 'https://fbref.com/en/comps/Big5/keepersadv/players/Big-5-European-Leagues-Stats'
shooting = 'https://fbref.com/en/comps/Big5/shooting/players/Big-5-European-Leagues-Stats'
passing = 'https://fbref.com/en/comps/Big5/passing/players/Big-5-European-Leagues-Stats'
pass_types = 'https://fbref.com/en/comps/Big5/passing_types/players/Big-5-European-Leagues-Stats'
creation = 'https://fbref.com/en/comps/Big5/gca/players/Big-5-European-Leagues-Stats'
defense = 'https://fbref.com/en/comps/Big5/defense/players/Big-5-European-Leagues-Stats'
possession = 'https://fbref.com/en/comps/Big5/possession/players/Big-5-European-Leagues-Stats'
play_time = 'https://fbref.com/en/comps/Big5/playingtime/players/Big-5-European-Leagues-Stats'
miscellaneous = 'https://fbref.com/en/comps/Big5/misc/players/Big-5-European-Leagues-Stats'

# Cols
standard_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MP', 'Starts', 'Min', '90s', 'Gls',
                 'Ast', 'G+A', 'G-PK', 'PK', 'PKattOff', 'CrdY', 'CrdR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC',
                 'PrgP', 'PrgR', 'Gls/90', 'Ast/90', 'G+A/90', 'G-PK/90', 'G+A-PK/90', 'xG/90', 'xAG/90', 'xG+xAG/90',
                 'npxG/90', 'npxG+xAG/90', 'Matches']
goalkeeping_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MP', 'Starts', 'Min', '90s', 'GA',
                    'GA90', 'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%', 'PKatt', 'PKA', 'PKsv', 'PKm',
                    'Save%', 'Matches']
adv_goalkeeping_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                        'GA', 'PKA', 'FKGoals', 'CKAgainst', 'OGgk', 'PSxG', 'PSxG/SoT', 'PSxG+/-', '/90',
                        'Cmp', 'AttLaunched', 'Cmp%', 'AttPasses', 'Thr', 'Launch%Passes', 'AvgLenPasses', 'AttKicks',
                        'Launch%Kicks', 'AvgLenKicks', 'Opp', 'Stp', 'Stp%', '#OPA', '#OPA/90', 'AvgDist', 'Matches']
shooting_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                 'Gls', 'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist',
                 'FKShot', 'PK', 'PKattOff', 'xG', 'npxG', 'npxG/Sh', 'G-xG', 'np:G-xG', 'Matches']
passing_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                'CmpTotal', 'AttTotal', 'Cmp%Total', 'TotDistPass', 'PrgDistPassed', 'CmpShort', 'AttShort', 'Cmp%Short',
                'CmpMedium', 'AttMedium', 'Cmp%Medium', 'CmpLong', 'AttLong', 'Cmp%Long', 'Ast', 'xAG', 'xA',
                'A-xAG', 'KP', '1/3Passes', 'PPA', 'CrsPA', 'PrgP', 'Matches']
pass_types_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s', 'AttPasses', 'LivePasses', 'Dead',
                   'FKPass', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'In', 'Out', 'Str', 'Cmp', 'Off', 'Blocked', 'Matches']
creation_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                 'SCA', 'SCA90', 'PassLiveSCA', 'PassDeadSCA', 'TOSCA', 'ShSCA', 'FldSCA', 'DefSCA', 'GCA',
                 'GCA90', 'PassLiveGCA', 'PassDeadGCA', 'TOGca', 'ShGCA', 'FldGCA', 'DefGCA', 'Matches']
defense_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                'TklTackles', 'TklW', 'Def 3rdTackles', 'Mid 3rdTackles', 'Att 3rdTackles', 'TklChallenges', 'AttDribblesAgainst', 'Tkl%',
                'LostChall', 'Blocks', 'ShBlocked', 'Pass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Matches']
possession_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                   'Touches', 'Def Pen', 'Def 3rdTouches', 'Mid 3rdTouches', 'Att 3rdTouches', 'Att Pen',
                   'LiveTouches', 'AttTakeOns', 'Succ', 'Succ%', 'Tkld', 'Tkld%', 'Carries', 'TotDistCarries',
                   'PrgDistCarried', 'PrgC', '1/3Carries', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR', 'Matches']
play_time_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', 'MPTotal',
                  'MinTotal', 'Mn/MP', 'Min%', '90s', 'StartsAll', 'Mn/Start', 'Compl', 'Subs',
                  'Mn/Sub', 'unSub', 'PPM', 'onG', 'onGA', '+/-', '+/-90', 'On-Off',
                  'onxG', 'onxGA', 'xG+/-', 'xG+/-90', 'On-OffxG', 'Matches']
miscellaneous_cols = ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born', '90s',
                      'CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Offside', 'Crs', 'Int', 'TklW',
                      'PKwon', 'PKcon', 'OG', 'Recov', 'WonAerial', 'LostAerial', 'Won%Aerial', 'Matches']
