import arcpy
import csv

featureClass = r'C:\Users\najohn20\Desktop\python\Exercise 3\Exercise_3.gdb\Police_General_Offense'
fieldNames = ['primary_ke', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand', 'place_name', 'OffenseCus']
cursorFields = ','.join(fieldNames)
crimeCount = 0

filterStatement = "OffenseCus = 'BURGLARY FROM FORCE' AND locationTranslation = 'Residence/Home'"

with open('burglaries.csv','w') as csvFile:
	fileWriter = csv.writer(csvFile,delimiter = ',',quotechar = '|', quoting = csv.QUOTE_MINIMAL)
	fileWriter.writerow(fieldNames)
	with arcpy.da.SearchCursor(featureClass,fieldNames,filterStatement) as cursor:
		for row in cursor:
			crimeCount += 1
			fileWriter.writerow(row)


print('Created csv file')
