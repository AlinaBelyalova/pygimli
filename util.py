import numpy as np
import pandas as pd
import os
import glob


def st2sgt(stpath, sgtpath):
    
    # Имя файла без пути и расширени
    base_name = os.path.basename(stpath).split('.')[0]
    
    # Чтение файла .st
    df = pd.read_csv(stpath, sep=r'\t|\s+', engine='python')
    
    # Обработка данных
    df_s = df[['tx', 'tz']].drop_duplicates().sort_values(by='tx')
    df_g = df[['rx', 'rz']].drop_duplicates().sort_values(by='rz').rename(columns={'rx':'tx', 'rz':'tz'})
    df_sg = pd.concat((df_s, df_g), ignore_index=True).drop_duplicates().sort_values(by='tx').reset_index(drop=True)
    df_sg['s'] = df_sg.index + 1
    df_sg['g'] = df_sg.index + 1
    df = df.merge(df_sg[['tx', 'tz', 's']], on=['tx', 'tz'])
    df = df.merge(df_sg[['tx', 'tz', 'g']].rename(columns={'tx': 'rx', 'tz': 'rz'}), on=['rx', 'rz'])
    df["ft"] /= 1000
    df1 = df_sg[['tx', 'tz']].rename(columns={'tx': 'x', 'tz': 'y'})
    df2 = df[["s", "g", "ft"]].rename(columns={"ft": "t"})
    df2['t'] = df2['t'].replace(0.0, 0.00000123)
    str1 = f"{len(df1)} # shot/geophone points"
    str2 = f"{len(df2)} # measurements"


    # Запись в файл
    with open(sgtpath, 'w+') as f:
        f.write(str1)
        f.write("\n#")
        df1.to_csv(f, sep='\t', index=False, lineterminator='\n')
        f.write(str2)
        f.write("\n#")
        df2.to_csv(f, sep='\t', index=False, lineterminator='\n')
