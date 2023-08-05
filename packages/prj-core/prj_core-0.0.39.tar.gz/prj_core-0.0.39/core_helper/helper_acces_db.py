# -*- coding: utf-8 -*-
import core_helper.helper_general as hg
hg.set_base_path()

#import src.Prj_Core.core_helper.model.general as g
import json
import pandas as pd
import numpy as np
import core_helper.helper_general as hg  
import core_helper.helper_dataframe as hd
from simpledbf import Dbf5


MR_File_Name = "base.txt"

def set_macro_region(filename):
    global MR_File_Name
    MR_File_Name = filename

def get_macro_region(macro):
    global MR_File_Name
    js_mr = hg.get_base_path()+"/config/macro_region/"+MR_File_Name
    with open(js_mr) as json_file:
        data = json.load(json_file)        
        
    if macro not in data: 
            raise Exception("No existe la clave [ " + macro + " ] en el archivo: "+MR_File_Name)
        
    return data[macro]



def get_traslados_por_anio(anio,TIPO_TRASLADO='EN EL MISMO AÑO',modalidad="EBR"):
    path_file = get_path_BD_siagie_procesado()
    url_trasl = path_file+'\\Siagie_Traslados_{}.csv'.format(anio)
    sep = "|"
    encoding = 'latin-1'
    cols_tras = ['ID_PERSONA','TIPO_TRASLADO']

    #df_trasl = pd.read_csv(url_trasl ,encoding='utf-8',usecols=cols_tras,  sep=sep,dtype={'PERSONA_NRO_DOC':str})
    df_trasl = pd.read_csv(url_trasl ,encoding=encoding,usecols=cols_tras,  sep=sep,dtype={'ID_PERSONA':int})
    #if(anio==2019):
        #df_trasl = df_trasl[df_trasl.TIPO_TRASLADO==TIPO_TRASLADO].copy()
        #df_trasl.reset_index(drop=True,inplace=True)
 
    df_agg_t  = df_trasl.assign(
     TOTAL_TRASLADOS =   1
    ).groupby(['ID_PERSONA']).agg({'TOTAL_TRASLADOS':'sum'})

    df_agg_t.sort_values(by='TOTAL_TRASLADOS', ascending=False,inplace=True)
    df_agg_t.reset_index(inplace=True)
    
    return df_agg_t



def get_traslados_a_publico(anio,df_servicios,modalidad):
    path_file = get_path_BD_siagie_procesado()
    url_trasl = path_file+'/Siagie_Traslados_{}.csv'.format(anio)
    sep = "|"
    encoding = 'latin-1'
    cols_tras = ['ID_PERSONA','TIPO_TRASLADO','COD_MOD_ORIGEN','ANEXO_ORIGEN','COD_MOD_DESTINO','ANEXO_DESTINO']

    cl_s = ["COD_MOD","ANEXO","ES_PUBLICO"]
    #df_trasl = pd.read_csv(url_trasl ,encoding='utf-8',usecols=cols_tras,  sep=sep,dtype={'PERSONA_NRO_DOC':str})
    df_trasl = pd.read_csv(url_trasl ,encoding=encoding,usecols=cols_tras,  sep=sep,dtype={'ID_PERSONA':int,
                                                                                           'COD_MOD_ORIGEN':str,
                                                                                           'ANEXO_ORIGEN':int,
                                                                                           'COD_MOD_DESTINO':str,                                                                                           
                                                                                           'ANEXO_DESTINO':int,
                                                                                            })

    df_trasl_origen = pd.merge(df_trasl,df_servicios[cl_s],left_on=["COD_MOD_ORIGEN","ANEXO_ORIGEN"],
                               right_on=["COD_MOD","ANEXO"],how="inner")

    df_trasl_origen.drop(columns=['COD_MOD', 'ANEXO'],inplace=True)
    df_trasl_origen.rename(columns={'ES_PUBLICO': 'ES_PUBLICO_ORIGEN'}, inplace=True)


    df_trasl_destino = pd.merge(df_trasl_origen,df_servicios[cl_s],left_on=["COD_MOD_DESTINO","ANEXO_DESTINO"],
                               right_on=["COD_MOD","ANEXO"],how="inner")

    df_trasl_destino.drop(columns=['COD_MOD', 'ANEXO'],inplace=True)
    df_trasl_destino.rename(columns={'ES_PUBLICO': 'ES_PUBLICO_DESTINO'}, inplace=True)

    df_trasl_destino['TRASLADO_A_PUBLICO'] = np.where((df_trasl_destino.ES_PUBLICO_ORIGEN==0) & 
                                                      (df_trasl_destino.ES_PUBLICO_DESTINO==1),1,0)


    df_trasl_destino = df_trasl_destino[df_trasl_destino["TRASLADO_A_PUBLICO"]==1].copy()
    
    df_agg_t  = df_trasl_destino.assign(
     TOTAL_TRASLADOS =   1
    ).groupby(['ID_PERSONA']).agg({'TOTAL_TRASLADOS':'sum'})

    df_agg_t.sort_values(by='TOTAL_TRASLADOS', ascending=False,inplace=True)
    df_agg_t.reset_index(inplace=True)
    

    return df_agg_t



