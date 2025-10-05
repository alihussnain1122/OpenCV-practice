import os as os
import cv2 as cv
import numpy as np

people= ['Aaron_Guiel', 'Adrian_Nastase', 'Ally_Sheedy', 'Andrew_Caldecott', 'Anna_Jones']
DIR= r'D:\\lfw_funneled'
feature= []
labels= []
haar=cv.CascadeClassifier('haar_face.xml')


def create_train():
    for person in people:
        path= os.path.join(DIR, person)
        label= people.index(person)


        for img in os.listdir(path):
            img_path= os.path.join(path, img)

            img_array= cv.imread(img_path)
            gray= cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect= haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi= gray[y:y+h, x:x+w]
                feature.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')
features= np.array(feature, dtype='object')
labels= np.array(labels)
#print(f'Length of feature= {len(feature)}')
#print(f'Length of labels= {len(labels)}')


face_recognizer= cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)