# Name: CreateFeatureclass
# Description: Create a feature class 

# Import system modules
import arcpy
arcpy.env.overwriteOutput = True

workspace_path = r'C:\Users\najohn20\Desktop\python\python_project.gdb'
question_9_fc = r'C:\Users\najohn20\Desktop\python\python_project.gdb\exampledomain.shp' 
arcpy.CreateFeatureclass_management(workspace_path, question_9_fc)
domain_name = 'question9Domain'

print('feature class created')



arcpy.AddField_management(question_9_fc,'New_Field','SHORT','','','500','NULLABLE','NON_REQUIRED')

print('new field created')

#Create the domains

arcpy.CreateDomain_management(workspace_path, domain_name, '', "SHORT", "CODED", "DEFAULT", "DEFAULT")

print('domain created')

arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, '1', 'cd_value1')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, '2', 'cd_value2')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, '3', 'cd_value3')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, '4', 'cd_value4')
arcpy.AddCodedValueToDomain_management(workspace_path, domain_name, '5', 'cd_value5')

print('Coded value domains created')


arcpy.AssignDomainToField_management(question_9_fc, 'New_Field', domain_name, "") 

print('all done')


## Not sure where the errors are to be honest. I followed examples online and the GNSS script examples. This is my best attempt.

