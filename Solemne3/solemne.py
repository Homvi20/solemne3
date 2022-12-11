import pandas as pd

def load():
    df = pd.read_csv("Solemne03.csv" , index_col= "Unnamed: 0")
    return df


def clean(df):
    df_fil = df.drop( df.index[df.Nombres == "FALSE"], axis = 0)
    df_fil1 = df_fil.drop( df_fil.index[df_fil.Nombres == "TRUE"], axis = 0)
    df_fil2 = df_fil1.drop( df_fil1.index[df_fil1.Nombres == "NaN"], axis = 0)
    df_fil3 = df_fil2.drop( df_fil2.index[df_fil2.Nombres == "NULL"], axis = 0)    
    df_fil4 = df_fil3.drop( df_fil3.index[df_fil3.Edad >=120,], axis = 0)
    df_fil5 = df_fil4.drop( df_fil4.index[df_fil4.Edad <=0,], axis = 0)
    return df_fil5


def deleterep(df):
    #df1 = df[df.deleterep(subset=["Nombres"],keep=False)].sort_values(by = ["Nombres", "Sueldo"])
    #df1 = df.duplicated(subset=["Nombres"])
    df0 = df["Nombres"]
    df1 = df0.head(1)
    df2 = df[df["Nombres"] == df1]
    return df2
    


def main():
    df = load()
    df_clean = clean(df)
    df_clean_rep = deleterep(df_clean)
    print(df_clean_rep)

main()