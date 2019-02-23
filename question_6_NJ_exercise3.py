# Name: AddField_Example2.py
# Description: Add a new field to a table
 
# Import system modules
import arcpy
import os
import numpy
 

arcpy.env.overwriteOuput = True
# Set environment settings
arcpy.env.workspace = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb'

# Set local variables
inFeatures = 'CallsforService'
fieldName1 = 'Crime_Explanation'

# Execute AddField 
arcpy.AddField_management(inFeatures, fieldName1, "TEXT")

print('Field added')

# Name: CalculateField_ranges.py



list_fields = ['CFSType', 'Crime_Explanation'] 

#Update Cursor and now update the 
# Create update cursor for feature class 

with arcpy.da.UpdateCursor(inFeatures, list_fields) as cursor:
    for row in cursor:
        if row[0] == 'Burglary Call':
            row[1] = 'This is a Burglary'
        cursor.updateRow(row) 
        del cursor

print('Field updated')


## This worked up until the cursor. I used the following webpage: https://pro.arcgis.com/en/pro-app/arcpy/data-access/updatecursor-class.htm
# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm
# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-feature-class.htm
# Here is my work from my initial attemps below: 


# Set local variables
#inTable = inFeatures
#fieldName_edited = fieldName1
#expression = "CFSType = Burglary Call"

#def Reclass(CFSType):
 #   if CFSType = 'Burglary Call':
  #      return 'This is a Burglary' 
   # else:
      #  return 3"""
  
# arcpy.CalculateField_management(inTable, fieldName_edited, expression, "SQL")