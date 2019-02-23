# Name:  Question 5 and CreateFileGDB_Example2.py


# Import system modules
import arcpy

#create your variables here

fgdb_name = 'question_5.gdb'

current_workspace_gdb = r'C:\Users\najohn20\Desktop\python\Exercise 3'
arcpy.CreateFileGDB_management(current_workspace_gdb, fgdb_name)

#Feature classes
geometry_type = 'POINT'

spatial_reference = arcpy.SpatialReference(102100)

featureClassNamesList = ['capitalCities', 'landmarks', 'historicPlaces', 'stateNames', 'nationalities', 'rivers']

current_workspace = r'C:\Users\najohn20\Desktop\python\Exercise 3\question_5.gdb'
arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True

# functions


def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')


createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

for fc in featureClassNamesList:
     createFeatureClass(fc)


print('All Done')


####
#try:
  #  arcpy.env.workspace =  
 
    # Copy the feature list 
  #  fc_List = featureList
 
    # Loop through the list and create features classes for the entire list 
  #  for featureClass in fc_List:
    #    try: 
    #        fcName = fc_List   
       #     outName = fcName  + '.shp'                                              
       #     outFolder = r'C:\Users\najohn20\Desktop\python\python_project.gdb'
            
        #    arcpy.CreateFeatureclass_management(out_path=outFolder
            #                        , outName=fcName
             #                       , geometry_type="POINT"
              #                      , template=""
               #                     , has_m="DISABLED"
                #                    , has_z="DISABLED"
                 #                   , spatial_reference=""
                  #                  , config_keyword=""
                   #                 , spatial_grid_1="0"
                    #                , spatial_grid_2="0"
                     #               , spatial_grid_3="0"
                      #              )




       #     print('Done creating feature class')    