def get_df_notas(anio):
    
    path_file = get_path_BD_siagie_procesado()
    dtype = {'COD_MOD':str,'ANEXO':np.int8,'NOTA_AREA_REGULAR':np.int8,'DA':str}    
    url_notas = path_file+'\\NOTAS_POR_ALUMNO_{}.csv'.format(anio)
    df_notas = pd.read_csv(url_notas ,encoding='utf-8', dtype=dtype)
    
    return df_notas


def get_df_servicios(macro_region=None,region=None,anio=None,totales=False):
    print("Imprimiendo el anio servicio ",anio)
    
    anio_min = 2016
    if (anio is not None and anio<anio_min):
        raise Exception("No existe data de servicios menor que {}".format(anio_min))
    
    if anio is None:
        print("Extrayendo servicios general")
        url =   get_path_BD() + "\\03.Servicios\\_data_\\Padron_web.dbf"        
        dbf_ser = Dbf5(url , codec='ISO-8859-1')
        df_servicios = dbf_ser.to_dataframe()
        
    elif anio<=2020:
        url =   get_path_BD()+"\\03.Servicios\\_data_\\Padron_web_{}.dbf".format(anio)        
        dbf_ser = Dbf5(url , codec='ISO-8859-1')
        df_servicios = dbf_ser.to_dataframe()
        if anio==2016:
            df_codii_dre =  pd.read_csv(get_path_BD() + "\\03.Servicios\\_data_\\CODOOII_D_REGION.csv",dtype={'CODOOII': str})
            df_servicios = pd.merge(df_servicios,df_codii_dre,left_on="CODOOII",right_on="CODOOII",how="inner")
            df_servicios.rename(columns={'D_AREASIG': 'DAREACENSO'}, inplace=True)       
        
    elif anio==2021:        
                
        url =   get_path_BD() + "\\03.Servicios\\_data_\\Padron_web_2021.dbf"        
        dbf_ser = Dbf5(url , codec='ISO-8859-1')
        df_servicios = dbf_ser.to_dataframe()
        df_servicios.columns = map(lambda x: str(x).upper(), df_servicios.columns)
        #url =   get_path_BD() + "\\03.Servicios\\_data_\\Padron_web_2021.dta"        
        #df_servicios = pd.read_stata(url)   
        #df_servicios.columns = map(lambda x: str(x).upper(), df_servicios.columns)
        
    cls = ["COD_MOD","ANEXO","CODGEO","GESTION","DAREACENSO",'D_TIPSSEXO','D_REGION']
    if totales:
        cls = cls + ['TALUM_HOM','TALUM_MUJ','TALUMNO', 'TDOCENTE', 'TSECCION']
    
    df_servicios = df_servicios[cls].copy() 
    df_servicios["ANEXO"] =df_servicios['ANEXO'].astype("int8")
    df_servicios["GESTION"] =df_servicios['GESTION'].astype("int8")    

    #df_servicios["AREA_CENSO"] =df_servicios['AREA_CENSO'].astype("int8")
    df_servicios['ES_PUBLICO'] = np.where(df_servicios['GESTION'].isin([1,2]),1,0)
    df_servicios['ES_URBANA'] = np.where(df_servicios['DAREACENSO']=='Urbana',1,0)
    df_servicios['ES_MIXTO'] = np.where(df_servicios['D_TIPSSEXO']=='Mixto',1,0)
    df_servicios['COD_MOD']=df_servicios['COD_MOD'].apply(lambda x: '{0:0>7}'.format(x))
    
    df_servicios.drop(['GESTION',"CODGEO", 'DAREACENSO', 'D_TIPSSEXO'], axis=1,inplace=True)
    
    if macro_region is not None:
        l_mr = get_macro_region(macro_region)
        df_servicios = df_servicios[df_servicios["D_REGION"].isin(l_mr)].copy()
    
    if region is not None:
        df_servicios = df_servicios[df_servicios["D_REGION"]==region].copy()
        
    return df_servicios


