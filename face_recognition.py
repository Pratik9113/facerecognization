# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np


# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1080x720+0+0")
#         self.root.title("student")

#         imgbg1 = Image.open(r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png")
#         imgbg1 = imgbg1.resize(
#             (1080, 720), Image.BILINEAR
#         )  # Change to your desired filter
#         self.photoimg1 = ImageTk.PhotoImage(imgbg1)

#         bg_img = Label(self.root, image=self.photoimg1)
#         bg_img.place(width=1080, height=720)

#         img5 = Image.open(r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png")
#         img5 = img5.resize((200, 120), Image.BILINEAR)
#         self.photoimg5 = ImageTk.PhotoImage(img5)
#         b2 = Button(
#             bg_img, image=self.photoimg5, command=self.face_recog, cursor="hand2"
#         )
#         b2.place(width=200, height=120, x=220, y=20)

#         b1_2 = Button(bg_img, text="photo", command=self.face_recog, cursor="hand2")
#         b1_2.place(x=220, y=90, width=200, height=40)

#     def face_recog(self):
#         def draw_boundary(img, classifer, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifer.detectMultiScale(gray_image, scaleFactor, minNeighbors)

#             coord = []

#             for x, y, w, h in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 id, predict = clf.predict(gray_image[y : y + h, x : x + w])
#                 confidence = int(100 * (1 - predict / 300))

#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     username="root",
#                     password="Pratik@6878",
#                     database="face_recognition",
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute(
#                     "select studentname from studentdetails where studentid" + str(id)
#                 )

#                 n = my_cursor.fetchone()
#                 n = "+".join(n)

#                 my_cursor.execute(
#                     "select studentid from studentdetails where studentid" + str(id)
#                 )

#                 i = my_cursor.fetchone()
#                 i = "+".join(i)

#                 my_cursor.execute(
#                     "select studentdiv from studentdetails where studentid" + str(id)
#                 )

#                 r = my_cursor.fetchone()
#                 r = "+".join(r)

#                 if confidence > 75:
#                     cv2.putText(
#                         img,
#                         f"studentid:{i}",
#                         (x, y - 55),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255, 255, 255),
#                         3,
#                     )
#                     cv2.putText(
#                         img,
#                         f"studentname:{n}",
#                         (x, y - 30),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255, 255, 255),
#                         3,
#                     )
#                     cv2.putText(
#                         img,
#                         f"studentdiv:{r}",
#                         (x, y - 5),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255, 255, 255),
#                         3,
#                     )
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

#                     cv2.putText(
#                         img,
#                         "not detected",
#                         (x, y - 5),
#                         cv2.FONT_HERSHEY_COMPLEX,
#                         0.8,
#                         (255, 255, 255),
#                         3,
#                     )
#                 coord = [x, y, w, h]

#             return coord

#         def recognize(img, clf, faceCascade):
#             coord = draw_boundary(
#                 img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf
#             )
#             return img

#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         # dekna idhar create ka
#         clf.read("classifier.xml")

#         video_cap = cv2.VideoCapture(0)

#         while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("face recognition", img)

#             if cv2.waitKey(1) == 13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+0+0")
        self.root.title("student")

        imgbg1 = Image.open(r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png")
        imgbg1 = imgbg1.resize(
            (1080, 720), Image.BILINEAR
        )  # Change to your desired filter
        self.photoimg1 = ImageTk.PhotoImage(imgbg1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(width=1080, height=720)

        img5 = Image.open(r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png")
        img5 = img5.resize((200, 120), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(
            bg_img, image=self.photoimg5, command=self.face_recog, cursor="hand2"
        )
        b2.place(width=200, height=120, x=220, y=20)

        b1_2 = Button(bg_img, text="photo", command=self.face_recog, cursor="hand2")
        b1_2.place(x=220, y=90, width=200, height=40)

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            coord = []

            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Pratik@6878",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select studentname from studentdetails where studentid = "
                    + str(id)
                )

                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"

                my_cursor.execute(
                    "select studentid from studentdetails where studentid = " + str(id)
                )

                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"

                my_cursor.execute(
                    "select studentdiv from studentdetails where studentid = " + str(id)
                )

                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"

                if confidence > 60:
                    cv2.putText(
                        img,
                        f"studentid:{i}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 0, 0),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"studentname:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 0, 0),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"studentdiv:{r}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 0, 0),
                        3,
                    )
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

                    cv2.putText(
                        img,
                        "not detected",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, face_cascade):
            coord = draw_boundary(
                img, face_cascade, 1.1, 10, (255, 25, 255), "Face", clf
            )
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        # dekna idhar create ka
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cascade)
            cv2.imshow("face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
