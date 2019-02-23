# Name: fcCount.py
# Purpose: calculate the number of features in a feature class

# Import system modules
import arcpy
 
lyrfile = r"C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb\CallsforService.shp"
result = arcpy.GetCount_management(lyrfile)
print('{} has {} records'.format(lyrfile, result[0]))