def get_desertores_por_anio(anio,modalidad="EBR"):
    
    path_file = get_path_BD_siagie_procesado()
    if(modalidad=="EBR"):
        url = path_file+"\\DESERCION\\DESERCION_{}"
    elif(modalidad=="EBE"):
        url = path_file+"\\DESERCION\\DESERCION_EBE_{}"
        
    anios_str=str(anio)+"_"+str(anio+1)
    ds = pd.read_csv(url.format("{}.csv".format(anios_str)))

    return ds


def get_shock_economico(anio,modalidad="EBR"):
    columns_n = ["ID_PERSONA","LOG_ING_T_MAS_1_IMP_DIST","NA_LOG_ING_T_MAS_1_IMP_DIST"] 
    dtypes_columns={'ID_PERSONA':int}
    url = get_path_BD()+"\\05.Schock_economico\\_data_\\procesado\\workfile_{}_{}_v2.csv".format(modalidad,anio)
    ds_ = pd.read_csv(url,usecols=columns_n,dtype=dtypes_columns) #
    return ds_

def get_sisfoh():
    url_sisfoh = get_path_BD()+'\\04.SISFOH\\_data_\\NOMINAL_SISFOH.csv'
    cols = ['PERSONA_NRO_DOC','SISFOH_CSE']    
    df_sisfoh = pd.read_csv(url_sisfoh ,usecols=cols, encoding='utf-8', dtype={'PERSONA_NRO_DOC':str})
    df_sisfoh.drop_duplicates(subset ="PERSONA_NRO_DOC", keep = "last", inplace = True)
    return df_sisfoh


def get_distancia_prim_sec():
    
    url_ddist = get_path_BD() + "\\03.Servicios\\_data_\\SecundariaCerca.csv"
    df_sec_cerca =pd.read_csv(url_ddist, encoding="utf-8",index_col=0) 

    df_sec_cerca.loc[(df_sec_cerca['Distancia'] == 0), 'GRUPO_DISTANCIA'] = '0K'
    df_sec_cerca.loc[(df_sec_cerca['Distancia'] > 0) & (df_sec_cerca['Distancia'] <= 1000), 'GRUPO_DISTANCIA'] = 'MENOR_1K'
    df_sec_cerca.loc[(df_sec_cerca['Distancia'] > 1000) & (df_sec_cerca['Distancia'] <= 5000), 'GRUPO_DISTANCIA'] = '1K_5K'
    df_sec_cerca.loc[(df_sec_cerca['Distancia'] > 5000), 'GRUPO_DISTANCIA'] = 'MAYOR_5K'

    df_sec_cerca.columns = [x.upper() for x in df_sec_cerca.columns]

    df_sec_cerca[['COD_MOD','ANEXO']] = df_sec_cerca.CODIGOLUGAR.str.split("-",expand=True)
    df_sec_cerca['ANEXO'] = df_sec_cerca['ANEXO'].astype('uint8')

    df_sec_cerca['COD_MOD']=df_sec_cerca['COD_MOD'].apply(lambda x: '{0:0>7}'.format(x))
    del df_sec_cerca['SECUNDARIACERCA']
    del df_sec_cerca['CODIGOLUGAR']
    
    
    return df_sec_cerca


