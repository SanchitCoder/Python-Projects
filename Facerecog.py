import face_recognition
import cv2
import os
from datetime import datetime

# Load known faces
def load_known_faces(path="images"):
    known_encodings = []
    known_names = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(path, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                name = os.path.splitext(filename)[0]
                known_names.append(name)
    return known_encodings, known_names

# Save attendance
def mark_attendance(name, file_path="attendance.txt"):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    date_str = now.strftime('%Y-%m-%d')

    # Read existing attendance
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            entries = f.readlines()
    else:
        entries = []

    if not any(name in line and date_str in line for line in entries):
        with open(file_path, "a") as f:
            f.write(f"{name}, {timestamp}\n")
        print(f"[INFO] Marked attendance for {name} at {timestamp}")

# Main function
def main():
    known_encodings, known_names = load_known_faces()

    cap = cv2.VideoCapture(0)

    print("[INFO] Starting webcam. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for faster recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect and encode faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]
                mark_attendance(name)

            # Scale back up face locations
            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.imshow("Face Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
