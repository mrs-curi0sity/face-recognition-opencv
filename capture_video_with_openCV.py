#https://www.udemy.com/the-python-mega-course/learn/lecture/4775504#content

import cv2, time

# 0 ist die Quelle: z.B. 0 Frontcamera
video = cv2.VideoCapture(0)

counter = 1

while True:
    counter+= 1

    # guck, ob alles klappt
    check, frame = video.read()
    print(f'check worked: {check}')
    print(f'type of result {type(frame)}')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # warte 3 sek, damit nicht sofort geschlossen
    # time.sleep(3)

    # frame is very first frame
    cv2.imshow('press q to quit', gray)

    # close when closed
    # cv2.waitKey(0)

    # schliesse nach 2 Sekunden
    key = cv2.waitKey(50)

    # press q to quit
    if key == ord('q'):
        break


print(f'number of passes throught loops {counter}')

video.release()
cv2.destroyAllWindows