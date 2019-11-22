# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:29:23 2019

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
####
df_comb['EconomicRES3D1to2NBSTRBBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBSTRBBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBSTRBCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBSTRBCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBSTRBSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2NBSTRBSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D1to2WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D1to2WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D3to4WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D3to4WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusNBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusNBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3D5PlusWBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3D5PlusWBSTRSlabPostFIRM,axis=1)/100
####
df124=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBBasementPreFIRMWeight')
df125=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBBasementPostFIRMWeigh')
df126=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBCrawlPreFIRMWeigh')
df127=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBCrawlPostFIRMWeigh')
df128=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBSlabPreFIRMWeigh')
df129=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2NBSTRBSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2NBSTRBSlabPostFIRMWeigh')
df130=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRBasementPreFIRMWeigh')
df131=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRBasementPostFIRMWeigh')
df132=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRCrawlPreFIRMWeigh')
df133=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRCrawlPostFIRMWeigh')
df134=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRSlabPreFIRMWeigh')
df135=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D1to2WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D1to2WBSTRSlabPostFIRMWeigh')
###
df136=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRBasementPreFIRMWeigh')
df137=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRBasementPostFIRMWeigh')
df138=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRCrawlPreFIRMWeigh')
df139=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRCrawlPostFIRMWeigh')
df140=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRSlabPreFIRMWeigh')
df141=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4NBSTRSlabPostFIRMWeigh')
df142=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRBasementPreFIRMWeigh')
df143=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRBasementPostFIRMWeigh')
df144=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRCrawlPreFIRMWeigh')
df145=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRCrawlPostFIRMWeigh')
df146=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRSlabPreFIRMWeigh')
df147=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D3to4WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D3to4WBSTRSlabPostFIRMWeigh')
###
df148=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRBasementPreFIRMWeigh')
df149=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRBasementPostFIRMWeigh')
df150=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRCrawlPreFIRMWeigh')
df151=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRCrawlPostFIRMWeigh')
df152=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRSlabPreFIRMWeigh')
df153=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusNBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusNBSTRSlabPostFIRMWeigh')
df154=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRBasementPreFIRMWeigh')
df155=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRBasementPostFIRMWeigh')
df156=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRCrawlPreFIRMWeigh')
df157=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRCrawlPostFIRMWeigh')
df158=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRSlabPreFIRMWeigh')
df159=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3D5PlusWBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3D5PlusWBSTRSlabPostFIRMWeigh')
###
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
###
df_comb['RES3DSmakeRES3D1to2NBSTRBasementPreFIRMWeight']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBBasementPreFIRMWeight,axis=1)
df_comb['RES3DSmakeRES3D1to2NBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2NBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2NBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2NBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBSlabPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2NBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2NBSTRBSlabPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D1to2WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D1to2WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4NBSTRSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4NBSTRSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D3to4WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D3to4WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusNBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusNBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusWBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusWBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusWBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusWBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3DSmakeRES3D5PlusWBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRSlabPreFIRMWeigh,axis=1)###
df_comb['RES3DSmakeRES3D5PlusWBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3DSmakeRES3D5PlusWBSTRSlabPostFIRMWeigh,axis=1)
####
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
####
df_comb["RES3DSmakeRES3D1to2NBSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2NBSTRBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2NBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2NBSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2NBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2NBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2NBSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2NBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2NBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3DSmakeRES3D1to2WBSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2WBSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D1to2WBSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D1to2WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D1to2WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3DSmakeRES3D3to4NBSTRSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4NBSTRSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4NBSTRSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4NBSTRSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4NBSTRSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4NBSTRSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4NBSTRSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4NBSTRSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4NBSTRSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3DSmakeRES3D3to4WBSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4WBSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D3to4WBSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D3to4WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D3to4WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3DSmakeRES3D5PlusNBSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusNBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusNBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusNBSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusNBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusNBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusNBSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusNBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusNBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3DSmakeRES3D5PlusWBSTRBasementStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusWBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusWBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusWBSTRCrawlStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusWBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusWBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3DSmakeRES3D5PlusWBSTRSlabStructureWeigh"]=((df_comb['RES3DSmakeRES3D5PlusWBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3DSmakeRES3D5PlusWBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES3D1to2NB"]=(df_comb["RES3DSmakeRES3D1to2NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D1to2NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D1to2NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3D1to2WB"]=(df_comb["RES3DSmakeRES3D1to2WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D1to2WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D1to2WBSTRSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES3D3to4NB"]=(df_comb["RES3DSmakeRES3D3to4NBSTRSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D3to4NBSTRSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D3to4NBSTRSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3D3to4WB"]=(df_comb["RES3DSmakeRES3D3to4WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D3to4WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D3to4WBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3D5plusNB"]=(df_comb["RES3DSmakeRES3D5PlusNBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D5PlusNBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D5PlusNBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3D5plusWB"]=(df_comb["RES3DSmakeRES3D5PlusWBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3DSmakeRES3D5PlusWBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3DSmakeRES3D5PlusWBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3D1to2"]=(df_comb["PRES3D1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3D1to2WB"]*Pctwbasement)
df_comb["PRES3D3to4"]=(df_comb["PRES3D3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3D3to4WB"]*Pctwbasement)
df_comb["RES3D5plus"]=(df_comb["PRES3D5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3D5plusWB"]*Pctwbasement)
###
df_comb["RES3D"]=(df_comb["PRES3D1to2"]*onetotwoStories)+(df_comb["PRES3D3to4"]*threetofourStories)+(df_comb["RES3D5plus"]*fiveandmore)
###
def hellRES3D(df_comb):
    if (df_comb['RES3D']>0.5):
        return 1
    elif (df_comb['RES3D']<0):
        return 0
    else:
        return df_comb['RES3D']
df_comb["RES3D"]=df_comb.apply(hellRES3D,axis=1)
###
####
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)

df_comb["RES3DLossStrDC"]=df_comb["DCRES3D"]*df_comb["RES3D"]*df_comb["AreaInundated"]
df_comb["RES3DLossStrVA"]=df_comb["VRES3D"]*df_comb["RES3D"]*df_comb["AreaInundated"]
df_comb["RES3DLossStrM"]=df_comb["MRES3D"]*df_comb["RES3D"]*df_comb["AreaInundated"]
df_comb["RES3DLossStrTotal"]=df_comb["RES3DLossStrDC"]+df_comb["RES3DLossStrVA"]+df_comb["RES3DLossStrM"]
###
PyhtonTotalRES3DContent=df_comb["RES3DLossStrTotal"].sum()
print(PyhtonTotalRES3DContent*1000)