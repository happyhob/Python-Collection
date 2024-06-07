# import os
# main_folder = "C:\\Users\\WSuser\\Desktop\\WS공유\\노가다작업\\가을학기\\pdf저장 - 복사본" # 검색 폴더 위치

# folderList = []
# fileNameList = []
# for item in os.listdir(main_folder): # 해당 폴더 내 모든 파일 및 폴더 추출

#     sub_folder = os.path.join(main_folder, item)
#     strings = sub_folder.split('\\')
#     fileName = strings[len(strings)-1]
#     #print(fileName)
#     folderList.append(sub_folder)
#     fileNameList.append(fileName)
#     # if os.path.isdir(sub_folder): # 폴더 여부 확인
#     #     print(sub_folder)

###### pdf 페이지 분리해서 저장하기!!!!!#####

import os
from PyPDF2 import PdfReader, PdfWriter

# Define the main folder and paths
main_folder = "C:\\Users\\WSuser\\Desktop\\WS공유\\노가다작업\\가을학기\\pdf저장 - 복사본"
inputPath = main_folder + "\\"
savePath = "C:\\Users\\WSuser\\Desktop\\WS공유\\노가다작업\\가을학기\\TEST\\"

# Ensure the save directory exists
os.makedirs(savePath, exist_ok=True)

# Get the list of files in the main folder
fileNameList = []
for item in os.listdir(main_folder):
    sub_folder = os.path.join(main_folder, item)
    if os.path.isfile(sub_folder):
        fileNameList.append(item)

# Process each PDF file
for fn in fileNameList:
    ipath = os.path.join(inputPath, fn)
    print(ipath)

    try:
        # Load the existing PDF
        pdfReader = PdfReader(ipath)

        # Create a new PDF writer object
        pdfWriter = PdfWriter()

        # Add the first two pages to the new PDF
        pdfWriter.add_page(pdfReader.pages[0])
        pdfWriter.add_page(pdfReader.pages[1])

        # Define the new PDF path
        newPath = os.path.join(savePath, fn)

        # Save the new PDF
        with open(newPath, "wb") as output_pdf:
            pdfWriter.write(output_pdf)

        print(f"Successfully processed and saved: {newPath}")

    except Exception as e:
        print(f"Failed to process {ipath}: {e}")
