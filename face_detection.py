import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('news.jpg')

# convert to greyscale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# scaleFactor: decrease by 5 percent for each run 
# the smaller, the slower, the higher accuracy
faces = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=5)

# faces is a numpy array, bounding box of face
# x_null, y_null, widht, height
print(type(faces))
print(faces.shape)
print(faces)

for x,y,w,h in faces:
    # bgr => (0, 255, 0) is green
    # 4 is width
    img = cv2.rectangle(img,(x, y), (x+w, y+h), (0,255,0), 4)

# show
cv2.imshow('grey face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()