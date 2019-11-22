# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:55:53 2019

@author: 90506
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:25:38 2019

@author: 90506
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:59:28 2019

@author: 90506
"""

#COMScalculation
import os
import pandas as pd
import numpy as np
import EconomicCOMS
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t1.xlsx')
df_area=df2.groupby("CensusBlock").apply(lambda dfx: (dfx["km2"].sum()/dfx["BlockArea"]).reset_index(name='AreaInundated'))
df_area=df_area.drop_duplicates(subset='AreaInundated',keep='first')
###
dpo=pd.read_excel(r'D:\SelinaDEM\oye3\Mean.xlsx')
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureByBlock")
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
##
df_comb["frstRES4"]=1
#Water depth-first floor height=effective flood depth for COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,COM10,RES4,RES5,RES6,IND1,IND2,IND3,IND4,IND5,IND6
df_comb["Finalwaterlevel"]=df_comb["WaterLevelftA"]-df_comb["frstRES4"]#Final water level
#Calculation
df_comb['COM1StructureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM1,axis=1)/100
df_comb['COM1ContentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM1Content,axis=1)/100
df_comb['COM1InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicCOM1Inventory,axis=1)/100
df_comb['COM2StructureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM2,axis=1)/100
df_comb['COM2ContentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM2Content,axis=1)/100
df_comb['COM2InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicCOM2Inventory,axis=1)/100
df_comb['COM3structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM3Structure,axis=1)/100
df_comb['COM3ContentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM3Content,axis=1)/100
df_comb['COM4structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM4Structure,axis=1)/100
df_comb['COM4ContentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM4Content,axis=1)/100
df_comb['COM5structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM5Structure,axis=1)/100
df_comb['COM5contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM5Content,axis=1)/100
df_comb['COM6structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM6Structure,axis=1)/100
df_comb['COM6contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM6Content,axis=1)/100
df_comb['COM7structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM7Structure,axis=1)/100
df_comb['COM7contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM7Content,axis=1)/100
df_comb['COM8structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM8Structure,axis=1)/100
df_comb['COM8contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM8Content,axis=1)/100
df_comb['COM9structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM9Structure,axis=1)/100
df_comb['COM9contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM9Content,axis=1)/100
df_comb['COM10structureDamage']=df_comb.apply(EconomicCOMS.EconomicCOM10Structure,axis=1)/100
df_comb['COM10contentDamage']=df_comb.apply(EconomicCOMS.EconomicCOM10Content,axis=1)/100
####


df3=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM2StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM2StructureWeigh')
df4=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM3structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM3StructureWeigh')
df5=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM4structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM4StructureWeigh')
df6=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM5structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM5StructureWeigh')
df7=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM6structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM6StructureWeigh')
df8=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM7structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM7StructureWeigh')
df9=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM8structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM8StructureWeigh')
df10=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM9structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM9StructureWeigh')
df11=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM10structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM10StructureWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM1StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM1StructureWeigh')
dfc1=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM1InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM1InventoryWeigh')
dfc2=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM2InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM2InventoryWeigh')
###Content
dfc9=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM2ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM2ContentWeigh')
dfc10=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM3ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM3ContentWeigh')
dfc11=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM4ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM4ContentWeigh')
dfc12=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM5contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM5ContentWeigh')
dfc13=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM6contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM6ContentWeigh')
dfc14=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM7contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM7ContentWeigh')
dfc15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM8contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM8ContentWeigh')
dfc16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM9contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM9ContentWeigh')
dfc17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM10contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM10ContentWeigh')
dfc30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["COM1ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM1ContentWeigh')
###


###
df_comb=pd.merge(df_comb,df3,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df4,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df5,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df6,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df7,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df8,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df9,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df10,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df11,on='CensusBlock',how='left')
##
df_comb=pd.merge(df_comb,df24,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc2,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc9,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc10,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc11,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc12,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc13,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc14,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc15,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc16,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc17,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc30,on='CensusBlock',how='left')

#COM10
def COM10Smake1(df_comb):
    if (df_comb['COM10StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM10StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM10StructureWeigh']
#COM9
def COM9Smake1(df_comb):
    if (df_comb['COM9StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM9StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM9StructureWeigh']
#COM8
def COM8Smake1(df_comb):
    if (df_comb['COM8StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM8StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM8StructureWeigh']
#COM7
def COM7Smake1(df_comb):
    if (df_comb['COM7StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM7StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM7StructureWeigh']
#COM6
def COM6Smake1(df_comb):
    if (df_comb['COM6StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM6StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM6StructureWeigh']
#COM5
def COM5Smake1(df_comb):
    if (df_comb['COM5StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM5StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM5StructureWeigh']
#COM4
def COM4Smake1(df_comb):
    if (df_comb['COM4StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM4StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM4StructureWeigh']
#COM3
def COM3Smake1(df_comb):
    if (df_comb['COM3StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM3StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM3StructureWeigh']
#COM2Structure
def COM2Smake1(df_comb):
    if (df_comb['COM2StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM2StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM2StructureWeigh']
#COM2Inventory
###BURAYA SONUÇLARA GÖRE YİNE İF CLAUSE'LU BİR ŞEY GELEBİLİR ÖNCELİKLE O IF CLAUSE'SUZ DENE  
#COM1
def COM1Smake1(df_comb):
    if (df_comb['COM1StructureWeigh']>0.5):
        return 1
    elif (df_comb['COM1StructureWeigh']<0):
        return 0
    else:
        return df_comb['COM1StructureWeigh']
###
df_comb['COM1StructureWeigh']=df_comb.apply(COM1Smake1,axis=1) 
df_comb['COM2StructureWeigh']=df_comb.apply(COM2Smake1,axis=1) 
df_comb['COM3StructureWeigh']=df_comb.apply(COM3Smake1,axis=1) 
df_comb['COM4StructureWeigh']=df_comb.apply(COM4Smake1,axis=1)  
df_comb['COM5StructureWeigh']=df_comb.apply(COM5Smake1,axis=1)   
df_comb['COM6StructureWeigh']=df_comb.apply(COM6Smake1,axis=1)
df_comb['COM7StructureWeigh']=df_comb.apply(COM7Smake1,axis=1) 
df_comb['COM8StructureWeigh']=df_comb.apply(COM8Smake1,axis=1)   
df_comb['COM9StructureWeigh']=df_comb.apply(COM9Smake1,axis=1) 
df_comb['COM10StructureWeigh']=df_comb.apply(COM10Smake1,axis=1)
###
df_comb['COM1StructureWeigh']=df_comb.apply(COM1Smake1,axis=1) 
df_comb['COM2StructureWeigh']=df_comb.apply(COM2Smake1,axis=1) 
df_comb['COM3StructureWeigh']=df_comb.apply(COM3Smake1,axis=1) 
df_comb['COM4StructureWeigh']=df_comb.apply(COM4Smake1,axis=1)  
df_comb['COM5StructureWeigh']=df_comb.apply(COM5Smake1,axis=1)   
df_comb['COM6StructureWeigh']=df_comb.apply(COM6Smake1,axis=1)
df_comb['COM7StructureWeigh']=df_comb.apply(COM7Smake1,axis=1) 
df_comb['COM8StructureWeigh']=df_comb.apply(COM8Smake1,axis=1)   
df_comb['COM9StructureWeigh']=df_comb.apply(COM9Smake1,axis=1) 
df_comb['COM10StructureWeigh']=df_comb.apply(COM10Smake1,axis=1)






###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
##
###Building
df_comb["COM1LossStrDC"]=df_comb["DCCOM1"]*df_comb["COM1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM1LossStrVA"]=df_comb["VCOM1"]*df_comb["COM1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM1LossStrM"]=df_comb["MCOM1"]*df_comb["COM1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM1TotalStr"]=df_comb["COM1LossStrDC"]+df_comb["COM1LossStrVA"]+df_comb["COM1LossStrM"]
####
df_comb["COM2LossStrDC"]=df_comb["DCCOM2"]*df_comb["COM2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM2LossStrVA"]=df_comb["VCOM2"]*df_comb["COM2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM2LossStrM"]=df_comb["MCOM2"]*df_comb["COM2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM2TotalStr"]=df_comb["COM2LossStrDC"]+df_comb["COM2LossStrVA"]+df_comb["COM2LossStrM"]
###
df_comb["COM3LossStrDC"]=df_comb["DCCOM3"]*df_comb["COM3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM3LossStrVA"]=df_comb["VCOM3"]*df_comb["COM3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM3LossStrM"]=df_comb["MCOM3"]*df_comb["COM3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM3TotalStr"]=df_comb["COM3LossStrDC"]+df_comb["COM3LossStrVA"]+df_comb["COM3LossStrM"]
####
df_comb["COM4LossStrDC"]=df_comb["DCCOM4"]*df_comb["COM4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM4LossStrVA"]=df_comb["VCOM4"]*df_comb["COM4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM4LossStrM"]=df_comb["MCOM4"]*df_comb["COM4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM4TotalStr"]=df_comb["COM4LossStrDC"]+df_comb["COM4LossStrVA"]+df_comb["COM4LossStrM"]
###
df_comb["COM5LossStrDC"]=df_comb["DCCOM5"]*df_comb["COM5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM5LossStrVA"]=df_comb["VCOM5"]*df_comb["COM5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM5LossStrM"]=df_comb["MCOM5"]*df_comb["COM5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM5TotalStr"]=df_comb["COM5LossStrDC"]+df_comb["COM5LossStrVA"]+df_comb["COM5LossStrM"]
###
df_comb["COM6LossStrDC"]=df_comb["DCCOM6"]*df_comb["COM6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM6LossStrVA"]=df_comb["VCOM6"]*df_comb["COM6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM6LossStrM"]=df_comb["MCOM6"]*df_comb["COM6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM6TotalStr"]=df_comb["COM6LossStrDC"]+df_comb["COM6LossStrVA"]+df_comb["COM6LossStrM"]
###
df_comb["COM7LossStrDC"]=df_comb["DCCOM7"]*df_comb["COM7StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM7LossStrVA"]=df_comb["VCOM7"]*df_comb["COM7StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM7LossStrM"]=df_comb["MCOM7"]*df_comb["COM7StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM7TotalStr"]=df_comb["COM7LossStrDC"]+df_comb["COM7LossStrVA"]+df_comb["COM7LossStrM"]
####
df_comb["COM8LossStrDC"]=df_comb["DCCOM8"]*df_comb["COM8StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM8LossStrVA"]=df_comb["VCOM8"]*df_comb["COM8StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM8LossStrM"]=df_comb["MCOM8"]*df_comb["COM8StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM8TotalStr"]=df_comb["COM8LossStrDC"]+df_comb["COM8LossStrVA"]+df_comb["COM8LossStrM"]
###
df_comb["COM9LossStrDC"]=df_comb["DCCOM9"]*df_comb["COM9StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM9LossStrVA"]=df_comb["VCOM9"]*df_comb["COM9StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM9LossStrM"]=df_comb["MCOM9"]*df_comb["COM9StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM9TotalStr"]=df_comb["COM9LossStrDC"]+df_comb["COM9LossStrVA"]+df_comb["COM9LossStrM"]
###
df_comb["COM10LossStrDC"]=df_comb["DCCOM10"]*df_comb["COM10StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM10LossStrVA"]=df_comb["VCOM10"]*df_comb["COM10StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM10LossStrM"]=df_comb["MCOM10"]*df_comb["COM10StructureWeigh"]*df_comb["AreaInundated"]
df_comb["COM10TotalStr"]=df_comb["COM10LossStrDC"]+df_comb["COM10LossStrVA"]+df_comb["COM10LossStrM"]
###

###Content
COM1loss=df_comb["COM1TotalStr"].sum()
COM2loss=df_comb["COM2TotalStr"].sum()
COM3loss=df_comb["COM3TotalStr"].sum()
COM4loss=df_comb["COM4TotalStr"].sum()
COM5loss=df_comb["COM5TotalStr"].sum()
COM6loss=df_comb["COM6TotalStr"].sum()
COM7loss=df_comb["COM7TotalStr"].sum()
COM8loss=df_comb["COM8TotalStr"].sum()
COM9loss=df_comb["COM9TotalStr"].sum()
COM10loss=df_comb["COM10TotalStr"].sum()
###################33
print(COM1loss*1000)
print(COM2loss*1000)
print(COM3loss*1000)
print(COM4loss*1000)
print(COM5loss*1000)
print(COM6loss*1000)
print(COM7loss*1000)
print(COM8loss*1000)
print(COM9loss*1000)
print(COM10loss*1000)
###




