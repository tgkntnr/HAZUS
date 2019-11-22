# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:08:26 2019

@author: 90506
"""


import os
import numpy as np
import pandas as pd
import xlrd
import EconomicRESS2
import EconomicRESS
import IncomeLossModule
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t5.xlsx')
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
df_comb['EconomicRES3A1to2NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A1to2WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A1to2WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A3to4WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A3to4WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusNBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusNBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3A5PlusWBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3A5PlusWBContentSlabPostFIRM,axis=1)/100
###
df15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentBasementPreFIRMWeight')
df16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentBasementPostFIRMWeigh')
df17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentCrawlPreFIRMWeigh')
df18=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentCrawlPostFIRMWeigh')
df19=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentSlabPreFIRMWeigh')
df20=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2NBContentSlabPostFIRMWeigh')
df21=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentBasementPreFIRMWeigh')
df22=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentBasementPostFIRMWeigh')
df23=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentCrawlPreFIRMWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentCrawlPostFIRMWeigh')
df25=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentSlabPreFIRMWeigh')
df26=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A1to2WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A1to2WBContentSlabPostFIRMWeigh')
df27=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentBasementPreFIRMWeigh')
df28=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentBasementPostFIRMWeigh')
df29=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentCrawlPreFIRMWeigh')
df30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentCrawlPostFIRMWeigh')
df31=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentSlabPreFIRMWeigh')
df32=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4NBContentSlabPostFIRMWeigh')
df33=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentBasementPreFIRMWeigh')
df34=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentBasementPostFIRMWeigh')
df35=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentCrawlPreFIRMWeigh')
df36=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentCrawlPostFIRMWeigh')
df37=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentSlabPreFIRMWeigh')
df38=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A3to4WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A3to4WBContentSlabPostFIRMWeigh')
###
df39=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentBasementPreFIRMWeigh')
df40=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentBasementPostFIRMWeigh')
df41=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentCrawlPreFIRMWeigh')
df42=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentCrawlPostFIRMWeigh')
df43=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentSlabPreFIRMWeigh')
df44=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusNBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusNBContentSlabPostFIRMWeigh')
df45=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentBasementPreFIRMWeigh')
df46=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentBasementPostFIRMWeigh')
df47=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentCrawlPreFIRMWeigh')
df48=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentCrawlPostFIRMWeigh')
df49=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentSlabPreFIRMWeigh')
df50=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3A5PlusWBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3A5PlusWBContentSlabPostFIRMWeigh')
####
####
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
df_comb["RES3A1to2NBContentBasementContentWeigh"]=((df_comb['EconomicRES3A1to2NBContentBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2NBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A1to2NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2NBContentSlabContentuWeigh"]=((df_comb['EconomicRES3A1to2NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3ASmakeRES3A1to2WBContentBasementContentWeigh"]=((df_comb['EconomicRES3A1to2WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2WBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A1to2WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A1to2WBContentSlabContentWeigh"]=((df_comb['EconomicRES3A1to2WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A1to2WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ASmakeRES3A3to4NBContentBasementContentWeigh"]=((df_comb['EconomicRES3A3to4NBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4NBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A3to4NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4NBContentSlabContentWeigh"]=((df_comb['EconomicRES3A3to4NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ASmakeRES3A3to4WBContentBasementContentWeigh"]=((df_comb['EconomicRES3A3to4WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4WBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A3to4WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A3to4WBContentSlabContentWeigh"]=((df_comb['EconomicRES3A3to4WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A3to4WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3ASmakeRES3A5PlusNBContentBasementContentWeigh"]=((df_comb['EconomicRES3A5PlusNBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusNBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusNBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A5PlusNBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusNBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusNBContentSlabContentWeigh"]=((df_comb['EconomicRES3A5PlusNBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusNBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3ASmakeRES3A5PlusWBContentBasementContentWeigh"]=((df_comb['EconomicRES3A5PlusWBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusWBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusWBContentCrawlContentWeigh"]=((df_comb['EconomicRES3A5PlusWBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusWBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3ASmakeRES3A5PlusWBContentSlabContentWeigh"]=((df_comb['EconomicRES3A5PlusWBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3A5PlusWBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["PRES3A1to2NBC"]=(df_comb["RES3A1to2NBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A1to2NBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A1to2NBContentSlabContentuWeigh"]*Slabfoundation)
df_comb["PRES3A1to2WBC"]=(df_comb["RES3ASmakeRES3A1to2WBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A1to2WBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A1to2WBContentSlabContentWeigh"]*Slabfoundation)
##
df_comb["PRES3A3to4NBC"]=(df_comb["RES3ASmakeRES3A3to4NBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A3to4NBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A3to4NBContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES3A3to4WBC"]=(df_comb["RES3ASmakeRES3A3to4WBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A3to4WBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A3to4WBContentSlabContentWeigh"]*Slabfoundation)
###
df_comb["PRES3A5plusNBC"]=(df_comb["RES3ASmakeRES3A5PlusNBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A5PlusNBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A5PlusNBContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES3A5plusWBC"]=(df_comb["RES3ASmakeRES3A5PlusWBContentBasementContentWeigh"]*Basementfoundation)+(df_comb["RES3ASmakeRES3A5PlusWBContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["RES3ASmakeRES3A5PlusWBContentSlabContentWeigh"]*Slabfoundation)
#####
df_comb["PRES3A1to2C"]=(df_comb["PRES3A1to2NBC"]*Pctwithoutbasement)+(df_comb["PRES3A1to2WBC"]*Pctwbasement)
df_comb["PRES3A3to4C"]=(df_comb["PRES3A3to4NBC"]*Pctwithoutbasement)+(df_comb["PRES3A3to4WBC"]*Pctwbasement)
df_comb["RES3A5plusC"]=(df_comb["PRES3A5plusNBC"]*Pctwithoutbasement)+(df_comb["PRES3A5plusWBC"]*Pctwbasement)
###
df_comb["RES3AC"]=(df_comb["PRES3A1to2C"]*onetotwoStories)+(df_comb["PRES3A3to4C"]*threetofourStories)+(df_comb["RES3A5plusC"]*fiveandmore)
###
#def hellRES3a(df_comb):
#   if (df_comb['RES3AC']>0.5):
#        return 1
#    elif (df_comb['RES3AC']<0):
#        return 0
#    else:
#        return df_comb['RES3AC']
#df_comb["RES3AC"]=df_comb.apply(hellRES3a,axis=1)
####
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
###
df_comb["RES3ALossStrDC"]=df_comb["CDCRES3A"]*df_comb["RES3AC"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrVA"]=df_comb["CVRES3A"]*df_comb["RES3AC"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrM"]=df_comb["CMRES3A"]*df_comb["RES3AC"]*df_comb["AreaInundated"]
df_comb["RES3ALossStrTotal"]=df_comb["RES3ALossStrDC"]+df_comb["RES3ALossStrVA"]+df_comb["RES3ALossStrM"]
####
PyhtonTotalRES3AContent=df_comb["RES3ALossStrTotal"].sum()
print(PyhtonTotalRES3AContent*1000)