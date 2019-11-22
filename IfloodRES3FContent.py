# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:27:40 2019

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
df_comb['EconomicRES3F1to2NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBContentSlabPostFIRM,axis=1)/100
####
df160=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentBasementPreFIRMWeight')
df161=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentBasementPostFIRMWeigh')
df162=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentCrawlPreFIRMWeigh')
df163=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentCrawlPostFIRMWeigh')
df164=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentSlabPreFIRMWeigh')
df165=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBContentSlabPostFIRMWeigh')
df166=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentBasementPreFIRMWeigh')
df167=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentBasementPostFIRMWeigh')
df168=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentCrawlPreFIRMWeigh')
df169=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentCrawlPostFIRMWeigh')
df170=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentSlabPreFIRMWeigh')
df171=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBContentSlabPostFIRMWeigh')
###
df172=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentBasementPreFIRMWeigh')
df173=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentBasementPostFIRMWeigh')
df174=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentCrawlPreFIRMWeigh')
df175=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentCrawlPostFIRMWeigh')
df176=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentSlabPreFIRMWeigh')
df177=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBContentSlabPostFIRMWeigh')
df178=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentBasementPreFIRMWeigh')
df179=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentBasementPostFIRMWeigh')
df180=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentCrawlPreFIRMWeigh')
df181=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentCrawlPostFIRMWeigh')
df182=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentSlabPreFIRMWeigh')
df183=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBContentSlabPostFIRMWeigh')
###
df184=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentBasementPreFIRMWeigh')
df185=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentBasementPostFIRMWeigh')
df186=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentCrawlPreFIRMWeigh')
df187=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentCrawlPostFIRMWeigh')
df188=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentSlabPreFIRMWeigh')
df189=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBContentSlabPostFIRMWeigh')
df190=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentBasementPreFIRMWeigh')
df191=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentBasementPostFIRMWeigh')
df192=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentCrawlPreFIRMWeigh')
df193=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentCrawlPostFIRMWeigh')
df194=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentSlabPreFIRMWeigh')
df195=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBContentSlabPostFIRMWeigh')
####
df_comb=pd.merge(df_comb,df160,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df161,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df162,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df163,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df164,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df165,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df166,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df167,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df168,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df169,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df170,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df171,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df172,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df173,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df174,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df175,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df176,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df177,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df178,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df179,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df180,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df181,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df182,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df183,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df184,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df185,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df186,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df187,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df188,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df189,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df190,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df191,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df192,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df193,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df194,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df195,on='CensusBlock',how='left')
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

df_comb["RES3FSmakeRES3F1to2NBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F1to2NBContentBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2NBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F1to2NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2NBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F1to2NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3FSmakeRES3F1to2WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F1to2WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F1to2WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F1to2WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F1to2WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3FSmakeRES3F3to4NBContentContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F3to4NBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4NBContentContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F3to4NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4NBContentContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F3to4NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3FSmakeRES3F3to4WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F3to4WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F3to4WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F3to4WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F3to4WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3FSmakeRES3F5PlusNBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusNBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusNBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusNBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusNBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusNBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusNBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusNBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusNBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3FSmakeRES3F5PlusWBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusWBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusWBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusWBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusWBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusWBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusWBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3F5PlusWBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3F5PlusWBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["PRES3F1to2NBC"]=(df_comb["RES3FSmakeRES3F1to2NBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F1to2NBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F1to2NBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3F1to2WBC"]=(df_comb["RES3FSmakeRES3F1to2WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F1to2WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F1to2WBContentSlabContentuctureWeigh"]*Slabfoundation)
##
df_comb["PRES3F3to4NBC"]=(df_comb["RES3FSmakeRES3F3to4NBContentContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F3to4NBContentContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F3to4NBContentContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3F3to4WBC"]=(df_comb["RES3FSmakeRES3F3to4WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F3to4WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F3to4WBContentSlabContentuctureWeigh"]*Slabfoundation)
###
df_comb["PRES3F5plusNBC"]=(df_comb["RES3FSmakeRES3F5PlusNBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F5PlusNBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F5PlusNBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3F5plusWBC"]=(df_comb["RES3FSmakeRES3F5PlusWBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F5PlusWBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F5PlusWBContentSlabContentuctureWeigh"]*Slabfoundation)
####
df_comb["PRES3F1to2C"]=(df_comb["PRES3F1to2NBC"]*Pctwithoutbasement)+(df_comb["PRES3F1to2WBC"]*Pctwbasement)
df_comb["PRES3F3to4C"]=(df_comb["PRES3F3to4NBC"]*Pctwithoutbasement)+(df_comb["PRES3F3to4WBC"]*Pctwbasement)
df_comb["RES3F5plusC"]=(df_comb["PRES3F5plusNBC"]*Pctwithoutbasement)+(df_comb["PRES3F5plusWBC"]*Pctwbasement)
###
df_comb["RES3FC"]=(df_comb["PRES3F1to2C"]*onetotwoStories)+(df_comb["PRES3F3to4C"]*threetofourStories)+(df_comb["RES3F5plusC"]*fiveandmore)
###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
###
df_comb["RES3FLossContentCDC"]=df_comb["CDCRES3E"]*df_comb["RES3FC"]*df_comb["AreaInundated"]
df_comb["RES3FLossContentCVA"]=df_comb["CVRES3E"]*df_comb["RES3FC"]*df_comb["AreaInundated"]
df_comb["RES3FLossContentCM"]=df_comb["CMRES3E"]*df_comb["RES3FC"]*df_comb["AreaInundated"]
df_comb["RES3FLossContentTotal"]=df_comb["RES3FLossContentCDC"]+df_comb["RES3FLossContentCVA"]+df_comb["RES3FLossContentCM"]
###
PyhtonTotalRES3EContent=df_comb["RES3FLossContentTotal"].sum()
print(PyhtonTotalRES3EContent*1000)