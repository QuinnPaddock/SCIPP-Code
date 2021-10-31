import csv

#need to extract the fields "EPC" and "Local Name" from the csv file "module frames 23june2021.csv"

filename = 'module frames 23june2021.csv' #this will need to be changed based on what the file is called on whatever computer

										  
with open(filename, 'r', newline='') as csv_file:
	reader = csv.reader(csv_file)
	fields = next(reader)	
	rows = list(reader)		



for column_number, field in enumerate(fields): 
	if(field == 'EPC'):
		print(field)
		for row in rows:
			print(row[column_number])

		print('\n')

	elif(field == 'Local Name'):
		print(field)
		for row in rows:
			print(row[column_number])

		print('\n')
