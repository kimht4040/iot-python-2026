
import cv2
import numpy as np
import time


img = cv2.imread(filename='cat.jpeg')
if img is None:
    raise FileNotFoundError("로딩 실패")

origin = img.copy()#원본 이미지 복사

edited_img = None

win_name = 'Editor'




def update(_=None):
    alpha = cv2.getTrackbarPos('Contrast', win_name)/50 
    Blur = cv2.getTrackbarPos('Blur', win_name) 
    beta = cv2.getTrackbarPos("Brightness", win_name)-50
    edge = cv2.getTrackbarPos('Edge', win_name)
    edited = cv2.convertScaleAbs(origin, alpha=alpha, beta=beta)


    if Blur > 0:
        k = Blur * 2 + 1 
        edited = cv2.GaussianBlur(origin, (k, k), 0)
    cv2.imshow(win_name, edited)
    if edge >0:
        edited = cv2.Canny(edited, edge, edge*2)
        edited = cv2.cvtColor(edited, cv2.COLOR_GRAY2BGR)
    
    cv2.imshow("Editor", edited)
    global edited_img
    edited_img = edited




cv2.namedWindow(win_name)
cv2.createTrackbar('Blur', win_name, 0, 10, update)  #블러
cv2.createTrackbar('Contrast', win_name, 50, 150, update) # 대비
cv2.createTrackbar('Brightness', win_name, 10, 200, update) #밝기

cv2.createTrackbar('Edge', win_name, 0, 200, update) # 엣지



update()

while True:
    key = cv2.waitKey(1) & 0xff
    if key == ord('r'):
        cv2.imshow('simple imageEditor', origin)
        pass
    elif key == ord('s'):
        if edited_img is None:
            print("저장 이미지 없음")
        else:
            filename = f'saved_{int(time.time())}.jpg'
            cv2.imwrite(filename, edited_img)
            print('저장완료')
    elif key ==ord('q'):
        break
    else:
        cv2.imshow('simple imageEditor', origin)



cv2.destroyAllWindows()