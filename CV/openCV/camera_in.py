import sys
import cv2


# 웹 카메라 열기
cap = cv2.VideoCapture(0) 

# 동영상 파일 열기
# cap = cv2.VideoCapture("video2.mp4")

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
num = 0
cnt = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # inversed = ~frame  # 반전 -> 컬러 영상을 반전시키는건 의미x 
    
    num += 1
    
    # 프레이 저장하기
    if num == 30:
        cnt += 1
        filename = "frame_%04d.jpg" % cnt
        cv2.imwrite(filename, frame)
        num = 0
        

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)

    if cv2.waitKey(1) == 27:   # 27 = ESC키, 1ms간격으로 프레임 출력(하드웨어 성능에 따라 알아서 조절 됨)
        break

cap.release()
cv2.destroyAllWindows()
