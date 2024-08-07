import cv2

# 얼굴 검출기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 웹캠 열기
webcam = cv2.VideoCapture(0)

# 웹캠 오류 처리
if not webcam.isOpened():
    print("WebCam is not running")
    exit()

time_num = 0    
image_num = 0

# 특정 영역 설정 (예: 화면 중앙에 사각형 설정)
frame_width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
center_x, center_y = frame_width // 2, frame_height // 2
region_size = 200  # 사각형 크기 설정
top_left_x = center_x - region_size // 2
top_left_y = center_y - region_size // 2
bottom_right_x = center_x + region_size // 2
bottom_right_y = center_y + region_size // 2

while webcam.isOpened():
    status, frame = webcam.read()
    time_num += 1

    if not status:
        break

    # 얼굴 감지
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 특정 영역에 얼굴이 있는지 확인
    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        if (top_left_x < face_center_x < bottom_right_x and 
                top_left_y < face_center_y < bottom_right_y):
            # 캡쳐 프레임 간격 설정
            if time_num == 30:
                image_num += 1
                cv2.imwrite('img' + str(image_num) + '.png', frame)
                time_num = 0
            break

    # 특정 영역 표시
    cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)

    # 출력창
    cv2.imshow("WebCam", frame)

    # q 입력시 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
