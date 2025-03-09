def cargar_dataset(archivo):
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
    #archivo = input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
    #Cargar el carchivo según su extención
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return(df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f"Formato de archivo no soportado: {extension}")

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()

    return("Valores nulos por columna", valores_nulos_cols,
           "Valores nulos por dataframe", valores_nulos_df)

#ffill
def sustitucion_ffill(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "object") | (data_type == "category")|(data_type == "int64") | (data_type == "float64"):  
            dataframe[col] = dataframe[col].fillna(method="ffill") 
    return dataframe 

#Bfill
def sustitucion_bfill(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "object") | (data_type == "category")|(data_type == "int64") | (data_type == "float64"):  
            dataframe[col] = dataframe[col].fillna(method="bfill")  
    return dataframe  

#promedio
def sustitucion_promedio(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            mean_value = dataframe[col].mean()    
            dataframe[col] = dataframe[col].fillna(round(mean_value, 1)) 
    return dataframe 

#mediana
def sustitucion_mediana(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            mediana_value = dataframe[col].median()    
            dataframe[col] = dataframe[col].fillna(round(mediana_value, 1)) 
    return dataframe 

#string concreto
def sustitucion_string_concreto(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "object") | (data_type == "category"):  
            dataframe[col] = dataframe[col].fillna("f")
    return dataframe  

#constante
def sustitucion_constante(dataframe, cols):  
    for col in cols:  
        data_type = dataframe[col].dtype  
        if (data_type == "int64") | (data_type == "float64"):  
            dataframe[col] = dataframe[col].fillna(3)
    return dataframe 