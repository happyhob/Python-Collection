import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import glob

folder_path = 'C:\\Users\\WSuser\\Desktop\\새 폴더\\작업완료'  # PDF 파일들이 있는 경로

merger = PdfMerger()

# PDF 파일 목록 가져오기 및 생성 시간 기준으로 정렬
pdf_files = sorted(glob.glob(folder_path + '/*.pdf'), key=os.path.getctime, reverse=True)

# 각 PDF 파일을 병합
for pdf_file in pdf_files:
    merger.append(pdf_file)

# 병합된 PDF 파일 저장
result_path = os.path.join(folder_path, "_result.pdf")
merger.write(result_path)
merger.close()

print(f"병합된 PDF 파일이 생성되었습니다: {result_path}")
