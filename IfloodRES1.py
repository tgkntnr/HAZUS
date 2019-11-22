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
dxo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureByBlock")
dyo=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureByBlock")
dyt=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureByBlock")
###
dxo1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\DCtotal.xlsx',sheet_name="ExposureContentByBlock")
dyo1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\VirginiaTotal.xlsx',sheet_name="ExposureContentByBlock")
dyt1=pd.read_excel(r'D:\SelinaDEM\oye3\saksak\MarylandTotal.xlsx',sheet_name="ExposureContentByBlock")
###
df_comb=pd.merge(df2,df_area,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dpo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dxo1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyo1,on='CensusBlock',how='left')
df_comb=pd.merge(df_comb,dyt1,on='CensusBlock',how='left')
##############
df_comb['RES11storynobasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES11storynobasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES11storynobasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES11storynobasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES11storynobasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES11storynobasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storynobasementStructureSlabPostFIRM,axis=1)/100
df_comb['RES11storywbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES11storywbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES11storywbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES11storywbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES11storywbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES11storywbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES11storywbasementStructureSlabPostFIRM,axis=1)/100
###2storyonlystructure
df_comb['RES12storynbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES12storynbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES12storynbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES12storynbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES12storynbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES12storynbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storynbasementStructureSlabPostFIRM,axis=1)/100
df_comb['RES12storywbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES12storywbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES12storywbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES12storywbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES12storywbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES12storywbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES12storywbasementStructureSlabPostFIRM,axis=1)/100
##3storyonlystructure
df_comb['RES13storynbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES13storynbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES13storynbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES13storynbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES13storynbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES13storynbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storynbasementStructureSlabPostFIRM,axis=1)/100
df_comb['RES13storywbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES13storywbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES13storywbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES13storywbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES13storywbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES13storywbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES13storywbasementStructureSlabPostFIRM,axis=1)/100
#splitlevelonlystructure
df_comb['RES1sstorynbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES1sstorynbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES1sstorynbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES1sstorynbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorynbasementStructureSlabPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureBasementPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureBasementPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureBasementPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureBasementPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureCrawlPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureCrawlPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureCrawlPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureCrawlPostFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureSlabPreFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureSlabPreFIRM,axis=1)/100
df_comb['RES1sstorywbasementStructureSlabPostFIRM']=df_comb.apply(EconomicRESS2.EconomicRES1sstorywbasementStructureSlabPostFIRM,axis=1)/100
##
df_comb['RES2StructureDamageBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureBasementPreFIRM,axis=1)/100
df_comb['RES2StructureDamageBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureBasementPostFIRM,axis=1)/100
df_comb['RES2StructureDamageCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureCrawlPreFIRM,axis=1)/100
df_comb['RES2StructureDamageCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureCrawlPostFIRM,axis=1)/100
df_comb['RES2StructureDamageSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureSlabPreFIRM,axis=1)/100
df_comb['RES2StructureDamageSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2StructureSlabPostFIRM,axis=1)/100
df_comb['RES2ContentDamageBasementPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentBasementPreFIRM,axis=1)/100
df_comb['RES2ContentDamageBasementPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentBasementPostFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentCrawlPreFIRM,axis=1)/100
df_comb['RES2ContentDamageCrawlPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentCrawlPostFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPreFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentSlabPreFIRM,axis=1)/100
df_comb['RES2ContentDamageSlabPostFIRM']=df_comb.apply(EconomicRESS.EconomicRES2ContentSlabPostFIRM,axis=1)/100
##
df15=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureBasementPreFIRMStructureWeigh')
df16=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureBasementPostFIRMStructureWeigh')
df17=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureCrawlPreFIRMStructureWeigh')
df18=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureCrawlPostFIRMStructureWeigh')
df19=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureSlabPreFIRMStructureWeigh')
df20=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storynobasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storynobasementStructureSlabPostFIRMStructureWeigh')
df21=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureBasementPreFIRMStructureWeigh')
df22=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureBasementPostFIRMStructureWeigh')
df23=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureCrawlPreFIRMStructureWeigh')
df24=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureCrawlPostFIRMStructureWeigh')
df25=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureSlabPreFIRMStructureWeigh')
df26=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES11storywbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES11storywbasementStructureSlabPostFIRMtructureWeigh')
###
df27=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureBasementPreFIRMStructureWeigh')
df28=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureBasementPostFIRMStructureWeigh')
df29=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureCrawlPreFIRMStructureWeigh')
df30=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureCrawlPostFIRMStructureWeigh')
df31=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureSlabPreFIRMStructureWeigh')
df32=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storynbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storynbasementStructureSlabPostFIRMStructureWeigh')
df33=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureBasementPreFIRMStructureWeigh')
df34=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureBasementPostFIRMStructureWeigh')
df35=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureCrawlPreFIRMStructureWeigh')
df36=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureCrawlPostFIRMStructureWeigh')
df37=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureSlabPreFIRMStructureWeigh')
df38=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES12storywbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES12storywbasementStructureSlabPostFIRMtructureWeigh')
###
df39=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureBasementPreFIRMStructureWeigh')
df40=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureBasementPostFIRMStructureWeigh')
df41=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureCrawlPreFIRMStructureWeigh')
df42=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureCrawlPostFIRMStructureWeigh')
df43=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureSlabPreFIRMStructureWeigh')
df44=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storynbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storynbasementStructureSlabPostFIRMStructureWeigh')
df45=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureBasementPreFIRMStructureWeigh')
df46=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureBasementPostFIRMStructureWeigh')
df47=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureCrawlPreFIRMStructureWeigh')
df48=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureCrawlPostFIRMStructureWeigh')
df49=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureSlabPreFIRMStructureWeigh')
df50=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES13storywbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES13storywbasementStructureSlabPostFIRMStructureWeigh')
####
df51=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureBasementPreFIRMStructureWeigh')
df52=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureBasementPostFIRMStructureWeigh')
df53=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureCrawlPreFIRMStructureWeigh')
df54=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureCrawlPostFIRMStructureWeigh')
df55=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureSlabPreFIRMStructureWeigh')
df56=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorynbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorynbasementStructureSlabPostFIRMStructureWeigh')
df57=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureBasementPreFIRMStructureWeigh')
df58=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureBasementPostFIRMStructureWeigh')
df59=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureCrawlPreFIRMStructureWeigh')
df60=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureCrawlPostFIRMStructureWeigh')
df61=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureSlabPreFIRMStructureWeigh')
df62=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES1sstorywbasementStructureSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES1sstorywbasementStructureSlabPostFIRMStructureWeigh')
###
df63=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageBasementPreFIRMStructureWeigh')
df64=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageBasementPostFIRMStructureWeigh')
df65=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageCrawlPreFIRMStructureWeigh')
df66=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageCrawlPostFIRMStructureWeigh')
df67=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageSlabPreFIRMStructureWeigh')
df68=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2StructureDamageSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2StructureDamageSlabPostFIRMStructureWeigh')
df69=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageBasementPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageBasementPreFIRMStructureWeigh')
df70=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageBasementPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageBasementPostFIRMStructureWeigh')
df71=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageCrawlPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageCrawlPreFIRMStructureWeigh')
df72=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageCrawlPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageCrawlPostFIRMStructureWeigh')
df73=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageSlabPreFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageSlabPreFIRMStructureWeigh')
df74=df_comb.groupby("CensusBlock").apply(lambda dfx: (dfx["RES2ContentDamageSlabPostFIRM"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES2ContentDamageSlabPostFIRMStructureWeigh')
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
###

df_comb['PRES11storynobasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storynobasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureBasementPostFIRMStructureWeigh,axis=1)
df_comb['PRES11storynobasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storynobasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES11storynobasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storynobasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storynobasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureBasementPostFIRMtructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES11storywbasementStructureSlabPostFIRMtructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES11storywbasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureBasementPostFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storynbasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storynobasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureBasementPostFIRMtructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES12storywbasementStructureSlabPostFIRMtructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES12storywbasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureBasementPostFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storynbasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storynobasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES13storywbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storywbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureBasementPostFIRMtructureWeigh,axis=1)
df_comb['PRES13storywbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storywbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureCrawlPostFIRMStructureWeigh,axis=1)###
df_comb['PRES13storywbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES13storywbasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES13storywbasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureBasementPostFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorynbasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorynobasementStructureSlabPostFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureBasementPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureBasementPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureBasementPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureBasementPostFIRMtructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureCrawlPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureCrawlPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureCrawlPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureCrawlPostFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureSlabPreFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureSlabPreFIRMStructureWeigh,axis=1)
df_comb['PRES1sstorywbasementStructureSlabPostFIRMStructureWeigh']=df_comb.apply(pointfive.RES1Smake1RES1sstorywbasementStructureSlabPostFIRMStructureWeigh,axis=1)
###
df_comb["PRES2StructureDamageBasementPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageBasementPreFIRMStructureWeigh,axis=1)
df_comb["PRES2StructureDamageBasementPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageBasementPreFIRMStructureWeigh,axis=1)
df_comb["PRES2StructureDamageCrawlPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageCrawlPreFIRMStructureWeigh,axis=1)
df_comb["PRES2StructureDamageCrawlPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageCrawlPostFIRMStructureWeigh,axis=1)
df_comb["PRES2StructureDamageSlabPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageSlabPreFIRMStructureWeigh,axis=1)
df_comb["PRES2StructureDamageSlabPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2StructureDamageSlabPostFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageBasementPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageBasementPreFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageBasementPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageBasementPostFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageCrawlPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageCrawlPreFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageCrawlPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageCrawlPostFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageSlabPreFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageSlabPreFIRMStructureWeigh,axis=1)
#df_comb["PRES2ContentDamageSlabPostFIRMStructureWeigh"]=df_comb.apply(pointfive.RES2SmakeRES2ContentDamageSlabPostFIRMStructureWeigh,axis=1)


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
###
df_comb["PRES2StructureDamageBasementStructureWeigh"]=((df_comb['PRES2StructureDamageBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES2StructureDamageBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES2StructureDamageCrawlStructureWeigh"]=((df_comb['PRES2StructureDamageCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES2StructureDamageCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES2StructureDamageSlabStructureWeigh"]=((df_comb['PRES2StructureDamageSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES2StructureDamageSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES2ContentDamageBasementWeigh"]=((df_comb['RES2ContentDamageBasementPreFIRM']*df_comb["PREFIRM"])+(df_comb['RES2ContentDamageBasementPostFIRM']*df_comb["POSTFIRM"]))
df_comb["PRES2ContentDamageCrawlWeigh"]=((df_comb['RES2ContentDamageCrawlPreFIRM']*df_comb["PREFIRM"])+(df_comb['RES2ContentDamageCrawlPostFIRM']*df_comb["POSTFIRM"]))
df_comb["PRES2ContentDamageSlabWeigh"]=((df_comb['RES2ContentDamageSlabPreFIRM']*df_comb["PREFIRM"])+(df_comb['RES2ContentDamageSlabPostFIRM']*df_comb["POSTFIRM"]))
##
df_comb["PRES11storynobasementStructureBasementStructureWeigh"]=((df_comb['PRES11storynobasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES11storynobasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES11storynobasementStructureCrawlStructureWeigh"]=((df_comb['PRES11storynobasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES11storynobasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
df_comb["PRES11storynobasementStructureSlabStructureWeigh"]=((df_comb['PRES11storynobasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"])+(df_comb['PRES11storynobasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"]))
###
df_comb["PRES11storywbasementStructureBasementStructureWeigh"]=(df_comb['PRES11storywbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES11storywbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES11storywbasementStructureCrawlStructureWeigh"]=(df_comb['PRES11storywbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES11storywbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES11storywbasementStructureSlabStructureWeigh"]=(df_comb['PRES11storywbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES11storywbasementStructureSlabPostFIRMtructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES12storynobasementStructureBasementStructureWeigh"]=(df_comb['PRES12storynbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storynbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storynobasementStructureCrawlStructureWeigh"]=(df_comb['PRES12storynbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storynbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storynobasementStructureSlabStructureWeigh"]=(df_comb['PRES12storynbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storynbasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES12storywbasementStructureBasementStructureWeigh"]=(df_comb['PRES12storywbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storywbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storywbasementStructureCrawlStructureWeigh"]=(df_comb['PRES12storywbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storywbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES12storywbasementStructureSlabStructureWeigh"]=(df_comb['PRES12storywbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES12storywbasementStructureSlabPostFIRMtructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES13storynobasementStructureBasementStructureWeigh"]=(df_comb['PRES13storynbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storynbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storynobasementStructureCrawlStructureWeigh"]=(df_comb['PRES13storynbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storynbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storynobasementStructureSlabStructureWeigh"]=(df_comb['PRES13storynbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storynbasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES13storywbasementStructureBasementStructureWeigh"]=(df_comb['PRES13storywbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storywbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storywbasementStructureCrawlStructureWeigh"]=(df_comb['PRES13storywbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storywbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES13storywbasementStructureSlabStructureWeigh"]=(df_comb['PRES13storywbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES13storywbasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES1sstorynobasementStructureBasementStructureWeigh"]=(df_comb['PRES1sstorynbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES1sstorynbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorynobasementStructureCrawlStructureWeigh"]=(df_comb['PRES1sstorynbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES1sstorynbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorynobasementStructureSlabStructureWeigh"]=(df_comb['PRES1sstorynbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES1sstorynbasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES1sstorywbasementStructureBasementStructureWeigh"]=(df_comb['PRES1sstorywbasementStructureBasementPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['PRES1sstorywbasementStructureBasementPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorywbasementStructureCrawlStructureWeigh"]=(df_comb['PRES1sstorywbasementStructureCrawlPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorywbasementStructureCrawlPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
df_comb["PRES1sstorywbasementStructureSlabStructureWeigh"]=(df_comb['RES1sstorywbasementStructureSlabPreFIRMStructureWeigh']*df_comb["PREFIRM"]+df_comb['RES1sstorywbasementStructureSlabPostFIRMStructureWeigh']*df_comb["POSTFIRM"])
###
df_comb["PRES11NB"]=(df_comb["PRES11storynobasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES11storynobasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES11storynobasementStructureSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES11WB"]=(df_comb["PRES11storywbasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES11storywbasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES11storywbasementStructureSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES12NB"]=(df_comb["PRES12storynobasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES12storynobasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES12storynobasementStructureSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES12WB"]=(df_comb["PRES12storywbasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES12storywbasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES12storywbasementStructureSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES13NB"]=(df_comb["PRES13storynobasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES13storywbasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES13storynobasementStructureSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES13WB"]=(df_comb["PRES13storywbasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES13storywbasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES13storywbasementStructureSlabStructureWeigh"]*Slabfoundation)
###
df_comb["PRES1SplitNB"]=(df_comb["PRES1sstorynobasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES1sstorynobasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES1sstorynobasementStructureSlabStructureWeigh"]*Slabfoundation)
df_comb["PRES1SplitWB"]=(df_comb["PRES1sstorywbasementStructureBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES1sstorywbasementStructureCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES1sstorywbasementStructureSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES2"]=(df_comb["PRES2StructureDamageBasementStructureWeigh"]*Basementfoundation)+(df_comb["PRES2StructureDamageCrawlStructureWeigh"]*Crawlfoundation)+(df_comb["PRES2StructureDamageSlabStructureWeigh"]*Slabfoundation)
##
df_comb["PRES2C"]=(df_comb["PRES2ContentDamageBasementWeigh"]*Basementfoundation)+(df_comb["PRES2ContentDamageCrawlWeigh"]*Crawlfoundation)+(df_comb["PRES2ContentDamageSlabWeigh"]*Slabfoundation)
##
##
df_comb["PRES11"]=(df_comb["PRES11NB"]*Pctwithoutbasement)+(df_comb["PRES11WB"]*Pctwbasement)
df_comb["PRES12"]=(df_comb["PRES12NB"]*Pctwithoutbasement)+(df_comb["PRES12WB"]*Pctwbasement)
df_comb["PRES13"]=(df_comb["PRES13NB"]*Pctwithoutbasement)+(df_comb["PRES13WB"]*Pctwbasement)
df_comb["PRES1Split"]=(df_comb["PRES1SplitNB"]*Pctwithoutbasement)+(df_comb["PRES1SplitWB"]*Pctwbasement)
##
df_comb["RES1Str"]=(df_comb["PRES11"]*OneStory)+(df_comb["PRES12"]*TwoStory)+(df_comb["PRES13"]*ThreeStory)+(df_comb["PRES1Split"]*SplitLevel)
##
def hellRES1(df_comb):
    if (df_comb['RES1Str']>0.5):
        return 1
    elif (df_comb['RES1Str']<0):
        return 0
    else:
        return df_comb['RES1Str']
df_comb["RES1StrLast"]=df_comb.apply(hellRES1,axis=1)
##
def hellRES2(df_comb):
    if(df_comb['PRES2']>=0.5):
        return 1
    elif (df_comb['PRES2']<0):
        return 0
    else:
        return df_comb['PRES2']
##
df_comb["PRES2StrLast"]=df_comb.apply(hellRES2,axis=1)
###

df_comb=df_comb.drop_duplicates(subset='CensusBlock',keep='first')
df_comb=df_comb.fillna(0)
df_comb["RES1LossStrDC"]=df_comb["DCRES1"]*df_comb["RES1StrLast"]*df_comb["AreaInundated"]
df_comb["RES1LossStrVA"]=df_comb["VRES1"]*df_comb["RES1StrLast"]*df_comb["AreaInundated"]
df_comb["RES1LossStrM"]=df_comb["MRES1"]*df_comb["RES1StrLast"]*df_comb["AreaInundated"]
df_comb["RES1TotalStr"]=df_comb["RES1LossStrVA"]+df_comb["RES1LossStrDC"]+df_comb["RES1LossStrM"]
##########
df_comb["RES2LossStrDC"]=df_comb["DCRES2"]*df_comb["PRES2StrLast"]*df_comb["AreaInundated"]
df_comb["RES2LossStrVA"]=df_comb["VRES2"]*df_comb["PRES2StrLast"]*df_comb["AreaInundated"]
df_comb["RES2LossStrM"]=df_comb["MRES2"]*df_comb["PRES2StrLast"]*df_comb["AreaInundated"]
df_comb["RES2TotalStr"]=df_comb["RES2LossStrVA"]+df_comb["RES2LossStrDC"]+df_comb["RES2LossStrM"]
#########
df_comb["RES2LossCntDC"]=df_comb["CDCRES2"]*df_comb["PRES2C"]*df_comb["AreaInundated"]
df_comb["RES2LossCntVA"]=df_comb["CVRES2"]*df_comb["PRES2C"]*df_comb["AreaInundated"]
df_comb["RES2LossCntM"]=df_comb["CMRES2"]*df_comb["PRES2C"]*df_comb["AreaInundated"]
df_comb["RES2TotalCnt"]=df_comb["RES2LossCntDC"]+df_comb["RES2LossCntVA"]+df_comb["RES2LossCntM"]
#####
#nefret=df_comb["RES1TotalStr"].sum()
nefret2=df_comb["RES2TotalStr"].sum()
nefret3=df_comb["RES2TotalCnt"].sum()
#print(nefret*1000)
print(nefret2*1000)
print(nefret3*1000)
#df_comb.to_excel(r'D:\SelinaDEM\oye\nutuk223.xlsx',sheet_name="atam")
     

