# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:09:53 2019

@author: 90506
"""

import os
import numpy as np
import pandas as pd
import xlrd
import EconomicRESS2
import EconomicRESS
import IncomeLossModule
import pointfive
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t7.xlsx')
df_area=df2.groupby("CensusBlock").apply(lambda dfx: (dfx["km2"].sum()/dfx["BlockArea"]).reset_index(name='AreaInundated'))
df_area=df_area.drop_duplicates(subset='AreaInundated',keep='first')
###
Basementfoundation=0.23
Crawlfoundation=0.35
Slabfoundation=0.42
###
#SingleFamily
Pctwbasement=0.19
Pctwithoutbasement=0.81
OneStory=0.66
TwoStory=0.32
ThreeStory=0.01
SplitLevel=0.01
###
onetotwoStories=0.69
threetofourStories=0.26
fiveandmore=0.05
###
df2["frstRES4"]=1
#Water depth-first floor height=effective flood depth for COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,COM10,RES4,RES5,RES6,IND1,IND2,IND3,IND4,IND5,IND6
df2["Finalwaterlevel"]=df2["WaterLevelftA"]-df2["frstRES4"]#Final water level
df2["frstRES1BasementPreFIRM"]=4
df2["frstRES1BasementPostFIRM"]=4
df2["frstRES1CrawlPreFIRM"]=3
df2["frstRES1CrawlPostFIRM"]=4
df2["frstRES1SlabPreFIRM"]=1
df2["frstRES1SlabPostFIRM"]=1
df2["Finalwaterlevel"]=df2["WaterLevelftA"]-df2["frstRES4"]#ILK KISMI BIR KERE DAHA WATERLEVEF
#Water depth- first floor height=effective flood depth for RES1,RES2,RES3A,RES3B,RES3C,RES3D,RES3E,RES3F
df2["FinalwaterlevelRES1BasementPreFIRM"]=df2["WaterLevelftA"]-df2["frstRES1BasementPreFIRM"]
df2["FinalwaterlevelRES1BasementPostFIRM"]=df2["WaterLevelftA"]-df2["frstRES1BasementPostFIRM"]
df2["FinalwaterlevelRES1CrawlPreFIRM"]=df2["WaterLevelftA"]-df2["frstRES1CrawlPreFIRM"]
df2["FinalwaterlevelRES1CrawlPostFIRM"]=df2["WaterLevelftA"]-df2["frstRES1CrawlPostFIRM"]
df2["FinalwaterlevelRES1SlabPreFIRM"]=df2["WaterLevelftA"]-df2["frstRES1SlabPreFIRM"]
df2["FinalwaterlevelRES1SlabPostFIRM"]=df2["WaterLevelftA"]-df2["frstRES1SlabPostFIRM"]
########### 
dpo=pd.read_excel(r'D:\SelinaDEM\oye3\Mean.xlsx')
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureByBlock")
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
###
###RES3C
df_comb['EconomicRES3C1to2NBSTRBBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBSTRBBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBSTRBCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBSTRBCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBSTRBSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBSTRBSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBSTRBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBSTRSlabPostFIRM,axis=1)/100
###
df87=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBBasementPreFIRMWeight')
df88=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBBasementPostFIRMWeigh')
df89=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBCrawlPreFIRMWeigh')
df90=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBCrawlPostFIRMWeigh')
df91=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBSlabPreFIRMWeigh')
df92=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBSTRBSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBSTRBSlabPostFIRMWeigh')
df93=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRBasementPreFIRMWeigh')
df94=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRBasementPostFIRMWeigh')
df95=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRCrawlPreFIRMWeigh')
df96=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRCrawlPostFIRMWeigh')
df97=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRSlabPreFIRMWeigh')
df98=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBSTRSlabPostFIRMWeigh')
###
df99=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRBasementPreFIRMWeigh')
df101=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRBasementPostFIRMWeigh')
df102=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRCrawlPreFIRMWeigh')
df103=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRCrawlPostFIRMWeigh')
df104=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRSlabPreFIRMWeigh')
df105=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBSTRSlabPostFIRMWeigh')
df106=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRBasementPreFIRMWeigh')
df107=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRBasementPostFIRMWeigh')
df108=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRCrawlPreFIRMWeigh')
df109=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRCrawlPostFIRMWeigh')
df110=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRSlabPreFIRMWeigh')
df111=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBSTRSlabPostFIRMWeigh')
###
df112=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRBasementPreFIRMWeigh')
df113=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRBasementPostFIRMWeigh')
df114=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRCrawlPreFIRMWeigh')
df115=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRCrawlPostFIRMWeigh')
df116=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRSlabPreFIRMWeigh')
df117=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBSTRSlabPostFIRMWeigh')
df118=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRBasementPreFIRMWeigh')
df119=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRBasementPostFIRMWeigh')
df120=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRCrawlPreFIRMWeigh')
df121=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRCrawlPostFIRMWeigh')
df122=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRSlabPreFIRMWeigh')
df123=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBSTRSlabPostFIRMWeigh')
####
df_comb=pd.merge(df_comb,df87,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df88,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df89,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df90,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df91,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df92,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df93,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df94,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df95,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df96,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df97,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df98,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df99,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df101,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df102,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df103,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df104,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df105,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df106,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df107,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df108,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df109,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df110,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df111,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df112,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df113,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df114,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df115,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df116,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df117,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df118,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df119,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df120,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df121,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df122,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df123,on='CensusBlock',how='left')
####
df_comb['RES3CSmakeRES3C1to2NBSTRBasementPreFIRMWeight']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBBasementPreFIRMWeight,axis=1)
df_comb['RES3CSmakeRES3C1to2NBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2NBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2NBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2NBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBSlabPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2NBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2NBSTRBSlabPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C1to2WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C1to2WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4NBSTRSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4NBSTRSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C3to4WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C3to4WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusNBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusNBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusWBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusWBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusWBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusWBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3CSmakeRES3C5PlusWBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRSlabPreFIRMWeigh,axis=1)###
df_comb['RES3CSmakeRES3C5PlusWBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3CSmakeRES3C5PlusWBSTRSlabPostFIRMWeigh,axis=1)
###
def PostFIRM(df_comb):
    if (df_comb["MedianYearBuilt"]>=1968):
        return 1
    else:
        return 0

def PreFIRM(df_comb):
    if (df_comb["MedianYearBuilt"]<1968):
        return 1
    else:
        return 0
###
df_comb["PREFIRM"]=df_comb.apply(PreFIRM,axis=1)
df_comb["POSTFIRM"]=df_comb.apply(PostFIRM,axis=1)
###
df_comb["RES3CSmakeRES3C1to2NBSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2NBSTRBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2NBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2NBSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2NBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2NBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2NBSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2NBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2NBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3CSmakeRES3C1to2WBSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2WBSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2WBSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C1to2WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C1to2WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3CSmakeRES3C3to4NBSTRSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4NBSTRSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4NBSTRSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4NBSTRSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4NBSTRSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4NBSTRSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4NBSTRSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4NBSTRSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4NBSTRSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3CSmakeRES3C3to4WBSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4WBSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4WBSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C3to4WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C3to4WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3CSmakeRES3C5PlusNBSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusNBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusNBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusNBSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusNBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusNBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusNBSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusNBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusNBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3CSmakeRES3C5PlusWBSTRBasementStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusWBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusWBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusWBSTRCrawlStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusWBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusWBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusWBSTRSlabStructureWeigh"]=((df_comb['RES3CSmakeRES3C5PlusWBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3CSmakeRES3C5PlusWBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES3C1to2NB"]=(df_comb["RES3CSmakeRES3C1to2NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C1to2NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C1to2NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3C1to2WB"]=(df_comb["RES3CSmakeRES3C1to2WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C1to2WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C1to2WBSTRSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES3C3to4NB"]=(df_comb["RES3CSmakeRES3C3to4NBSTRSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C3to4NBSTRSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C3to4NBSTRSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3C3to4WB"]=(df_comb["RES3CSmakeRES3C3to4WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C3to4WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C3to4WBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3C5plusNB"]=(df_comb["RES3CSmakeRES3C5PlusNBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C5PlusNBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C5PlusNBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3C5plusWB"]=(df_comb["RES3CSmakeRES3C5PlusWBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C5PlusWBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C5PlusWBSTRSlabStructureWeigh"]*Slabfoundation)
####
df_comb["PRES3C1to2"]=(df_comb["PRES3C1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3C1to2WB"]*Pctwbasement)
df_comb["PRES3C3to4"]=(df_comb["PRES3C3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3C3to4WB"]*Pctwbasement)
df_comb["RES3C5plus"]=(df_comb["PRES3C5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3C5plusWB"]*Pctwbasement)
###
df_comb["RES3C"]=(df_comb["PRES3C1to2"]*onetotwoStories)+(df_comb["PRES3C3to4"]*threetofourStories)+(df_comb["RES3C5plus"]*fiveandmore)
####
def hellRES3C(df_comb):
    if (df_comb['RES3C']>0.5):
        return 1
    elif (df_comb['RES3C']<0):
        return 0
    else:
        return df_comb['RES3C']
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
df_comb["RES3CLossStrDC"]=df_comb["DCRES3C"]*df_comb["RES3C"]*df_comb["AreaInundated"]
df_comb["RES3CLossStrVA"]=df_comb["VRES3C"]*df_comb["RES3C"]*df_comb["AreaInundated"]
df_comb["RES3CLossStrM"]=df_comb["MRES3C"]*df_comb["RES3C"]*df_comb["AreaInundated"]
df_comb["RES3CLossStrTotal"]=df_comb["RES3CLossStrDC"]+df_comb["RES3CLossStrVA"]+df_comb["RES3CLossStrM"]

PyhtonTotalRES3CContent=df_comb["RES3CLossStrTotal"].sum()
print(PyhtonTotalRES3CContent*1000)