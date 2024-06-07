

import os
main_folder = "C:\\Users\\WSuser\\Desktop\\WS공유\\노가다작업\\가을학기\\pdf저장" # 검색 폴더 위치

folderList = []
fileNameList = []
for item in os.listdir(main_folder): # 해당 폴더 내 모든 파일 및 폴더 추출

    sub_folder = os.path.join(main_folder, item)
    strings = sub_folder.split('\\')
    fileName = strings[len(strings)-1]
    print(fileName)
    folderList.append(sub_folder)
    fileNameList.append(fileName)
    # if os.path.isdir(sub_folder): # 폴더 여부 확인
    #     print(sub_folder)