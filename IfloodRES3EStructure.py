# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:45:42 2019

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
df_comb['EconomicRES3E1to2NBSTRBBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2NBSTRBBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E1to2NBSTRBCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2NBSTRBCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E1to2NBSTRBSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2NBSTRBSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2NBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E1to2WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E1to2WBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4NBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E3to4WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E3to4WBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E5PlusNBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusWBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3E35WBPlusSlabPostFIRM,axis=1)/100
####
df160=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBBasementPreFIRMWeight')
df161=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBBasementPostFIRMWeigh')
df162=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBCrawlPreFIRMWeigh')
df163=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBCrawlPostFIRMWeigh')
df164=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBSlabPreFIRMWeigh')
df165=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2NBSTRBSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2NBSTRBSlabPostFIRMWeigh')
df166=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRBasementPreFIRMWeigh')
df167=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRBasementPostFIRMWeigh')
df168=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRCrawlPreFIRMWeigh')
df169=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRCrawlPostFIRMWeigh')
df170=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRSlabPreFIRMWeigh')
df171=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E1to2WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E1to2WBSTRSlabPostFIRMWeigh')
###
df172=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRESE3to4NBSTRBasementPreFIRMWeigh')
df173=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4NBSTRBasementPostFIRMWeigh')
df174=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4NBSTRCrawlPreFIRMWeigh')
df175=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4NBSTRCrawlPostFIRMWeigh')
df176=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4NBSTRSlabPreFIRMWeigh')
df177=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4NBSTRSlabPostFIRMWeigh')
df178=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRBasementPreFIRMWeigh')
df179=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRBasementPostFIRMWeigh')
df180=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRCrawlPreFIRMWeigh')
df181=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRCrawlPostFIRMWeigh')
df182=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRSlabPreFIRMWeigh')
df183=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E3to4WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E3to4WBSTRSlabPostFIRMWeigh')
###
df184=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRBasementPreFIRMWeigh')
df185=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRBasementPostFIRMWeigh')
df186=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRCrawlPreFIRMWeigh')
df187=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRCrawlPostFIRMWeigh')
df188=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRSlabPreFIRMWeigh')
df189=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusNBSTRSlabPostFIRMWeigh')
df190=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRBasementPreFIRMWeigh')
df191=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRBasementPostFIRMWeigh')
df192=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRCrawlPreFIRMWeigh')
df193=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRCrawlPostFIRMWeigh')
df194=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRSlabPreFIRMWeigh')
df195=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusWBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3E5PlusWBSTRSlabPostFIRMWeigh')
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
####
df_comb['RES3ESmakeRES3E1to2NBSTRBasementPreFIRMWeight']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBBasementPreFIRMWeight,axis=1)
df_comb['RES3ESmakeRES3E1to2NBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2NBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2NBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2NBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBSlabPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2NBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2NBSTRBSlabPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E1to2WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E1to2WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4NBSTRSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4NBSTRSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E3to4WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E3to4WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusNBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusNBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusWBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusWBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusWBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusWBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3ESmakeRES3E5PlusWBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRSlabPreFIRMWeigh,axis=1)###
df_comb['RES3ESmakeRES3E5PlusWBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3ESmakeRES3E5PlusWBSTRSlabPostFIRMWeigh,axis=1)
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
df_comb["RES3ESmakeRES3E1to2NBSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2NBSTRBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2NBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E1to2NBSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2NBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2NBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E1to2NBSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2NBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2NBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3ESmakeRES3E1to2WBSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E1to2WBSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E1to2WBSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E1to2WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E1to2WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ESmakeRES3E3to4NBSTRSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4NBSTRSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4NBSTRSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E3to4NBSTRSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4NBSTRSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4NBSTRSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E3to4NBSTRSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4NBSTRSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4NBSTRSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ESmakeRES3E3to4WBSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E3to4WBSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E3to4WBSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E3to4WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E3to4WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ESmakeRES3E5PlusNBSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusNBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusNBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E5PlusNBSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusNBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusNBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E5PlusNBSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusNBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusNBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ESmakeRES3E5PlusWBSTRBasementStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusWBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusWBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E5PlusWBSTRCrawlStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusWBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusWBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ESmakeRES3E5PlusWBSTRSlabStructureWeigh"]=((df_comb['RES3ESmakeRES3E5PlusWBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ESmakeRES3E5PlusWBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
##
df_comb["PRES3E1to2NB"]=(df_comb["RES3ESmakeRES3E1to2NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E1to2NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E1to2NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3E1to2WB"]=(df_comb["RES3ESmakeRES3E1to2WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E1to2WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E1to2WBSTRSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES3E3to4NB"]=(df_comb["RES3ESmakeRES3E3to4NBSTRSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E3to4NBSTRSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E3to4NBSTRSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3E3to4WB"]=(df_comb["RES3ESmakeRES3E3to4WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E3to4WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E3to4WBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3E5plusNB"]=(df_comb["RES3ESmakeRES3E5PlusNBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E5PlusNBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E5PlusNBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3E5plusWB"]=(df_comb["RES3ESmakeRES3E5PlusWBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ESmakeRES3E5PlusWBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ESmakeRES3E5PlusWBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3E1to2"]=(df_comb["PRES3E1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3E1to2WB"]*Pctwbasement)
df_comb["PRES3E3to4"]=(df_comb["PRES3E3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3E3to4WB"]*Pctwbasement)
df_comb["RES3E5plus"]=(df_comb["PRES3E5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3E5plusWB"]*Pctwbasement)
####
df_comb["RES3E"]=(df_comb["PRES3E1to2"]*onetotwoStories)+(df_comb["PRES3E3to4"]*threetofourStories)+(df_comb["RES3E5plus"]*fiveandmore)

def hellRES3E(df_comb):
    if (df_comb['RES3E']>0.5):
        return 1
    elif (df_comb['RES3E']<0):
        return 0
    else:
        return df_comb['RES3E']
df_comb["RES3E"]=df_comb.apply(hellRES3E,axis=1)
###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)

df_comb["RES3ELossStrDC"]=df_comb["DCRES3E"]*df_comb["RES3E"]*df_comb["AreaInundated"]
df_comb["RES3ELossStrVA"]=df_comb["VRES3E"]*df_comb["RES3E"]*df_comb["AreaInundated"]
df_comb["RES3ELossStrM"]=df_comb["MRES3E"]*df_comb["RES3E"]*df_comb["AreaInundated"]
df_comb["RES3ELossStrTotal"]=df_comb["RES3ELossStrDC"]+df_comb["RES3ELossStrVA"]+df_comb["RES3ELossStrM"]

PyhtonTotalRES3EContent=df_comb["RES3ELossStrTotal"].sum()
print(PyhtonTotalRES3EContent*1000)
