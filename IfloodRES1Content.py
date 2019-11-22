# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:41:29 2019

@author: 90506
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 01:28:02 2019

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
####
Basementfoundation=0.23
Crawlfoundation=0.35
Slabfoundation=0.42
####
Pctwbasement=0.19
Pctwithoutbasement=0.81
##3
OneStory=0.66
TwoStory=0.32
ThreeStory=0.01
SplitLevel=0.01
onetotwoStories=0.69
threetofourStories=0.26
fiveandmore=0.05
####
dpo=pd.read_excel(r'D:\SelinaDEM\oye3\Mean.xlsx')
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureContentByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureContentByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureContentByBlock")
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
df_comb['RES11storynobasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentBasementPreFIRM,axis=1)/100
df_comb['RES11storynobasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentBasementPostFIRM,axis=1)/100
df_comb['RES11storynobasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES11storynobasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES11storynobasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentSlabPreFIRM,axis=1)/100
df_comb['RES11storynobasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementContentSlabPostFIRM,axis=1)/100
df_comb['RES11storywbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES11storywbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES11storywbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES11storywbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES11storywbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES11storywbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementContentSlabPostFIRM,axis=1)/100
###2storyonlyContent
df_comb['RES12storynbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES12storynbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES12storynbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES12storynbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES12storynbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES12storynbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementContentSlabPostFIRM,axis=1)/100
df_comb['RES12storywbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES12storywbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES12storywbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES12storywbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES12storywbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES12storywbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementContentSlabPostFIRM,axis=1)/100
##3storyonlyContent
df_comb['RES13storynbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES13storynbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES13storynbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES13storynbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES13storynbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES13storynbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementContentSlabPostFIRM,axis=1)/100
df_comb['RES13storywbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES13storywbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES13storywbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES13storywbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES13storywbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES13storywbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementContentSlabPostFIRM,axis=1)/100
#splitlevelonlyContent
df_comb['RES1sstorynbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES1sstorynbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES1sstorynbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementContentSlabPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementContentSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementContentSlabPostFIRM,axis=1)/100
##
df_comb['RES2ContentDamageBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentBasementPreFIRM,axis=1)/100
df_comb['RES2ContentDamageBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentBasementPostFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentSlabPreFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storynobasementContentSlabPostFIRM,axis=1)/100
df_comb['RES2ContentDamageBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentBasementPreFIRM,axis=1)/100
df_comb['RES2ContentDamageBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentBasementPostFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentCrawlPreFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentCrawlPostFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentSlabPreFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES11storywbasementContentSlabPostFIRM,axis=1)/100
##
df15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentBasementPreFIRMContentWeigh')
df16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentBasementPostFIRMContentWeigh')
df17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentCrawlPreFIRMContentWeigh')
df18=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentCrawlPostFIRMContentWeigh')
df19=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentSlabPreFIRMContentWeigh')
df20=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementContentSlabPostFIRMContentWeigh')
df21=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentBasementPreFIRMContentWeigh')
df22=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentBasementPostFIRMContentWeigh')
df23=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentCrawlPreFIRMContentWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentCrawlPostFIRMContentWeigh')
df25=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentSlabPreFIRMContentWeigh')
df26=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementContentSlabPostFIRMtructureWeigh')
###
df27=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentBasementPreFIRMContentWeigh')
df28=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentBasementPostFIRMContentWeigh')
df29=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentCrawlPreFIRMContentWeigh')
df30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentCrawlPostFIRMContentWeigh')
df31=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentSlabPreFIRMContentWeigh')
df32=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementContentSlabPostFIRMContentWeigh')
df33=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentBasementPreFIRMContentWeigh')
df34=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentBasementPostFIRMContentWeigh')
df35=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentCrawlPreFIRMContentWeigh')
df36=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentCrawlPostFIRMContentWeigh')
df37=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentSlabPreFIRMContentWeigh')
df38=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementContentSlabPostFIRMtructureWeigh')
###
df39=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentBasementPreFIRMContentWeigh')
df40=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentBasementPostFIRMContentWeigh')
df41=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentCrawlPreFIRMContentWeigh')
df42=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentCrawlPostFIRMContentWeigh')
df43=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentSlabPreFIRMContentWeigh')
df44=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementContentSlabPostFIRMContentWeigh')
df45=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentBasementPreFIRMContentWeigh')
df46=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentBasementPostFIRMContentWeigh')
df47=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentCrawlPreFIRMContentWeigh')
df48=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentCrawlPostFIRMContentWeigh')
df49=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentSlabPreFIRMContentWeigh')
df50=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementContentSlabPostFIRMContentWeigh')
####
df51=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentBasementPreFIRMContentWeigh')
df52=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentBasementPostFIRMContentWeigh')
df53=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentCrawlPreFIRMContentWeigh')
df54=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentCrawlPostFIRMContentWeigh')
df55=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentSlabPreFIRMContentWeigh')
df56=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementContentSlabPostFIRMContentWeigh')
df57=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentBasementPreFIRMContentWeigh')
df58=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentBasementPostFIRMContentWeigh')
df59=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentCrawlPreFIRMContentWeigh')
df60=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentCrawlPostFIRMContentWeigh')
df61=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentSlabPreFIRMContentWeigh')
df62=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementContentSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementContentSlabPostFIRMContentWeigh')
###

###
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

###

df_comb["CEp"]=df_comb.apply(IncomeLossModule.IncomeLossConditionCep,axis=1)
df_comb["CAa"]=df_comb.apply(IncomeLossModule.IncomeLossConditionCAa,axis=1)
df_comb["CCg"]=df_comb.apply(IncomeLossModule.IncomeLossConditionCCg,axis=1)
df_comb["CLg"]=df_comb.apply(IncomeLossModule.IncomeLossConditionCLg,axis=1)
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
df_comb["PREFIRM"]=df_comb.apply(PreFIRM,axis=1)
df_comb["POSTFIRM"]=df_comb.apply(PostFIRM,axis=1)
##
df_comb["PRES11storynobasementContentBasementContentWeigh"]=((df_comb['RES11storynobasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"])+(df_comb['RES11storynobasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES11storynobasementContentCrawlContentWeigh"]=((df_comb['RES11storynobasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"])+(df_comb['RES11storynobasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES11storynobasementContentSlabContentWeigh"]=((df_comb['RES11storynobasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"])+(df_comb['RES11storynobasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES11storywbasementContentBasementContentWeigh"]=(df_comb['RES11storywbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES11storywbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES11storywbasementContentCrawlContentWeigh"]=(df_comb['RES11storywbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES11storywbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES11storywbasementContentSlabContentWeigh"]=(df_comb['RES11storywbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES11storywbasementContentSlabPostFIRMtructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES12storynobasementContentBasementContentWeigh"]=(df_comb['RES12storynbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storynbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storynobasementContentCrawlContentWeigh"]=(df_comb['RES12storynbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storynbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storynobasementContentSlabContentWeigh"]=(df_comb['RES12storynbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storynbasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES12storywbasementContentBasementContentWeigh"]=(df_comb['RES12storywbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storywbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storywbasementContentCrawlContentWeigh"]=(df_comb['RES12storywbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storywbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storywbasementContentSlabContentWeigh"]=(df_comb['RES12storywbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES12storywbasementContentSlabPostFIRMtructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES13storynobasementContentBasementContentWeigh"]=(df_comb['RES13storynbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storynbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storynobasementContentCrawlContentWeigh"]=(df_comb['RES13storynbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storynbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storynobasementContentSlabContentWeigh"]=(df_comb['RES13storynbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storynbasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES13storywbasementContentBasementContentWeigh"]=(df_comb['RES13storywbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storywbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storywbasementContentCrawlContentWeigh"]=(df_comb['RES13storywbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storywbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storywbasementContentSlabContentWeigh"]=(df_comb['RES13storywbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES13storywbasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES1sstorynobasementContentBasementContentWeigh"]=(df_comb['RES1sstorynbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorynbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorynobasementContentCrawlContentWeigh"]=(df_comb['RES1sstorynbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorynbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorynobasementContentSlabContentWeigh"]=(df_comb['RES1sstorynbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorynbasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES1sstorywbasementContentBasementContentWeigh"]=(df_comb['RES1sstorywbasementContentBasementPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorywbasementContentBasementPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorywbasementContentCrawlContentWeigh"]=(df_comb['RES1sstorywbasementContentCrawlPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorywbasementContentCrawlPostFIRMContentWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorywbasementContentSlabContentWeigh"]=(df_comb['RES1sstorywbasementContentSlabPreFIRMContentWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorywbasementContentSlabPostFIRMContentWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES11NB"]=(df_comb["PRES11storynobasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES11storynobasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES11storynobasementContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES11WB"]=(df_comb["PRES11storywbasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES11storywbasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES11storywbasementContentSlabContentWeigh"]*Slabfoundation)
##
df_comb["PRES12NB"]=(df_comb["PRES12storynobasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES12storynobasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES12storynobasementContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES12WB"]=(df_comb["PRES12storywbasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES12storywbasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES12storywbasementContentSlabContentWeigh"]*Slabfoundation)
###
df_comb["PRES13NB"]=(df_comb["PRES13storynobasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES13storywbasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES13storynobasementContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES13WB"]=(df_comb["PRES13storywbasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES13storywbasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES13storywbasementContentSlabContentWeigh"]*Slabfoundation)
###
df_comb["PRES1SplitNB"]=(df_comb["PRES1sstorynobasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES1sstorynobasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES1sstorynobasementContentSlabContentWeigh"]*Slabfoundation)
df_comb["PRES1SplitWB"]=(df_comb["PRES1sstorywbasementContentBasementContentWeigh"]*Basementfoundation)+(df_comb["PRES1sstorywbasementContentCrawlContentWeigh"]*Crawlfoundation)+(df_comb["PRES1sstorywbasementContentSlabContentWeigh"]*Slabfoundation)

##
df_comb["PRES11C"]=(df_comb["PRES11NB"]*Pctwithoutbasement)+(df_comb["PRES11WB"]*Pctwbasement)
df_comb["PRES12C"]=(df_comb["PRES12NB"]*Pctwithoutbasement)+(df_comb["PRES12WB"]*Pctwbasement)
df_comb["PRES13C"]=(df_comb["PRES13NB"]*Pctwithoutbasement)+(df_comb["PRES13WB"]*Pctwbasement)
df_comb["PRES1SplitC"]=(df_comb["PRES1SplitNB"]*Pctwithoutbasement)+(df_comb["PRES1SplitWB"]*Pctwbasement)
##
df_comb["RES1Content"]=(df_comb["PRES11C"]*OneStory)+(df_comb["PRES12C"]*TwoStory)+(df_comb["PRES13C"]*ThreeStory)+(df_comb["PRES1SplitC"]*SplitLevel)
##
#def hellRES1(df_comb):
#    if (df_comb['RES1Str']>0.5):
#        return 1
#   elif (df_comb['RES1Str']<0):
#        return 0
#    else:
#       return df_comb['RES1Str']
#df_comb["RES1StrLast"]=df_comb.apply(hellRES1,axis=1)
##
#def hellRES2(df_comb):
#    if(df_comb['PRES2']>=0.5):
#       return 1
#    elif (df_comb['PRES2']<0):
#        return 0
#    else:
#        return df_comb['PRES2']
##
#df_comb["PRES2StrLast"]=df_comb.apply(hellRES2,axis=1)
df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
df_comb["RES1LossContentCDC"]=df_comb["CDCRES1"]*df_comb["RES1Content"]*df_comb["AreaInundated"]
df_comb["RES1LossContentCVA"]=df_comb["CVRES1"]*df_comb["RES1Content"]*df_comb["AreaInundated"]
df_comb["RES1LossContentCM"]=df_comb["CMRES1"]*df_comb["RES1Content"]*df_comb["AreaInundated"]
df_comb["RES1TotalContent"]=df_comb["RES1LossContentCDC"]+df_comb["RES1LossContentCVA"]+df_comb["RES1LossContentCM"]

nefret=df_comb["RES1TotalContent"].sum()
print(nefret*1000)
df_comb.to_excel(r'D:\SelinaDEM\oye\nutuk223.xlsx',sheet_name="atam")
     