def get_path_BD_siagie_procesado():
    path_file =get_path_BD() +"\\01.SIAGIE\\_data_\\procesado"
    return path_file

def get_path_BD_siagie_sin_procesar():
    path_file =get_path_BD() +"\\01.SIAGIE\\_data_\\sin_procesar"
    return path_file

def get_path_BD():
    path_file =hg.get_base_path()+"\\src\\Prj_BD"
    return path_file



def get_siagie_por_anio(anio,id_grado=None,modalidad='EBR',dtypes_columns={'ID_PERSONA':int,'COD_MOD':str,'ANEXO':int},
                        columns_n= ['ID_PERSONA','ID_GRADO','ID_NIVEL','COD_MOD','ANEXO'],
                        id_persona_df=None,id_nivel=None,id_nivel_list=None,reduce_mem_usage=False):  

    id_niveles_inicial_ebr = ['A1','A2','A3','A5']
    if id_nivel  is not None:
        if id_nivel=="A0":      
            print("El nivel ficticio A0  sera reemplazado por los verdaderos niveles ",id_niveles_inicial_ebr)
            
    if id_nivel_list  is not None:
        if "A0" in id_nivel_list:    
            print("El nivel ficticio A0  sera reemplazado por los verdaderos niveles ",id_niveles_inicial_ebr)
     

    path_file = get_path_BD_siagie_procesado()
    if (modalidad=='EBR'):    
        if(anio<2019):
            url = path_file+"\\NOMINAL_{}.csv"
            iter_pd = pd.read_csv(url.format(anio), usecols=columns_n,encoding="latin-1",sep="|",
                                  dtype=dtypes_columns,iterator=True, chunksize=500000)
            

            df = procesar_chunk_siagie(iter_pd,id_grado,id_persona_df,id_nivel,id_nivel_list,id_niveles_inicial_ebr)
        else:
            list_df = []
            for nivel in ["A0","B0","F0"]:               
                
                url = path_file+"\\NOMINAL_{}_{}.csv"
                iter_pd = pd.read_csv(url.format(nivel,anio), usecols=columns_n,encoding="latin-1",
                                      sep="|",dtype=dtypes_columns,iterator=True, chunksize=500000)
                
                df = procesar_chunk_siagie(iter_pd,id_grado,id_persona_df,id_nivel,id_nivel_list,id_niveles_inicial_ebr)
                list_df.append(df)
                
            df = pd.concat(list_df)
            
    elif(modalidad=='EBE'):
            url = path_file+"\\NOMINAL_{}_{}.csv"
            df = pd.read_csv(url.format("E0",anio), usecols=columns_n,encoding="latin-1",sep="|",dtype=dtypes_columns)
                
    df = df.drop_duplicates(subset=['ID_PERSONA'], keep='last')
    
    if reduce_mem_usage:
        return hd.reduce_mem_usage(df)
    else:    
        return df


def procesar_chunk_siagie(iter_pd,id_grado,id_persona_df,id_nivel,id_nivel_list,id_niveles_inicial_ebr):
    chunk_list = []

    for chunk in iter_pd:
        if id_grado  is not None:
            chunk = chunk[(chunk['ID_GRADO'] == id_grado)] 
        if id_nivel  is not None:
            if id_nivel=="A0":     
                chunk = chunk[(chunk['ID_NIVEL'].isin(id_niveles_inicial_ebr))] 
            else:                  
                chunk = chunk[(chunk['ID_NIVEL'] == id_nivel)]  
        if id_nivel_list  is not None:
            if "A0" in id_nivel_list:    
                id_nivel_list.remove( "A0")                
                id_nivel_list = id_nivel_list + id_niveles_inicial_ebr                
            chunk = chunk[(chunk['ID_NIVEL'].isin(id_nivel_list))]  
        if id_persona_df is not None:
            #print(id_persona_df.shape)
            chunk = pd.merge(chunk, id_persona_df[['ID_PERSONA']], left_on="ID_PERSONA", right_on="ID_PERSONA", how='inner')
        chunk_list.append(chunk)
    return pd.concat(chunk_list)

