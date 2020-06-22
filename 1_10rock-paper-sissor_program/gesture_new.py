import cv2
import numpy as np
import time
class gesture:
    def __init__(self):
        #pics to show to play rock-paper-sessiors game
        self.rock= cv2.imread("data/rock.jpg")
        self.paper= cv2.imread("data/paper.jpg")
        self.scissors= cv2.imread("data/scissors.jpg")
        self.clone=None
        self.this_time=time.time()
        self.fps=0
    #recall the rgb,pixel value
    def mouse_event(self,event, x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            print('PIX:',x,y)
            print('BGR:',self.clone[y,x])
            global ax
            global ay
            ax=x
            ay=y
            cv2.circle(self.clone,(x,y),3,(255,255,0),1)#draw circle
    def ellipse_detect(self,image):
        #skin detection
        img =image
        skinCrCbHist = np.zeros((256,256), dtype= np.uint8 )
        cv2.ellipse(skinCrCbHist ,(113,155),(23,15),43,0, 360, (255,255,255),-1)
        YCRCB = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
        (y,cr,cb)= cv2.split(YCRCB)
        skin = np.zeros(cr.shape, dtype=np.uint8)
        (x,y)= cr.shape
        #accelerate process speed
        for i in range(0,int(x/3)):
            i=3*i
            for j in range(0,int(y/3)):
                j=j*3
                CR= YCRCB[i,j,1]
                CB= YCRCB[i,j,2]
                if skinCrCbHist [CR,CB]>0:
                    skin[i,j]= 255
        kernel = np.ones((3,3),np.uint8)  
        skin= cv2.dilate(skin,kernel,iterations = 1)
        #cv2.imshow("cutout",skin)
        cnts, _ = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        if len(cnts) == 0:
            return None
        else:
            segmented = max(cnts, key=cv2.contourArea)
            return (1, segmented)
    def loop(self):
            #for saving photos
            im_count = 0
            # get the reference to the webcam
            camera = cv2.VideoCapture(3)
            x, y, r = 240, 320, 100
            # region of interest (ROI) coordinates
            top, right, bottom, left = x-r, y-r, x+r, y+r
            #for calculating fps
            num_frames = 0
            # keep looping, until interrupted
            while(True):
                # get the current frame
                (grabbed, frame) = camera.read()
                while frame is None:
                    (grabbed, frame) = camera.read()
                    print("No camera\n")
                # flip the frame so that it is not the mirror view
                frame = cv2.flip(frame, 1)
                # clone the frame
                self.clone = frame.copy()
                # get the height and width of the frame
                (height, width) = frame.shape[:2]
                # get the ROI
                roi = frame[top:bottom, right:left]
                # convert the roi to grayscale and blur it
                #get the hand region
                hand=self.ellipse_detect(roi)
                # check whether hand region is segmented
                if hand is not None:
                    # segmented region
                    (thresholded, segmented) = hand
                    epsilon = 0.001*cv2.arcLength(segmented,True)
                    segmented = cv2.approxPolyDP(segmented,epsilon,True)
                    # draw the segmented region and display the frame
                    convex_hull = cv2.convexHull(segmented)
                    cv2.rectangle(self.clone, (left, top), (right, bottom), (0,0,0),thickness=cv2.FILLED)
                    cv2.drawContours(self.clone, [convex_hull+(right, top) ], -1, (255, 0, 0), thickness=cv2.FILLED)
                    cv2.drawContours(self.clone, [segmented+(right, top)], -1, (0, 255, 255), thickness=cv2.FILLED)
                    s1=cv2.contourArea(convex_hull)
                    s2=cv2.contourArea(segmented)
                    #defects = cv2.convexityDefects(segmented,convex_hull)
                    ans=0
                    if s1/s2<1.2:
                        ans=0
                        cv2.imshow("ans",self.paper)
                    elif s1/s2<1.4:
                        ans=1
                        cv2.imshow("ans",self.rock)
                    else:
                        ans=2
                        cv2.imshow("ans",self.scissors)
                    text = ["rock", "scissors", "paper"][ans] + " " + str(round(s1/s2, 2))
                    cv2.putText(self.clone, text, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
                text2 ="fps:"+ " " + str(self.fps)
                cv2.putText(self.clone, text2, (30,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
                # draw the segmented hand
                cv2.rectangle(self.clone, (left, top), (right, bottom), (0,255,0), 2)
                # increment the number of frames
                num_frames += 1
                if time.time()-self.this_time>1:
                    self.fps=num_frames
                    self.this_time=time.time()
                    num_frames=0
                # display the frame with segmented hand
                cv2.imshow("Video Feed", self.clone)
                cv2.setMouseCallback("Video Feed",self.mouse_event)		
                # observe the keypress by the user
                keypress = cv2.waitKey(1) & 0xFF
                # if the user pressed "q", then stop looping
                path = None
                if keypress == ord("r"):
                    path = "r" + str(im_count) + ".png"
                elif keypress == ord("p"):
                    path = "p" + str(im_count) + ".png"
                elif keypress == ord("s"):
                    path = "s" + str(im_count) + ".png"
                if path is not None:
                    cv2.imwrite("data/" + path, self.clone)
                    im_count += 1
            # free up memory
            camera.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    my=gesture()
    my.loop()
    
