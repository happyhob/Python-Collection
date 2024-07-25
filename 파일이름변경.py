import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = 'C:\\Users\\WSuser\\Desktop\\교구재 사진'
file_names = os.listdir(file_path)
file_names

# >>> ['photo-1577055209976-ddae617a8023.jpg', 'photo-1577255714682-69db9b067fda.jpg', ..., 'photo-1579122549707-440e9edc4a6d.jpg']


i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1