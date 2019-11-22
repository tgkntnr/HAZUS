# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:26:32 2019

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
####3
df_comb['EconomicRES3B1to2NBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2NBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B1to2WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B1to2WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4NBContentContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4NBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B3to4WBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B3to4WBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusNBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusNBContentSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3B5PlusWBContentSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3B5PlusWBContentSlabPostFIRM,axis=1)/100
####
df51=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentBasementPreFIRMWeight')
df52=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentBasementPostFIRMWeigh')
df53=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentCrawlPreFIRMWeigh')
df54=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentCrawlPostFIRMWeigh')
df55=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentSlabPreFIRMWeigh')
df56=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2NBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2NBContentSlabPostFIRMWeigh')
df57=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentBasementPreFIRMWeigh')
df58=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentBasementPostFIRMWeigh')
df59=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentCrawlPreFIRMWeigh')
df60=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentCrawlPostFIRMWeigh')
df61=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentSlabPreFIRMWeigh')
df62=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B1to2WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B1to2WBContentSlabPostFIRMWeigh')
###
df63=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentBasementPreFIRMWeigh')
df64=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentBasementPostFIRMWeigh')
df65=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentCrawlPreFIRMWeigh')
df66=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentCrawlPostFIRMWeigh')
df67=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentSlabPreFIRMWeigh')
df68=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4NBContentContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4NBContentContentSlabPostFIRMWeigh')
df69=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentBasementPreFIRMWeigh')
df70=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentBasementPostFIRMWeigh')
df71=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentCrawlPreFIRMWeigh')
df72=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentCrawlPostFIRMWeigh')
df73=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentSlabPreFIRMWeigh')
df74=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B3to4WBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B3to4WBContentSlabPostFIRMWeigh')
###
df75=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentBasementPreFIRMWeigh')
df76=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentBasementPostFIRMWeigh')
df77=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentCrawlPreFIRMWeigh')
df78=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentCrawlPostFIRMWeigh')
df79=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentSlabPreFIRMWeigh')
df80=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusNBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusNBContentSlabPostFIRMWeigh')
df81=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentBasementPreFIRMWeigh')
df82=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentBasementPostFIRMWeigh')
df83=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentCrawlPreFIRMWeigh')
df84=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentCrawlPostFIRMWeigh')
df85=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentSlabPreFIRMWeigh')
df86=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3B5PlusWBContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3B5PlusWBContentSlabPostFIRMWeigh')
###
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
df_comb["RES3BSmakeRES3B1to2NBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B1to2NBContentBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2NBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2NBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B1to2NBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2NBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2NBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B1to2NBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2NBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3BSmakeRES3B1to2WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B1to2WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B1to2WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B1to2WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B1to2WBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B1to2WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3BSmakeRES3B3to4NBContentContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B3to4NBContentContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4NBContentContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4NBContentContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B3to4NBContentContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4NBContentContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4NBContentContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B3to4NBContentContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4NBContentContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3BSmakeRES3B3to4WBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B3to4WBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4WBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4WBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B3to4WBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4WBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B3to4WBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B3to4WBContentSlabPostFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B3to4WBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3BSmakeRES3B5PlusNBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusNBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusNBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusNBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusNBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusNBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusNBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusNBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusNBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3BSmakeRES3B5PlusWBContentBasementContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusWBContentBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusWBContentBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusWBContentCrawlContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusWBContentCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusWBContentCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3BSmakeRES3B5PlusWBContentSlabContentuctureWeigh"]=((df_comb['EconomicRES3B5PlusWBContentSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['EconomicRES3B5PlusWBContentSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES3B1to2NBC"]=(df_comb["RES3BSmakeRES3B1to2NBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B1to2NBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B1to2NBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3B1to2WBC"]=(df_comb["RES3BSmakeRES3B1to2WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B1to2WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B1to2WBContentSlabContentuctureWeigh"]*Slabfoundation)
##
df_comb["PRES3B3to4NBC"]=(df_comb["RES3BSmakeRES3B3to4NBContentContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B3to4NBContentContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B3to4NBContentContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3B3to4WBC"]=(df_comb["RES3BSmakeRES3B3to4WBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B3to4WBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B3to4WBContentSlabContentuctureWeigh"]*Slabfoundation)
###
df_comb["PRES3B5plusNBC"]=(df_comb["RES3BSmakeRES3B5PlusNBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B5PlusNBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B5PlusNBContentSlabContentuctureWeigh"]*Slabfoundation)
df_comb["PRES3B5plusWBC"]=(df_comb["RES3BSmakeRES3B5PlusWBContentBasementContentuctureWeigh"]*Basementfoundation)+(df_comb["RES3BSmakeRES3B5PlusWBContentCrawlContentuctureWeigh"]*Crawlfoundation)+(df_comb["RES3BSmakeRES3B5PlusWBContentSlabContentuctureWeigh"]*Slabfoundation)
###############
df_comb["PRES3B1to2C"]=(df_comb["PRES3B1to2NBC"]*Pctwithoutbasement)+(df_comb["PRES3B1to2WBC"]*Pctwbasement)
df_comb["PRES3B3to4C"]=(df_comb["PRES3B3to4NBC"]*Pctwithoutbasement)+(df_comb["PRES3B3to4WBC"]*Pctwbasement)
df_comb["RES3B5plusC"]=(df_comb["PRES3B5plusNBC"]*Pctwithoutbasement)+(df_comb["PRES3B5plusWBC"]*Pctwbasement)
##############
df_comb["RES3BC"]=(df_comb["PRES3B1to2C"]*onetotwoStories)+(df_comb["PRES3B3to4C"]*threetofourStories)+(df_comb["RES3B5plusC"]*fiveandmore)
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
####
df_comb["RES3BLossContentDC"]=df_comb["CDCRES3B"]*df_comb["RES3BC"]*df_comb["AreaInundated"]
df_comb["RES3BLossContentVA"]=df_comb["CVRES3B"]*df_comb["RES3BC"]*df_comb["AreaInundated"]
df_comb["RES3BLossContentM"]=df_comb["CMRES3B"]*df_comb["RES3BC"]*df_comb["AreaInundated"]
df_comb["RES3BLossContentTotal"]=df_comb["RES3BLossContentDC"]+df_comb["RES3BLossContentVA"]+df_comb["RES3BLossContentM"]
###
PyhtonTotalRES3BContent=df_comb["RES3BLossContentTotal"].sum()
print(PyhtonTotalRES3BContent*1000)