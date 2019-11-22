# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:41:35 2019

@author: 90506
"""

import os
import numpy as np
import pandas as pd
import xlrd
import EconomicRESS2
import EconomicRESS
import IncomeLossModule
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t7.xlsx')
df_area=df2.groupby("CensusBlock").apply(lambda dfx: (dfx["km2"].sum()/dfx["BlockArea"]).reset_index(name='AreaInundated'))
df_area=df_area.drop_duplicates(subset='AreaInundated',keep='first')
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
##
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
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureContentByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureContentByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureContentByBlock")
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
####
df_comb['EconomicRES3C1to2NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C1to2WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C1to2WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C3to4WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C3to4WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusNBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusNBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3C5PlusWBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3C5PlusWBContentSlabPostFIRM,axis=1)/100


#######
df87=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentBasementPreFIRMWeight')
df88=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentBasementPostFIRMWeigh')
df89=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentCrawlPreFIRMWeigh')
df90=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentCrawlPostFIRMWeigh')
df91=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentSlabPreFIRMWeigh')
df92=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2NBContentSlabPostFIRMWeigh')
df93=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentBasementPreFIRMWeigh')
df94=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentBasementPostFIRMWeigh')
df95=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentCrawlPreFIRMWeigh')
df96=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentCrawlPostFIRMWeigh')
df97=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentSlabPreFIRMWeigh')
df98=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C1to2WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C1to2WBContentSlabPostFIRMWeigh')
###
df99=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentBasementPreFIRMWeigh')
df101=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentBasementPostFIRMWeigh')
df102=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentCrawlPreFIRMWeigh')
df103=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentCrawlPostFIRMWeigh')
df104=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentSlabPreFIRMWeigh')
df105=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4NBContentSlabPostFIRMWeigh')
df106=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentBasementPreFIRMWeigh')
df107=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentBasementPostFIRMWeigh')
df108=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentCrawlPreFIRMWeigh')
df109=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentCrawlPostFIRMWeigh')
df110=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentSlabPreFIRMWeigh')
df111=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C3to4WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C3to4WBContentSlabPostFIRMWeigh')
###
df112=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentBasementPreFIRMWeigh')
df113=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentBasementPostFIRMWeigh')
df114=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentCrawlPreFIRMWeigh')
df115=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentCrawlPostFIRMWeigh')
df116=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentSlabPreFIRMWeigh')
df117=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusNBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusNBContentSlabPostFIRMWeigh')
df118=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentBasementPreFIRMWeigh')
df119=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentBasementPostFIRMWeigh')
df120=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentCrawlPreFIRMWeigh')
df121=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentCrawlPostFIRMWeigh')
df122=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentSlabPreFIRMWeigh')
df123=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3C5PlusWBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3C5PlusWBContentSlabPostFIRMWeigh')
################################################################################3
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
df_comb["RES3CSmakeRES3C1to2NBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C1to2NBContentBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2NBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C1to2NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2NBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C1to2NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3CSmakeRES3C1to2WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C1to2WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C1to2WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C1to2WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C1to2WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C1to2WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3CSmakeRES3C3to4NBContentContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C3to4NBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4NBContentContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C3to4NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4NBContentContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C3to4NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3CSmakeRES3C3to4WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C3to4WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C3to4WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C3to4WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C3to4WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C3to4WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3CSmakeRES3C5PlusNBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusNBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusNBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusNBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusNBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusNBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusNBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusNBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusNBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3CSmakeRES3C5PlusWBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusWBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusWBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusWBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusWBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusWBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3CSmakeRES3C5PlusWBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3C5PlusWBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3C5PlusWBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###########
df_comb["PRES3C1to2NBC"]=(df_comb["RES3CSmakeRES3C1to2NBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C1to2NBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C1to2NBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3C1to2WBC"]=(df_comb["RES3CSmakeRES3C1to2WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C1to2WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C1to2WBContentSlabContentuctureWeigh"]*Slabfoundation)
##
df_comb["PRES3C3to4NBC"]=(df_comb["RES3CSmakeRES3C3to4NBContentContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C3to4NBContentContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C3to4NBContentContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3C3to4WBC"]=(df_comb["RES3CSmakeRES3C3to4WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C3to4WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C3to4WBContentSlabContentuctureWeigh"]*Slabfoundation)
###
df_comb["PRES3C5plusNBC"]=(df_comb["RES3CSmakeRES3C5PlusNBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C5PlusNBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C5PlusNBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3C5plusWBC"]=(df_comb["RES3CSmakeRES3C5PlusWBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3CSmakeRES3C5PlusWBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3CSmakeRES3C5PlusWBContentSlabContentuctureWeigh"]*Slabfoundation)
####
df_comb["PRES3C1to2C"]=(df_comb["PRES3C1to2NBC"]*Pctwithoutbasement)+(df_comb["PRES3C1to2WBC"]*Pctwbasement)
df_comb["PRES3C3to4C"]=(df_comb["PRES3C3to4NBC"]*Pctwithoutbasement)+(df_comb["PRES3C3to4WBC"]*Pctwbasement)
df_comb["RES3C5plusC"]=(df_comb["PRES3C5plusNBC"]*Pctwithoutbasement)+(df_comb["PRES3C5plusWBC"]*Pctwbasement)
###
df_comb["RES3CC"]=(df_comb["PRES3C1to2C"]*onetotwoStories)+(df_comb["PRES3C3to4C"]*threetofourStories)+(df_comb["RES3C5plusC"]*fiveandmore)
###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
#####
df_comb["RES3CLossContentCDC"]=df_comb["CDCRES3C"]*df_comb["RES3CC"]*df_comb["AreaInundated"]
df_comb["RES3CLossContentCVA"]=df_comb["CVRES3C"]*df_comb["RES3CC"]*df_comb["AreaInundated"]
df_comb["RES3CLossContentCM"]=df_comb["CMRES3C"]*df_comb["RES3CC"]*df_comb["AreaInundated"]
df_comb["RES3CLossContentTotal"]=df_comb["RES3CLossContentCDC"]+df_comb["RES3CLossContentCVA"]+df_comb["RES3CLossContentCM"]
####
PyhtonTotalRES3CContent=df_comb["RES3CLossContentTotal"].sum()
print(PyhtonTotalRES3CContent*1000)