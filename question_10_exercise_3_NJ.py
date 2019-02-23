# Name: SpatialJoin_Example2.py
# Description: Join attributes of cities to states based on spatial relationships.
# Requirements: os module

# Import system modules
import arcpy

# Set local variables
workspace = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise 3_question_5.gdb'
outWorkspace = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise 3_question_5.gdb'
 
target_features = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise 3_question_5.gdb\General_Offense'
join_features = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise 3_question_5.gdb\Tracts'
out_feature_class = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise 3_question_5.gdb\Offense_Tracts'

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
