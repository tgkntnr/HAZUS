# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:56:38 2019

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
#######
df_comb['EconomicRES3D1to2NBContentBBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBContentBBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBContentBCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBContentBCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBContentBSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBContentBSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBContentSlabPostFIRM,axis=1)/100
###########
df124=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBBasementPreFIRMWeight')
df125=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBBasementPostFIRMWeigh')
df126=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBCrawlPreFIRMWeigh')
df127=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBCrawlPostFIRMWeigh')
df128=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBSlabPreFIRMWeigh')
df129=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBContentBSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBContentBSlabPostFIRMWeigh')
df130=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentBasementPreFIRMWeigh')
df131=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentBasementPostFIRMWeigh')
df132=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentCrawlPreFIRMWeigh')
df133=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentCrawlPostFIRMWeigh')
df134=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentSlabPreFIRMWeigh')
df135=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBContentSlabPostFIRMWeigh')
###
df136=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentBasementPreFIRMWeigh')
df137=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentBasementPostFIRMWeigh')
df138=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentCrawlPreFIRMWeigh')
df139=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentCrawlPostFIRMWeigh')
df140=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentSlabPreFIRMWeigh')
df141=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBContentSlabPostFIRMWeigh')
df142=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentBasementPreFIRMWeigh')
df143=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentBasementPostFIRMWeigh')
df144=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentCrawlPreFIRMWeigh')
df145=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentCrawlPostFIRMWeigh')
df146=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentSlabPreFIRMWeigh')
df147=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBContentSlabPostFIRMWeigh')
###
df148=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentBasementPreFIRMWeigh')
df149=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentBasementPostFIRMWeigh')
df150=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentCrawlPreFIRMWeigh')
df151=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentCrawlPostFIRMWeigh')
df152=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentSlabPreFIRMWeigh')
df153=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBContentSlabPostFIRMWeigh')
df154=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentBasementPreFIRMWeigh')
df155=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentBasementPostFIRMWeigh')
df156=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentCrawlPreFIRMWeigh')
df157=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentCrawlPostFIRMWeigh')
df158=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentSlabPreFIRMWeigh')
df159=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBContentSlabPostFIRMWeigh')
####
df_comb=pd.merge(df_comb,df124,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df125,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df126,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df127,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df128,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df129,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df130,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df131,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df132,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df133,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df134,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df135,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df136,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df137,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df138,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df139,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df140,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df141,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df142,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df143,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df144,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df145,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df146,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df147,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df148,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df149,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df150,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df151,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df152,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df153,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df154,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df155,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df156,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df157,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df158,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df159,on='CensusBlock',how='left')
########
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
#####
df_comb["RES3DSmakeRES3D1to2NBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D1to2NBContentBBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2NBContentBBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2NBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D1to2NBContentBCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2NBContentBCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2NBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D1to2NBContentBSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2NBContentBSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3DSmakeRES3D1to2WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D1to2WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D1to2WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D1to2WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D1to2WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3DSmakeRES3D3to4NBContentContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D3to4NBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4NBContentContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D3to4NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4NBContentContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D3to4NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3DSmakeRES3D3to4WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D3to4WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D3to4WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D3to4WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D3to4WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3DSmakeRES3D5PlusNBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusNBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusNBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusNBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusNBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusNBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusNBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusNBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusNBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3DSmakeRES3D5PlusWBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusWBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusWBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusWBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusWBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusWBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusWBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3D5PlusWBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3D5PlusWBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
#####
df_comb["PRES3D1to2NBC"]=(df_comb["RES3DSmakeRES3D1to2NBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D1to2NBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D1to2NBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3D1to2WBC"]=(df_comb["RES3DSmakeRES3D1to2WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D1to2WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D1to2WBContentSlabContentuctureWeigh"]*Slabfoundation)
##
df_comb["PRES3D3to4NBC"]=(df_comb["RES3DSmakeRES3D3to4NBContentContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D3to4NBContentContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D3to4NBContentContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3D3to4WBC"]=(df_comb["RES3DSmakeRES3D3to4WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D3to4WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D3to4WBContentSlabContentuctureWeigh"]*Slabfoundation)
###
df_comb["PRES3D5plusNBC"]=(df_comb["RES3DSmakeRES3D5PlusNBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D5PlusNBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D5PlusNBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3D5plusWBC"]=(df_comb["RES3DSmakeRES3D5PlusWBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D5PlusWBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D5PlusWBContentSlabContentuctureWeigh"]*Slabfoundation)
####
df_comb["PRES3D1to2C"]=(df_comb["PRES3D1to2NBC"]*Pctwithoutbasement)+(df_comb["PRES3D1to2WBC"]*Pctwbasement)
df_comb["PRES3D3to4C"]=(df_comb["PRES3D3to4NBC"]*Pctwithoutbasement)+(df_comb["PRES3D3to4WBC"]*Pctwbasement)
df_comb["RES3D5plusC"]=(df_comb["PRES3D5plusNBC"]*Pctwithoutbasement)+(df_comb["PRES3D5plusWBC"]*Pctwbasement)
##########
df_comb["RES3DC"]=(df_comb["PRES3D1to2C"]*onetotwoStories)+(df_comb["PRES3D3to4C"]*threetofourStories)+(df_comb["RES3D5plusC"]*fiveandmore)
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
###
df_comb["RES3DLossContentCDC"]=df_comb["CDCRES3D"]*df_comb["RES3DC"]*df_comb["AreaInundated"]
df_comb["RES3DLossContentCVA"]=df_comb["CVRES3D"]*df_comb["RES3DC"]*df_comb["AreaInundated"]
df_comb["RES3DLossContentCM"]=df_comb["CMRES3D"]*df_comb["RES3DC"]*df_comb["AreaInundated"]
df_comb["RES3DLossContentTotal"]=df_comb["RES3DLossContentCDC"]+df_comb["RES3DLossContentCVA"]+df_comb["RES3DLossContentCM"]
###
PyhtonTotalRES3DContent=df_comb["RES3DLossContentTotal"].sum()
print(PyhtonTotalRES3DContent*1000)