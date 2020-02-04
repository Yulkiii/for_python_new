import cv2

cap = cv2.VideoCapture('C:/Users/qwe/Music/MV/1.mp4')
fps =int(cap.get(cv2.CAP_PROP_FPS))
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
ret, frame = cap.read()
while(ret):
	cv2.imshow("capture", frame)
	videoWriter.write(frame)
	cv2.waitKey(fps)
	ret,frame = cap.read()

cap.release()
cv2.destroyAllWindows()
