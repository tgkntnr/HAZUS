# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:04:22 2019

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
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t6.xlsx')
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
df_comb['EconomicRES3B1to2NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBSTRSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBSTRSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBSTRSlabPostFIRM,axis=1)/100
####
df51=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRBasementPreFIRMWeight')
df52=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRBasementPostFIRMWeigh')
df53=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRCrawlPreFIRMWeigh')
df54=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRCrawlPostFIRMWeigh')
df55=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRSlabPreFIRMWeigh')
df56=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBSTRSlabPostFIRMWeigh')
df57=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRBasementPreFIRMWeigh')
df58=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRBasementPostFIRMWeigh')
df59=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRCrawlPreFIRMWeigh')
df60=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRCrawlPostFIRMWeigh')
df61=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRSlabPreFIRMWeigh')
df62=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBSTRSlabPostFIRMWeigh')
###
df63=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRBasementPreFIRMWeigh')
df64=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRBasementPostFIRMWeigh')
df65=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRCrawlPreFIRMWeigh')
df66=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRCrawlPostFIRMWeigh')
df67=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRSlabPreFIRMWeigh')
df68=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBSTRSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBSTRSTRSlabPostFIRMWeigh')
df69=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRBasementPreFIRMWeigh')
df70=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRBasementPostFIRMWeigh')
df71=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRCrawlPreFIRMWeigh')
df72=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRCrawlPostFIRMWeigh')
df73=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRSlabPreFIRMWeigh')
df74=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBSTRSlabPostFIRMWeigh')
###
df75=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRBasementPreFIRMWeigh')
df76=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRBasementPostFIRMWeigh')
df77=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRCrawlPreFIRMWeigh')
df78=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRCrawlPostFIRMWeigh')
df79=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRSlabPreFIRMWeigh')
df80=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBSTRSlabPostFIRMWeigh')
df81=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRBasementPreFIRMWeigh')
df82=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRBasementPostFIRMWeigh')
df83=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRCrawlPreFIRMWeigh')
df84=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRCrawlPostFIRMWeigh')
df85=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRSlabPreFIRMWeigh')
df86=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBSTRSlabPostFIRMWeigh')
#####
df_comb=pd.merge(df_comb,df51,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df52,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df53,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df54,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df55,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df56,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df57,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df58,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df59,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df60,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df61,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df62,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df63,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df64,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df65,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df66,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df67,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df68,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df69,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df70,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df71,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df72,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df73,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df74,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df75,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df76,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df77,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df78,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df79,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df80,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df81,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df82,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df83,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df84,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df85,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df86,on='CensusBlock',how='left')
###
df_comb['RES3BSmakeRES3B1to2NBSTRBasementPreFIRMWeight']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRBasementPreFIRMWeight,axis=1)
df_comb['RES3BSmakeRES3B1to2NBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2NBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2NBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2NBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2NBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2NBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B1to2WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B1to2WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4NBSTRSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4NBSTRSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B3to4WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B3to4WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusNBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusNBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusWBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusWBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusWBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusWBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3BSmakeRES3B5PlusWBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRSlabPreFIRMWeigh,axis=1)###
df_comb['RES3BSmakeRES3B5PlusWBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3BSmakeRES3B5PlusWBSTRSlabPostFIRMWeigh,axis=1)
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
df_comb["RES3BSmakeRES3B1to2NBSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2NBSTRBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2NBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2NBSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2NBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2NBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2NBSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2NBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2NBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3BSmakeRES3B1to2WBSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2WBSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2WBSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B1to2WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B1to2WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3BSmakeRES3B3to4NBSTRSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4NBSTRSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4NBSTRSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4NBSTRSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4NBSTRSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4NBSTRSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4NBSTRSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4NBSTRSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4NBSTRSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3BSmakeRES3B3to4WBSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4WBSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4WBSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B3to4WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B3to4WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3BSmakeRES3B5PlusNBSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusNBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusNBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusNBSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusNBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusNBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusNBSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusNBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusNBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3BSmakeRES3B5PlusWBSTRBasementStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusWBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusWBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusWBSTRCrawlStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusWBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusWBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusWBSTRSlabStructureWeigh"]=((df_comb['RES3BSmakeRES3B5PlusWBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3BSmakeRES3B5PlusWBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["PRES3B1to2NB"]=(df_comb["RES3BSmakeRES3B1to2NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B1to2NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B1to2NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3B1to2WB"]=(df_comb["RES3BSmakeRES3B1to2WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B1to2WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B1to2WBSTRSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES3B3to4NB"]=(df_comb["RES3BSmakeRES3B3to4NBSTRSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B3to4NBSTRSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B3to4NBSTRSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3B3to4WB"]=(df_comb["RES3BSmakeRES3B3to4WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B3to4WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B3to4WBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3B5plusNB"]=(df_comb["RES3BSmakeRES3B5PlusNBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B5PlusNBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B5PlusNBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3B5plusWB"]=(df_comb["RES3BSmakeRES3B5PlusWBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B5PlusWBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B5PlusWBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3B1to2"]=(df_comb["PRES3B1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3B1to2WB"]*Pctwbasement)
df_comb["PRES3B3to4"]=(df_comb["PRES3B3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3B3to4WB"]*Pctwbasement)
df_comb["RES3B5plus"]=(df_comb["PRES3B5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3B5plusWB"]*Pctwbasement)
###
df_comb["RES3B"]=(df_comb["PRES3B1to2"]*onetotwoStories)+(df_comb["PRES3B3to4"]*threetofourStories)+(df_comb["RES3B5plus"]*fiveandmore)
###
def hellRES3B(df_comb):
    if (df_comb['RES3B']>0.5):
        return 1
    elif (df_comb['RES3B']<0):
        return 0
    else:
        return df_comb['RES3B']
df_comb["RES3B"]=df_comb.apply(hellRES3B,axis=1)
##
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
df_comb["RES3BLossStrDC"]=df_comb["DCRES3B"]*df_comb["RES3B"]*df_comb["AreaInundated"]
df_comb["RES3BLossStrVA"]=df_comb["VRES3B"]*df_comb["RES3B"]*df_comb["AreaInundated"]
df_comb["RES3BLossStrM"]=df_comb["MRES3B"]*df_comb["RES3B"]*df_comb["AreaInundated"]
df_comb["RES3BLossStrTotal"]=df_comb["RES3BLossStrDC"]+df_comb["RES3BLossStrVA"]+df_comb["RES3BLossStrM"]
PyhtonTotalRES3BContent=df_comb["RES3BLossStrTotal"].sum()
print(PyhtonTotalRES3BContent*1000)