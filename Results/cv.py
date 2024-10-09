import cv2 
import pyzbar.pyzbar as pyzbar
import sqlite3

conn = sqlite3.connect('exam_result.db')
cursor = conn.cursor()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    print("Frame captured:", ret)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    try:
        decoded_objects = pyzbar.decode(frame)
        
        for obj in decoded_objects:
            print("QR Code Detected:")
            print("Decoded Info:", obj.data.decode("utf-8"))
            exam_result_id = obj.data.decode("utf-8")

            try:
                cursor.execute("SELECT * FROM exam_result WHERE ID=?", (exam_result_id,))
                cursor.execute("SELECT * FROM exam_result WHERE ID=?", {"id": exam_result_id})
                result = cursor.fetchtone()
                if result:
                    print("Authentic Exam Result:")
                    print("Student Name:", exam_result_id[1])
                    print("Exam Score:", exam_result_id[2])
                    print("Exam Subject:", exam_result_id[3])
                else:
                    print("Invalid Exam result ID")
            except sqlite3.Error as e:
                print("Error reterieving exam result", e)
    except TypeError:
        print("No QR Code Detected")

    try:
        cv2.imshow("Frame", frame)
    except cv2.error as e:
        print("Error displaying frame:", e)

    try:
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except Exception as e:
        print("Error waiting for key press:", e) 

conn.close()

cap.release()
cv2.destroyAllWindows()