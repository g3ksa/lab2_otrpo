import cv2

def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print(f"Найдено {len(faces)} лиц(а):")
    for (x, y, w, h) in faces:
        print(f"Лицо на координатах: x={x}, y={y}, w={w}, h={h}")

if __name__ == "__main__":
    image_path = 'image1.jpg'

    detect_faces(image_path)
