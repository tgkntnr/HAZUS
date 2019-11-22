# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:21:51 2019

@author: 90506
"""

import os
import pandas as pd
import numpy as np
import EconomicCOMS
import EconomicRESS
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t7.xlsx')
df_area=df2.groupby("CensusBlock").apply(lambda dfx: (dfx["km2"].sum()/dfx["BlockArea"]).reset_index(name='AreaInundated'))
df_area=df_area.drop_duplicates(subset='AreaInundated',keep='first')
###
dpo=pd.read_excel(r'D:\SelinaDEM\oye3\Mean.xlsx')
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureByBlock")
###
dxo1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureContentByBlock")
dyo1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureContentByBlock")
dyt1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureContentByBlock")
###
dxo2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="BuildingsqftByBlock")
dyo2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="BuildingsqftByBlock")
dyt2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="BuildingsqftByBlock")
###
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo2,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo2,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt2,on='CensusBlock',how='left')
####
df_comb["frstRES4"]=1
#Water depth-first floor height=effective flood depth for COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,COM10,RES4,RES5,RES6,IND1,IND2,IND3,IND4,IND5,IND6
df_comb["Finalwaterlevel"]=df_comb["WaterLevelftA"]-df_comb["frstRES4"]#Final water level
##
df_comb['IND1StructureDamage']=df_comb.apply(EconomicCOMS.EconomicIND1Structure,axis=1)/100
df_comb['IND1ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND1Content,axis=1)/100
df_comb['IND1InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND1Inventory,axis=1)/100
df_comb['IND2StructureDamage']=df_comb.apply(EconomicCOMS.EconomicIND2Structure,axis=1)/100
df_comb['IND2ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND2Content,axis=1)/100
df_comb['IND2InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND2Inventory,axis=1)/100
df_comb['IND3structureDamage']=df_comb.apply(EconomicCOMS.EconomicIND3Structure,axis=1)/100
df_comb['IND3ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND3Content,axis=1)/100
df_comb['IND3InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND3Inventory,axis=1)/100
df_comb['IND4StructureDamage']=df_comb.apply(EconomicCOMS.EconomicIN4Structure,axis=1)/100
df_comb['IND4ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND4Content,axis=1)/100
df_comb['IND4InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND4Inventory,axis=1)/100
df_comb['IND5structureDamage']=df_comb.apply(EconomicCOMS.EconomicIND5Structure,axis=1)/100
df_comb['IND5ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND5Content,axis=1)/100
df_comb['IND5InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND5Inventory,axis=1)/100
df_comb['IND6structureDamage']=df_comb.apply(EconomicCOMS.EconomicIND6Structure,axis=1)/100
df_comb['IND6ContentDamage']=df_comb.apply(EconomicCOMS.EconomicIND6Content,axis=1)/100
df_comb['IND6InventoryDamage']=df_comb.apply(EconomicCOMS.EconomicIND6Inventory,axis=1)/100
df_comb['RES4structureDamage']=df_comb.apply(EconomicRESS.EconomicRES4Structure,axis=1)/100
df_comb['RES4contentDamage']=df_comb.apply(EconomicRESS.EconomicRES4content,axis=1)/100
df_comb['RES5structureDamage']=df_comb.apply(EconomicRESS.EconomicRES5Structure,axis=1)/100
df_comb['RES5contentDamage']=df_comb.apply(EconomicRESS.EconomicRES5content,axis=1)/100
df_comb['RES6structureDamage']=df_comb.apply(EconomicRESS.EconomicRES6Structure,axis=1)/100
df_comb['RES6contentDamage']=df_comb.apply(EconomicRESS.EconomicRES6content,axis=1)/100
###
df3=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND1StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND1StructureWeigh')
df4=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND1ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND1ContentWeigh')
df5=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND1InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND1InventoryWeigh')
df6=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND2StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND2StructureWeigh')
df7=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND2ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND2ContentWeigh')
df8=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND2InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND2InventoryWeigh')
df9=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND3structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND3StructureWeigh')
df10=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND3ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND3ContentWeigh')
df11=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND3InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND3InventoryWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND4StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND4StructureWeigh')
dfc1=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND4ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND4ContentWeigh')
dfc2=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND4InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND4InventoryWeigh')
dfc9=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND5structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND5StructureWeigh')
dfc10=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND5ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND5ContentWeigh')
dfc11=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND5InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND5InventoryWeigh')
dfc12=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND6structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND6StructureWeigh')
dfc13=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND6ContentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND6ContentWeigh')
dfc14=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["IND6InventoryDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND6InventoryWeigh')
dfc15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES4structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES4StructureWeigh')
dfc16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES4contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES4ContentWeigh')
dfc17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES5structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES5StructureWeigh')
dfc30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES5contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES5ContentWeigh')
dfc18=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES6structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES6StructureWeigh')
dfc31=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES6contentDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES6ContentWeigh')
####
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
df_comb=pd.merge(df_comb,dfc18,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dfc31,on='CensusBlock',how='left')
######33
 #IND6
def IND6Smake1(df_comb):
    if (df_comb['IND6StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND6StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND6StructureWeigh']  
#IND5
def IND5Smake1(df_comb):
    if (df_comb['IND5StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND5StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND5StructureWeigh']
#IND4
def IND4Smake1(df_comb):
    if (df_comb['IND4StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND4StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND4StructureWeigh']
#IND3
def IND3Smake1(df_comb):
    if (df_comb['IND3StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND3StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND3StructureWeigh']
#IND2
def IND2Smake1(df_comb):
    if (df_comb['IND2StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND2StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND2StructureWeigh']
#IND1
def IND1Smake1(df_comb):
    if (df_comb['IND1StructureWeigh']>0.5):
        return 1
    elif (df_comb['IND1StructureWeigh']<0):
        return 0
    else:
        return df_comb['IND1StructureWeigh']
#RES6
def RES6Smake1(df_comb55):
    if (df_comb55['RES6StructureWeigh']>0.5):
        return 1
    elif (df_comb55['RES6StructureWeigh']<0):
        return 0
    else:
        return df_comb55['RES6StructureWeigh']
#RES5
def RES5Smake1(df_comb55):
    if (df_comb55['RES5StructureWeigh']>0.5):
        return 1
    elif (df_comb55['RES5StructureWeigh']<0):
        return 0
    else:
        return df_comb55['RES5StructureWeigh']
#RES4
def RES4Smake1(df_comb55):
    if (df_comb55['RES4StructureWeigh']>0.5):
        return 1
    elif (df_comb55['RES4StructureWeigh']<0):
        return 0
    else:
        return df_comb55['RES4StructureWeigh']

df_comb['IND1StructureWeigh']=df_comb.apply(IND1Smake1,axis=1) 
df_comb['IND2StructureWeigh']=df_comb.apply(IND2Smake1,axis=1) 
df_comb['IND3StructureWeigh']=df_comb.apply(IND3Smake1,axis=1) 
df_comb['IND4StructureWeigh']=df_comb.apply(IND4Smake1,axis=1)  
df_comb['IND5StructureWeigh']=df_comb.apply(IND5Smake1,axis=1)   
df_comb['IND6StructureWeigh']=df_comb.apply(IND6Smake1,axis=1)
df_comb['RES6StructureWeigh']=df_comb.apply(RES6Smake1,axis=1) 
df_comb['RES5StructureWeigh']=df_comb.apply(RES5Smake1,axis=1)   
df_comb['RES4StructureWeigh']=df_comb.apply(RES4Smake1,axis=1)
###

###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
##
df_comb["IND1LossStrDC"]=df_comb["DCIND1"]*df_comb["IND1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND1LossStrVA"]=df_comb["VIND1"]*df_comb["IND1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND1LossStrM"]=df_comb["MIND1"]*df_comb["IND1StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND1TotalStr"]=df_comb["IND1LossStrVA"]+df_comb["IND1LossStrDC"]+df_comb["IND1LossStrM"]
####
df_comb["IND2LossStrDC"]=df_comb["DCIND2"]*df_comb["IND2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND2LossStrVA"]=df_comb["VIND2"]*df_comb["IND2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND2LossStrM"]=df_comb["MIND2"]*df_comb["IND2StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND2TotalStr"]=df_comb["IND2LossStrVA"]+df_comb["IND2LossStrDC"]+df_comb["IND2LossStrM"]
####
df_comb["IND3LossStrDC"]=df_comb["DCIND3"]*df_comb["IND3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND3LossStrVA"]=df_comb["VIND3"]*df_comb["IND3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND3LossStrM"]=df_comb["MIND3"]*df_comb["IND3StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND3TotalStr"]=df_comb["IND3LossStrVA"]+df_comb["IND3LossStrDC"]+df_comb["IND3LossStrM"]
####
df_comb["IND4LossStrDC"]=df_comb["DCIND4"]*df_comb["IND4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND4LossStrVA"]=df_comb["VIND4"]*df_comb["IND4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND4LossStrM"]=df_comb["MIND4"]*df_comb["IND4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND4TotalStr"]=df_comb["IND4LossStrVA"]+df_comb["IND4LossStrDC"]+df_comb["IND4LossStrM"]
####
df_comb["IND5LossStrDC"]=df_comb["DCIND5"]*df_comb["IND5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND5LossStrVA"]=df_comb["VIND5"]*df_comb["IND5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND5LossStrm"]=df_comb["MIND5"]*df_comb["IND5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND5TotalStr"]=df_comb["IND5LossStrVA"]+df_comb["IND5LossStrDC"]+df_comb["IND5LossStrm"]
###
df_comb["IND6LossStrDC"]=df_comb["DCIND6"]*df_comb["IND6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND6LossStrVA"]=df_comb["VIND6"]*df_comb["IND6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND6LossStrM"]=df_comb["MIND6"]*df_comb["IND6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["IND6TotalStr"]=df_comb["IND6LossStrVA"]+df_comb["IND6LossStrDC"]+df_comb["IND6LossStrM"]
###
df_comb["RES4LossStrDC"]=df_comb["DCRES4"]*df_comb["RES4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES4LossStrVA"]=df_comb["VRES4"]*df_comb["RES4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES4LossStrM"]=df_comb["MRES4"]*df_comb["RES4StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES4TotalStr"]=df_comb["RES4LossStrVA"]+df_comb["RES4LossStrDC"]+df_comb["RES4LossStrM"]
###
df_comb["RES5LossStrDC"]=df_comb["DCRES5"]*df_comb["RES5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES5LossStrVA"]=df_comb["VRES5"]*df_comb["RES5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES5LossStrM"]=df_comb["MRES5"]*df_comb["RES5StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES5TotalStr"]=df_comb["RES5LossStrVA"]+df_comb["RES5LossStrDC"]+df_comb["RES5LossStrM"]
####
df_comb["RES6LossStrDC"]=df_comb["DCRES6"]*df_comb["RES6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES6LossStrVA"]=df_comb["VRES6"]*df_comb["RES6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES6LossStrM"]=df_comb["MRES6"]*df_comb["RES6StructureWeigh"]*df_comb["AreaInundated"]
df_comb["RES6TotalStr"]=df_comb["RES6LossStrVA"]+df_comb["RES6LossStrDC"]+df_comb["RES6LossStrM"]
#################################################################################################
df_comb["IND1LossCntDC"]=df_comb["CDCIND1"]*df_comb["IND1ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND1LossCntVA"]=df_comb["CVIND1"]*df_comb["IND1ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND1LossCntM"]=df_comb["CMIND1"]*df_comb["IND1ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND1TotalCnt"]=df_comb["IND1LossCntDC"]+df_comb["IND1LossCntVA"]+df_comb["IND1LossCntM"]
####
df_comb["IND2LossCntDC"]=df_comb["CDCIND2"]*df_comb["IND2ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND2LossCntVA"]=df_comb["CVIND2"]*df_comb["IND2ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND2LossCntM"]=df_comb["CMIND2"]*df_comb["IND2ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND2TotalCnt"]=df_comb["IND2LossCntVA"]+df_comb["IND2LossCntDC"]+df_comb["IND2LossCntM"]
####
df_comb["IND3LossCntDC"]=df_comb["CDCIND3"]*df_comb["IND3ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND3LossCntVA"]=df_comb["CVIND3"]*df_comb["IND3ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND3LossCntM"]=df_comb["CMIND3"]*df_comb["IND3ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND3TotalCnt"]=df_comb["IND3LossCntDC"]+df_comb["IND3LossCntVA"]+df_comb["IND3LossCntM"]
####
df_comb["IND4LossCntDC"]=df_comb["CDCIND4"]*df_comb["IND4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND4LossCntVA"]=df_comb["CVIND4"]*df_comb["IND4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND4LossCntM"]=df_comb["CMIND4"]*df_comb["IND4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND4TotalCnt"]=df_comb["IND4LossCntVA"]+df_comb["IND4LossCntDC"]+df_comb["IND4LossCntM"]
####
df_comb["IND5LossCntDC"]=df_comb["CDCIND5"]*df_comb["IND5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND5LossCntVA"]=df_comb["CVIND5"]*df_comb["IND5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND5LossCntm"]=df_comb["CMIND5"]*df_comb["IND5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND5TotalCnt"]=df_comb["IND5LossCntVA"]+df_comb["IND5LossCntDC"]+df_comb["IND5LossCntm"]
###
df_comb["IND6LossCntDC"]=df_comb["CDCIND6"]*df_comb["IND6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND6LossCntVA"]=df_comb["CVIND6"]*df_comb["IND6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND6LossCntM"]=df_comb["CMIND6"]*df_comb["IND6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["IND6TotalCnt"]=df_comb["IND6LossCntVA"]+df_comb["IND6LossCntDC"]+df_comb["IND6LossCntM"]
###
df_comb["RES4LossCntDC"]=df_comb["CDCRES4"]*df_comb["RES4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES4LossCntVA"]=df_comb["CVRES4"]*df_comb["RES4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES4LossCntM"]=df_comb["CMRES4"]*df_comb["RES4ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES4TotalCnt"]=df_comb["RES4LossCntVA"]+df_comb["RES4LossCntDC"]+df_comb["RES4LossCntM"]
###
df_comb["RES5LossCntDC"]=df_comb["CDCRES5"]*df_comb["RES5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES5LossCntVA"]=df_comb["CVRES5"]*df_comb["RES5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES5LossCntM"]=df_comb["CMRES5"]*df_comb["RES5ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES5TotalCnt"]=df_comb["RES5LossCntDC"]+df_comb["RES5LossCntVA"]+df_comb["RES5LossCntM"]
####
df_comb["RES6LossCntDC"]=df_comb["CDCRES6"]*df_comb["RES6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES6LossCntVA"]=df_comb["CVRES6"]*df_comb["RES6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES6LossCntM"]=df_comb["CMRES6"]*df_comb["RES6ContentWeigh"]*df_comb["AreaInundated"]
df_comb["RES6TotalCnt"]=df_comb["RES6LossCntVA"]+df_comb["RES6LossCntDC"]+df_comb["RES6LossCntM"]
################################################################################################
#############Inventory Calculation for IND1,2,3,4,5,6 
df_comb['InventorylossVIND6Py']=df_comb['SqVIND6']*df_comb['IND6InventoryWeigh']*808*df_comb['AreaInundated']*0.02
df_comb['InventorylossVIND5Py']=df_comb['SqVIND5']*df_comb['IND5InventoryWeigh']*459*df_comb['AreaInundated']*0.04
df_comb['InventorylossVIND4Py']=df_comb['SqVIND4']*df_comb['IND4InventoryWeigh']*690*df_comb['AreaInundated']*0.03
df_comb['InventorylossVIND3Py']=df_comb['SqVIND3']*df_comb['IND3InventoryWeigh']*733*df_comb['AreaInundated']*0.05
df_comb['InventorylossVIND1Py']=df_comb['SqVIND1']*df_comb['IND1InventoryWeigh']*750*df_comb['AreaInundated']*0.05
df_comb['InventorylossVIND2Py']=df_comb['SqVIND2']*df_comb['IND2InventoryWeigh']*238*df_comb['AreaInundated']*0.04
###
df_comb['InventorylossMIND6Py']=df_comb['SqMIND6']*df_comb['IND6InventoryWeigh']*808*df_comb['AreaInundated']*0.02
df_comb['InventorylossMIND5Py']=df_comb['SqMIND5']*df_comb['IND5InventoryWeigh']*459*df_comb['AreaInundated']*0.04
df_comb['InventorylossMIND4Py']=df_comb['SqMIND4']*df_comb['IND4InventoryWeigh']*690*df_comb['AreaInundated']*0.03
df_comb['InventorylossMIND3Py']=df_comb['SqMIND3']*df_comb['IND3InventoryWeigh']*733*df_comb['AreaInundated']*0.05
df_comb['InventorylossMIND1Py']=df_comb['SqMIND1']*df_comb['IND1InventoryWeigh']*750*df_comb['AreaInundated']*0.05
df_comb['InventorylossMIND2Py']=df_comb['SqMIND2']*df_comb['IND2InventoryWeigh']*238*df_comb['AreaInundated']*0.04
###
df_comb['InventorylossDCIND6Py']=df_comb['SqDCIND6']*df_comb['IND6InventoryWeigh']*808*df_comb['AreaInundated']*0.02
df_comb['InventorylossDCIND5Py']=df_comb['SqDCIND5']*df_comb['IND5InventoryWeigh']*459*df_comb['AreaInundated']*0.04
df_comb['InventorylossDCIND4Py']=df_comb['SqDCIND4']*df_comb['IND4InventoryWeigh']*690*df_comb['AreaInundated']*0.03
df_comb['InventorylossDCIND3Py']=df_comb['SqDCIND3']*df_comb['IND3InventoryWeigh']*733*df_comb['AreaInundated']*0.05
df_comb['InventorylossDCIND1Py']=df_comb['SqDCIND1']*df_comb['IND1InventoryWeigh']*750*df_comb['AreaInundated']*0.05
df_comb['InventorylossDCIND2Py']=df_comb['SqDCIND2']*df_comb['IND2InventoryWeigh']*238*df_comb['AreaInundated']*0.04
##############################################################################################
df_comb["IND1TotalInv"]=df_comb['InventorylossMIND1Py']+df_comb['InventorylossDCIND1Py']+df_comb['InventorylossVIND1Py']
df_comb["IND2TotalInv"]=df_comb['InventorylossMIND2Py']+df_comb['InventorylossDCIND2Py']+df_comb['InventorylossVIND2Py']
df_comb["IND3TotalInv"]=df_comb['InventorylossMIND3Py']+df_comb['InventorylossDCIND3Py']+df_comb['InventorylossVIND3Py']
df_comb["IND4TotalInv"]=df_comb['InventorylossMIND4Py']+df_comb['InventorylossDCIND4Py']+df_comb['InventorylossVIND4Py']
df_comb["IND5TotalInv"]=df_comb['InventorylossMIND5Py']+df_comb['InventorylossDCIND5Py']+df_comb['InventorylossVIND5Py']
df_comb["IND6TotalInv"]=df_comb['InventorylossMIND6Py']+df_comb['InventorylossDCIND6Py']+df_comb['InventorylossVIND6Py']
##
IND1Inventoryloss=df_comb["IND1TotalInv"].sum()
IND2Inventoryloss=df_comb["IND2TotalInv"].sum()
IND3Inventoryloss=df_comb["IND3TotalInv"].sum()
IND4Inventoryloss=df_comb["IND4TotalInv"].sum()
IND5Inventoryloss=df_comb["IND5TotalInv"].sum()
IND6Inventoryloss=df_comb["IND6TotalInv"].sum()

RES5Contentloss=df_comb["RES5TotalCnt"].sum()
RES6Contentloss=df_comb["RES6TotalCnt"].sum()
RES4Contentloss=df_comb["RES4TotalCnt"].sum()
###
IND1Contentloss=df_comb["IND1TotalCnt"].sum()
IND2Contentloss=df_comb["IND2TotalCnt"].sum()
IND3Contentloss=df_comb["IND3TotalCnt"].sum()
IND4Contentloss=df_comb["IND4TotalCnt"].sum()
IND5Contentloss=df_comb["IND5TotalCnt"].sum()
IND6Contentloss=df_comb["IND6TotalCnt"].sum()
####
RES5loss=df_comb["RES5TotalStr"].sum()
RES6loss=df_comb["RES6TotalStr"].sum()
RES4loss=df_comb["RES4TotalStr"].sum()
###
IND1loss=df_comb["IND1TotalStr"].sum()
IND2loss=df_comb["IND2TotalStr"].sum()
IND3loss=df_comb["IND3TotalStr"].sum()
IND4loss=df_comb["IND4TotalStr"].sum()
IND5loss=df_comb["IND5TotalStr"].sum()
IND6loss=df_comb["IND6TotalStr"].sum()
###################33
print(IND1Inventoryloss*1000)
print(IND2Inventoryloss*1000)
print(IND3Inventoryloss*1000)
print(IND4Inventoryloss*1000)
print(IND5Inventoryloss*1000)
print(IND6Inventoryloss*1000)
df_comb.to_excel(r'D:\SelinaDEM\oye\IND1.xlsx',sheet_name="atam")