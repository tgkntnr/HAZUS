# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:46:14 2019

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
####
df_comb['EconomicRES3A1to2NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBSTRSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBSTRSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBSTRSlabPostFIRM,axis=1)/100
###
df15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRBasementPreFIRMWeight')
df16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRBasementPostFIRMWeigh')
df17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRCrawlPreFIRMWeigh')
df18=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRCrawlPostFIRMWeigh')
df19=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRSlabPreFIRMWeigh')
df20=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBSTRSlabPostFIRMWeigh')
df21=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRBasementPreFIRMWeigh')
df22=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRBasementPostFIRMWeigh')
df23=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRCrawlPreFIRMWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRCrawlPostFIRMWeigh')
df25=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRSlabPreFIRMWeigh')
df26=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBSTRSlabPostFIRMWeigh')
###
df27=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRBasementPreFIRMWeigh')
df28=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRBasementPostFIRMWeigh')
df29=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRCrawlPreFIRMWeigh')
df30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRCrawlPostFIRMWeigh')
df31=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRSlabPreFIRMWeigh')
df32=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBSTRSlabPostFIRMWeigh')
df33=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRBasementPreFIRMWeigh')
df34=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRBasementPostFIRMWeigh')
df35=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRCrawlPreFIRMWeigh')
df36=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRCrawlPostFIRMWeigh')
df37=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRSlabPreFIRMWeigh')
df38=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBSTRSlabPostFIRMWeigh')
###
df39=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRBasementPreFIRMWeigh')
df40=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRBasementPostFIRMWeigh')
df41=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRCrawlPreFIRMWeigh')
df42=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRCrawlPostFIRMWeigh')
df43=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRSlabPreFIRMWeigh')
df44=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBSTRSlabPostFIRMWeigh')
df45=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRBasementPreFIRMWeigh')
df46=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRBasementPostFIRMWeigh')
df47=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRCrawlPreFIRMWeigh')
df48=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRCrawlPostFIRMWeigh')
df49=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRSlabPreFIRMWeigh')
df50=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBSTRSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBSTRSlabPostFIRMWeigh')
#############
df_comb=pd.merge(df_comb,df15,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df16,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df17,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df18,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df19,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df20,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df21,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df22,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df23,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df24,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df25,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df26,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df27,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df28,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df29,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df30,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df31,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df32,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df33,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df34,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df35,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df36,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df37,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df38,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df39,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df40,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df41,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df42,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df43,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df44,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df45,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df46,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df47,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df48,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df49,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,df50,on='CensusBlock',how='left')
####
df_comb['RES3A1to2NBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3A1to2NBSTRBasementPostFIRMWeighStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2NBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2NBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2NBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2NBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2NBSTRSlabPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A1to2WBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A1to2WBSTRSlabPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4NBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4NBSTRSlabPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A3to4WBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A3to4WBSTRSlabPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusNBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusNBSTRSlabPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRBasementPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRBasementPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRCrawlPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRCrawlPostFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRSlabPreFIRMStructureWeigh,axis=1)
df_comb['RES3ASmakeRES3A5PlusWBSTRSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES3ASmakeRES3A5PlusWBSTRSlabPostFIRMStructureWeigh,axis=1)
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
####
df_comb["RES3A1to2NBSTRBasementStructureWeigh"]=((df_comb['RES3A1to2NBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3A1to2NBSTRBasementPostFIRMWeighStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2NBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A1to2NBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A1to2NBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2NBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A1to2NBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A1to2NBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ASmakeRES3A1to2WBSTRBasementStructureWeigh"]=((df_comb['RES3ASmakeRES3A1to2WBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A1to2WBSTRBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2WBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A1to2WBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A1to2WBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2WBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A1to2WBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A1to2WBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ASmakeRES3A3to4NBSTRBasementStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4NBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4NBSTRBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4NBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4NBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4NBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4NBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4NBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4NBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ASmakeRES3A3to4WBSTRBasementStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4WBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4WBSTRBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4WBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4WBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4WBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4WBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A3to4WBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A3to4WBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ASmakeRES3A5PlusNBSTRBasementStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusNBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusNBSTRBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusNBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusNBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusNBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusNBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusNBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusNBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ASmakeRES3A5PlusWBSTRBasementStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusWBSTRBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusWBSTRBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusWBSTRCrawlStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusWBSTRCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusWBSTRCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusWBSTRSlabStructureWeigh"]=((df_comb['RES3ASmakeRES3A5PlusWBSTRSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['RES3ASmakeRES3A5PlusWBSTRSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
####
df_comb["PRES3A1to2NB"]=(df_comb["RES3A1to2NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A1to2NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A1to2NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3A1to2WB"]=(df_comb["RES3ASmakeRES3A1to2WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A1to2WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A1to2WBSTRSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES3A3to4NB"]=(df_comb["RES3ASmakeRES3A3to4NBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A3to4NBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A3to4NBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3A3to4WB"]=(df_comb["RES3ASmakeRES3A3to4WBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A3to4WBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A3to4WBSTRSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES3A5plusNB"]=(df_comb["RES3ASmakeRES3A5PlusNBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A5PlusNBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A5PlusNBSTRSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES3A5plusWB"]=(df_comb["RES3ASmakeRES3A5PlusWBSTRBasementStructureWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A5PlusWBSTRCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A5PlusWBSTRSlabStructureWeigh"]*Slabfoundation)
####
df_comb["PRES3A1to2"]=(df_comb["PRES3A1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3A1to2WB"]*Pctwbasement)
df_comb["PRES3A3to4"]=(df_comb["PRES3A3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3A3to4WB"]*Pctwbasement)
df_comb["RES3A5plus"]=(df_comb["PRES3A5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3A5plusWB"]*Pctwbasement)
###
df_comb["RES3A"]=(df_comb["PRES3A1to2"]*onetotwoStories)+(df_comb["PRES3A3to4"]*threetofourStories)+(df_comb["RES3A5plus"]*fiveandmore)
def hellRES3a(df_comb):
    if (df_comb['RES3A']>0.5):
        return 1
    elif (df_comb['RES3A']<0):
        return 0
    else:
        return df_comb['RES3A']
df_comb["RES3A"]=df_comb.apply(hellRES3a,axis=1)
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
##
df_comb["RES3ALossStrDC"]=df_comb["DCRES3A"]*df_comb["RES3A"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrVA"]=df_comb["VRES3A"]*df_comb["RES3A"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrM"]=df_comb["MRES3A"]*df_comb["RES3A"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrTotal"]=df_comb["RES3ALossStrDC"]+df_comb["RES3ALossStrVA"]+df_comb["RES3ALossStrM"]
PyhtonTotalRES3AContent=df_comb["RES3ALossStrTotal"].sum()
print(PyhtonTotalRES3AContent*1000)