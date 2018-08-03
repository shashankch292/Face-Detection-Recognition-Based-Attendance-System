# Face-Detection-Recognition-Based-Attendance-System

• Each teacher can login through his/her login ID and Password. Then he/she can chose an option to see existing attendance record of particular Branch, Year & Subject combination by selecting them.
• To update the record of a particular subject, the teacher have to upload the image of the whole class and select the respective Branch, Year & Subject and the database gets updated.
• The GUI is built using TkInter Module in python. The database is managed on MySQL. MySQLdb module of python is used to handle various user queries and to update the database.
• The face detection part is done through Haar-Cascade Classifier(through OpenCV) and face recognition by implementing LBPH algorithm through OpenCV module.
