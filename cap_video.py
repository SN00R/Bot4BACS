import cv2

cap= cv2.VideoCapture(4)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width,height))


while True:
    ret,frame= cap.read()
    new = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

    writer.write(frame)

    cv2.imshow('frame', new)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
