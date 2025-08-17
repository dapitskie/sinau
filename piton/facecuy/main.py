import cv2

face_ref = cv2.CascadeClassifier('face_ref.xml')
camera = cv2.VideoCapture(0)

def face_detection(frame):
    opetimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(opetimized_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def drawer_box(frame):
    for x,y,w,h in face_detection(frame):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    pass

def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit

def mulaiambilgambar():
    if __name__ == "__main__" :
        print("Mulai deteksi wajah...")
        while True:
            _, frame = camera.read()
            drawer_box(frame)
            cv2.imshow('Cuy face aiaiaiaiai', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                close_window()
                break

if __name__ == "__main__":
    mulaiambilgambar()