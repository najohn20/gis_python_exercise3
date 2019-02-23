import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True

#change your feature class name here
fc_name = "New_CensusTracts"
 
fgdb_name = 'DataCollection.gdb'
workspace_path = r'C:\Users\najohn20\Desktop\python'
#create a gdb
arcpy.CreateFileGDB_management(workspace_path, fgdb_name)

print('gdb created')

#import modules

import pprint

pp = pprint.PrettyPrinter(indent=4)

#set a workspace
arcpy.env.workspace = r'C:\Users\najohn20\Desktop\python\Question 13\Question 13'

#set this environment setting to True so we can run our code repeatedly
arcpy.env.overwriteOutput = True

#set an output location because our import process will need a place to put its outputs
outputLocation = fgdb_name

#create a list of feature classes in the current workspace
in_features = arcpy.ListFeatureClasses()

#print the following list of shapefiles in the current workspace
pp.pprint("This folder contains the following shapefiles or feature classes: " + str(in_features))

#ask the user for feedback
boolPrompt = input("Would you like to import the following data? ")

#check whether the user wishes to proceed with importing the data
if boolPrompt == "Yes":
    for feature in in_features:
       arcpy.FeatureClassToGeodatabase_conversion(feature, outputLocation)
else:
    print("The data cannot be imported due to your answer.")
    
for feature in in_features:
    descObject = arcpy.Describe(feature)
    pp.pprint("Feature " + feature + " has the following properties: \n\n" + "Feature Type: " + descObject.featureType + " ShapeType: " + descObject.shapeType + " Spatial Index " + str(descObject.hasSpatialIndex) + "\n")

def dynamicFeatureImport(workspace, overwriteSetting, outputGDB):
    
    arcpy.env.workspace = workspace
    
    arcpy.env.overwriteOutput = overwriteSetting

    in_features = arcpy.ListFeatureClasses()

    #print the following list of shapefiles in the current workspace
    pp.pprint("This folder contains the following shapefiles or feature classes: " + str(in_features))

    #ask the user for feedback
    boolPrompt = input("Would you like to import the following data? ")

    #check whether the user wishes to proceed with importing the data
    if boolPrompt == "Yes":
        for feature in in_features:
            arcpy.FeatureClassToGeodatabase_conversion(feature, outputGDB)
    else:
        print("The data cannot be imported.")

dynamicFeatureImport(r'C:\Users\najohn20\Desktop\python\Question 13\Question 13', True, r'C:\Users\najohn20\Desktop\python\DataCollection.gdb')


# Name: Clip_Example2.py
# Description: Clip . 


# Set workspace
env.workspace = r'C:\Users\najohn20\Desktop\python\DataCollection.gdb'

# Set local variables
in_features = "tl_2018_us_county.shp"
clip_features = "tl_2018_04_tract.shp"
out_feature_class = r"C:\Users\najohn20\Desktop\python\Question 13\clip_census_maricopa.shp"
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)




## This was my best attempt at combining multiple scripts and ideas
# https://pro.arcgis.com/en/pro-app/tool-reference/analysis/clip.htm