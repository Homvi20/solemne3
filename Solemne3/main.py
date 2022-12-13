import pandas as pd
from docente import Docente
from estudiante import Estudiante

def inicio():
    datos=pd.read_csv("Solemne03.csv", index_col= "Unnamed: 0")
    return datos


def filtrado(datos):   
    datos.dropna(how="any",inplace=True)
    datos2=datos.drop(datos.index[datos.Nombres == "TRUE"],axis=0)
    datos3=datos2.drop(datos2.index[datos2.Nombres == "FALSE"],axis=0)
    datos4=datos3.drop(datos3.index[datos3.Edad < 0],axis=0)
    datos5=datos4.drop(datos4.index[datos4.Edad > 120],axis=0)
    df=pd.DataFrame(datos5)
    df2=df.sort_values(by=["Sueldo"],ascending=[False])
    df3=df2.drop_duplicates(subset="Nombres")
    return df3


def tipo(df3):
    df3["Tipo"] = ""
    df3.loc[df3["Edad"] > int("60"),"Tipo"]="Docente"
    df3.loc[df3["Edad"] < int("60"),"Tipo"]="Estudiante"
    df4=df3
    return df4


def findf(df4):  
    df4.reset_index().to_csv("SolemneFiltrada.csv",header=True,index=False)

def main():
    df1 = inicio()
    df2 = filtrado(df1)
    df3 = tipo(df2)
    df4 = findf(df3)
    print("------------------Cargado------------------")
    return df4


main()

def cargar():
    df = pd.read_csv("SolemneFiltrada.csv", index_col= "index")
    return df

listaE=[]
listaD=[]

def IngresaDatos():
    da = cargar()
    print(da)
    print("-------------------------------------------")


IngresaDatos()
