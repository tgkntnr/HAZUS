# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:06:08 2019

@author: 90506
"""

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
import pointfive
df2=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\t1.xlsx')
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
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureByBlock")
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
####
df_comb['EconomicRES3F1to2NBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2NBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2NBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F1to2WBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F1to2WBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4NBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4NBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F3to4WBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F3to4wBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3E5PlusNBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusNBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5NBSlabPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBBasementPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBBasementPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBCrawlPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBCrawlPostFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBSlabPreFIRM,axis=1)/100
df_comb['EconomicRES3F5PlusWBStructureSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES3F5wBSlabPostFIRM,axis=1)/100
####
df160=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureBasementPreFIRMWeight')
df161=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureBasementPostFIRMWeigh')
df162=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureCrawlPreFIRMWeigh')
df163=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureCrawlPostFIRMWeigh')
df164=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureSlabPreFIRMWeigh')
df165=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2NBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2NBStructureSlabPostFIRMWeigh')
df166=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureBasementPreFIRMWeigh')
df167=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureBasementPostFIRMWeigh')
df168=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureCrawlPreFIRMWeigh')
df169=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureCrawlPostFIRMWeigh')
df170=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureSlabPreFIRMWeigh')
df171=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F1to2WBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F1to2WBStructureSlabPostFIRMWeigh')
###
df172=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureBasementPreFIRMWeigh')
df173=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureBasementPostFIRMWeigh')
df174=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureCrawlPreFIRMWeigh')
df175=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureCrawlPostFIRMWeigh')
df176=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureSlabPreFIRMWeigh')
df177=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4NBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4NBStructureSlabPostFIRMWeigh')
df178=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureBasementPreFIRMWeigh')
df179=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureBasementPostFIRMWeigh')
df180=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureCrawlPreFIRMWeigh')
df181=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureCrawlPostFIRMWeigh')
df182=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureSlabPreFIRMWeigh')
df183=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F3to4WBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F3to4WBStructureSlabPostFIRMWeigh')
###
df184=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureBasementPreFIRMWeigh')
df185=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureBasementPostFIRMWeigh')
df186=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3E5PlusNBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureCrawlPreFIRMWeigh')
df187=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureCrawlPostFIRMWeigh')
df188=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureSlabPreFIRMWeigh')
df189=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusNBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusNBStructureSlabPostFIRMWeigh')
df190=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureBasementPreFIRMWeigh')
df191=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureBasementPostFIRMWeigh')
df192=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureCrawlPreFIRMWeigh')
df193=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureCrawlPostFIRMWeigh')
df194=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureSlabPreFIRMWeigh')
df195=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["EconomicRES3F5PlusWBStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='EconomicRES3F5PlusWBStructureSlabPostFIRMWeigh')
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
df_comb['RES3FSmakeRES3F1to2NBSTRBasementPreFIRMWeight']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBBasementPreFIRMWeight,axis=1)
df_comb['RES3FSmakeRES3F1to2NBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2NBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2NBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2NBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBSlabPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2NBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2NBSTRBSlabPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F1to2WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F1to2WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4NBSTRSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4NBSTRSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F3to4WBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F3to4WBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRSlabPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusNBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusNBSTRSlabPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusWBSTRBasementPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRBasementPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusWBSTRBasementPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRBasementPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusWBSTRCrawlPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRCrawlPreFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusWBSTRCrawlPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRCrawlPostFIRMWeigh,axis=1)
df_comb['RES3FSmakeRES3F5PlusWBSTRSlabPreFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRSlabPreFIRMWeigh,axis=1)###
df_comb['RES3FSmakeRES3F5PlusWBSTRSlabPostFIRMWeigh']=df_comb.apply(pointfive.RES3FSmakeRES3F5PlusWBSTRSlabPostFIRMWeigh,axis=1)

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

df_comb["RES3FSmakeRES3F1to2NBStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2NBSTRBasementPreFIRMWeight']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2NBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2NBStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2NBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2NBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2NBStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2NBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2NBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
###
df_comb["RES3FSmakeRES3F1to2WBStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2WBStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F1to2WBStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F1to2WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F1to2WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3FSmakeRES3F3to4NBStructureStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4NBSTRSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4NBSTRSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4NBStructureStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4NBSTRSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4NBSTRSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4NBStructureStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4NBSTRSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4NBSTRSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3FSmakeRES3F3to4WBStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4WBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4WBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4WBStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4WBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4WBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F3to4WBStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F3to4WBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F3to4WBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["RES3FSmakeRES3F5PlusNBStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusNBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusNBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusNBStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusNBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusNBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusNBStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusNBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusNBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####3
df_comb["RES3FSmakeRES3F5PlusWBStructureBasementStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusWBSTRBasementPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusWBSTRBasementPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusWBStructureCrawlStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusWBSTRCrawlPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusWBSTRCrawlPostFIRMWeigh']*df_comb["POSTFIRM"]))
df_comb["RES3FSmakeRES3F5PlusWBStructureSlabStructureuctureWeigh"]=((df_comb['RES3FSmakeRES3F5PlusWBSTRSlabPreFIRMWeigh']*df_comb["PREFIRM"])+(df_comb['RES3FSmakeRES3F5PlusWBSTRSlabPostFIRMWeigh']*df_comb["POSTFIRM"]))
####
df_comb["PRES3F1to2NB"]=(df_comb["RES3FSmakeRES3F1to2NBStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F1to2NBStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F1to2NBStructureSlabStructureuctureWeigh"]*Slabfoundation)
df_comb["PRES3F1to2WB"]=(df_comb["RES3FSmakeRES3F1to2WBStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F1to2WBStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F1to2WBStructureSlabStructureuctureWeigh"]*Slabfoundation)
##
df_comb["PRES3F3to4NB"]=(df_comb["RES3FSmakeRES3F3to4NBStructureStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F3to4NBStructureStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F3to4NBStructureStructureSlabStructureuctureWeigh"]*Slabfoundation)
df_comb["PRES3F3to4WB"]=(df_comb["RES3FSmakeRES3F3to4WBStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F3to4WBStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F3to4WBStructureSlabStructureuctureWeigh"]*Slabfoundation)
###
df_comb["PRES3F5plusNB"]=(df_comb["RES3FSmakeRES3F5PlusNBStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F5PlusNBStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F5PlusNBStructureSlabStructureuctureWeigh"]*Slabfoundation)
df_comb["PRES3F5plusWB"]=(df_comb["RES3FSmakeRES3F5PlusWBStructureBasementStructureuctureWeigh"]*Basementfoundation)+(df_comb["RES3FSmakeRES3F5PlusWBStructureCrawlStructureuctureWeigh"]*Crawlfoundation)+(df_comb["RES3FSmakeRES3F5PlusWBStructureSlabStructureuctureWeigh"]*Slabfoundation)
####
df_comb["PRES3F1to2"]=(df_comb["PRES3F1to2NB"]*Pctwithoutbasement)+(df_comb["PRES3F1to2WB"]*Pctwbasement)
df_comb["PRES3F3to4"]=(df_comb["PRES3F3to4NB"]*Pctwithoutbasement)+(df_comb["PRES3F3to4WB"]*Pctwbasement)
df_comb["RES3F5plus"]=(df_comb["PRES3F5plusNB"]*Pctwithoutbasement)+(df_comb["PRES3F5plusWB"]*Pctwbasement)
###
df_comb["RES3F"]=(df_comb["PRES3F1to2"]*onetotwoStories)+(df_comb["PRES3F3to4"]*threetofourStories)+(df_comb["RES3F5plus"]*fiveandmore)
def hellRES3F(df_comb):
    if (df_comb['RES3F']>0.5):
        return 1
    elif (df_comb['RES3F']<0):
        return 0
    else:
        return df_comb['RES3F']
df_comb["RES3F"]=df_comb.apply(hellRES3F,axis=1)
###
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
###
df_comb["RES3FLossStructureDC"]=df_comb["DCRES3F"]*df_comb["RES3F"]*df_comb["AreaInundated"]
df_comb["RES3FLossStuctureVA"]=df_comb["VRES3F"]*df_comb["RES3F"]*df_comb["AreaInundated"]
df_comb["RES3FLossStructureM"]=df_comb["MRES3F"]*df_comb["RES3F"]*df_comb["AreaInundated"]
df_comb["RES3FLossStructureTotal"]=df_comb["RES3FLossStructureDC"]+df_comb["RES3FLossStuctureVA"]+df_comb["RES3FLossStructureM"]
###
PyhtonTotalRES3EStructure=df_comb["RES3FLossStructureTotal"].sum()
print(PyhtonTotalRES3EStructure*1000)