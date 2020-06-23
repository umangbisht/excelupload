from django.shortcuts import render
import openpyxl
import datetime
from myapp.models import ExcelData
import os
from django.core.files.storage import FileSystemStorage
import random
from django.contrib import messages
import xlrd
#import pandas

def index(request):
	VALID_EXTENSIONS = [
	"xlsx",
]
	validationErrors = {}
	if "GET" == request.method:
		return render(request, 'myapp/index.html', {})
	else:
		if request.FILES.get("excel_file") == None:
			validationErrors["excel_file"]	=	"Please select your excel file."
		else:
			excel_file = request.FILES.get("excel_file")
			file = excel_file.name
			extension = file.split(".")[-1].lower()
			if not extension in VALID_EXTENSIONS:
				validationErrors["excel_file"]	=	"This is not a valid file. Please upload a valid file."
		if not validationErrors:
			currentMonth = datetime.datetime.now().month
			currentYear = datetime.datetime.now().year
			folder = 'media/uploads/'
			folder_directory = 'uploads/'

			if not os.path.exists(folder):
				os.mkdir(folder)
			if request.FILES.get("excel_file"):
				pntiwdpFile = request.FILES.get("excel_file")
				fs = FileSystemStorage()
				filename = pntiwdpFile.name.split(".")[0].lower()
				extension = pntiwdpFile.name.split(".")[-1].lower()
				newfilename = filename+str(random.randint(0,922337))+"."+extension
				fs.save(folder_directory+newfilename, pntiwdpFile)
				messages.success(request,"File has been uploaded successfully.")
			fileReader(request,newfilename)
		return render(request, 'myapp/index.html',{"errors":validationErrors})



def fileReader(request, newname):
	folder_directory = 'uploads/'
	newfilename = newname
	os.chdir('F:\\vamsi\\vamsi\\media\\'+folder_directory)
	loc	= ('F:\\vamsi\\vamsi\\media\\'+folder_directory+newfilename)
	wb = xlrd.open_workbook(os.path.join(loc)) 
	sheet = wb.sheet_by_index(0) 
	sheet.cell_value(0, 0) 

	exceldataList	=	[]
	for i in range(sheet.nrows):
		exceldataList.append(sheet.row_values(i))
	sheetData				=	ExcelData()
	sheetData.all_record	=	exceldataList
	sheetData.file_name		=	newfilename
	sheetData.save()
	return True






