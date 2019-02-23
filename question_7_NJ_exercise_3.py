import arcpy
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

#set workspace
arcpy.env.workspace = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb'

#set tool and its results to be equal to a variable
offensesNearLandmarks = arcpy.SelectLayerByAttribute_management('General_Offenses', 'INTERSECT', 
                                                          'landmarks', 0, 'NEW_SELECTION')
#use results put into crimeNearBusStops variable in CopyFeatures_management
arcpy.CopyFeatures_management(offensesNearLandmarks, 'Offenses_Near_Landmarks')

def offenselandmarkSelection(workspace, inLayer, selectionType, layerToSelectAgainst, distance):
    
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True
    
    offensesNearLandmarks = arcpy.SelectLayerByAttribute_management(inLayer, selectionType, layerToSelectAgainst, distance)

    arcpy.CopyFeatures_management(offensesNearLandmarks, 'Offenses_Near_Landmarks')

    pp.pprint("Analysis completed")

offenselandmarkSelection(r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb', 'Tempe_General_Offenses', 'INTERSECT', 'landmarks', 0, 'NEW_SELECTION')

# Set local variables
outWorkspace = r"C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb"
 
# Use ListFeatureClasses to generate a list of shapefiles in the
#  workspace shown above.
fcList = arcpy.ListFeatureClasses()
 
# Execute CopyFeatures for each input shapefile
for shapefile in fcList:
    # Determine the new output feature class path and name
    outFeatureClass = os.path.join(outWorkspace, shapefile.strip("landmarks_2.shp"))
    arcpy.CopyFeatures_management(shapefile, outFeatureClass)

# Set the local parameters
inFeatures = "offenselandmarkSelection"
joinField = "Shape_Area"
joinTable = "landmarks"


# Join two feature classes by the zonecode field and only carry 
# over the land use and land cover fields
arcpy.JoinField_management(inFeatures, joinField, joinTable, joinField, 
                           )



## This is as far as I got.
# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/join-field.htm
# http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/copy-features.htm

##https://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-attribute.htm
