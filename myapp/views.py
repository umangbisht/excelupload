from django.shortcuts import render
import openpyxl
import datetime
import os
from django.core.files.storage import FileSystemStorage
import random


def index(request):
	VALID_EXTENSIONS = [
	"csv",
	"xls",
]
	validationErrors = {}
	if "GET" == request.method:
		return render(request, 'myapp/index.html', {})
	else:
		'''excel_file = request.FILES["excel_file"]

		# you may put validations here to check extension or file size

		wb = openpyxl.load_workbook(excel_file)

		# getting all sheets
		sheets = wb.sheetnames
		print(sheets)

		# getting a particular sheet
		worksheet = wb["Sheet1"]
		print(worksheet)

		# getting active sheet
		active_sheet = wb.active
		print(active_sheet)

		# reading a cell
		print(worksheet["A1"].value)

		excel_data = list()
		# iterating over the rows and
		# getting value from each cell in row
		for row in worksheet.iter_rows():
			row_data = list()
			for cell in row:
				row_data.append(str(cell.value))
				print(cell.value)
			excel_data.append(row_data)'''
		if request.FILES.get("excel_file") == None:
			validationErrors["excel_file"]	=	"Please select photo next to id with dated paper"
		else:
			excel_file = request.FILES.get("excel_file")
			file = excel_file.name
			extension = file.split(".")[-1].lower()
			if not extension in VALID_EXTENSIONS:
				validationErrors["excel_file"]	=	"This is not a valid image. Please upload a valid featured image."
		if not validationErrors:
			currentMonth = datetime.datetime.now().month
			currentYear = datetime.datetime.now().year
			folder = 'media/uploads/'+str(currentMonth)+str(currentYear)+"/"
			folder_directory = 'uploads/'+str(currentMonth)+str(currentYear)+"/"
			if not os.path.exists(folder):
				os.mkdir(folder)
			if request.FILES.get("excel_file"):
				pntiwdpFile = request.FILES.get("excel_file")
				fs = FileSystemStorage()
				filename = pntiwdpFile.name.split(".")[0].lower()
				extension = pntiwdpFile.name.split(".")[-1].lower()
				newfilename = str(int(datetime.datetime.now().timestamp()))+str(random.randint(0,922337))+"."+extension
				fs.save(folder_directory+newfilename, pntiwdpFile)	
				pntiwdp_image	=	str(currentMonth)+str(currentYear)+"/"+newfilename

		return render(request, 'myapp/index.html',{"errors":validationErrors})









