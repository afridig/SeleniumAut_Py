import openpyxl

path="C:\\Users\\User\\Desktop\\mydemo.xlsx"

workbook=openpyxl.load_workbook(path) #creating a workbook object

sheet=workbook.active #getting the active sheet, mostly when there is only one sheet active in the workbook

#an alternative method is to get the sheet by its name when there are more than one sheet, as follows
#sheet=workBook.get_sheet_by_name("sheet1")

#populating the file, 5 rows and 3 columns
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="welcome"

workbook.save(path) #saving the file


