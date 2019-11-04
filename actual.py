
import os
import math
import cv2

from flask import Flask, render_template, url_for, request
app = Flask(__name__)


def videotoimage(video):
    videoFile = "C:\\Users\\manid\\Desktop\\Chainer_Realtime_Multi-Person_Pose_Estimation\\data1\\"+video
    imagesFolder = "C:\\Users\\manid\\Desktop\\Chainer_Realtime_Multi-Person_Pose_Estimation\\output"
    cap = cv2.VideoCapture(videoFile)
    count = 0
    frameRate = cap.get(5)  # frame rate

    while(cap.isOpened()):
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = imagesFolder + "/image" + str(count) + ".jpg"
            count = count+1
            cv2.imwrite(filename, frame)

    cap.release()
    print("Done!")


def videotoimage1(video):
    videoFile = "C:\\Users\\manid\\Desktop\\Chainer_Realtime_Multi-Person_Pose_Estimation\\data1\\"+video+".mp4"
    imagesFolder = "C:\\Users\\manid\\Desktop\\Chainer_Realtime_Multi-Person_Pose_Estimation\\input"
    cap = cv2.VideoCapture(videoFile)
    count = 0
    frameRate = cap.get(5)  # frame rate

    while(cap.isOpened()):
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = imagesFolder + "/image" + str(count) + ".jpg"
            count = count+1
            cv2.imwrite(filename, frame)

    cap.release()
    print("Done!")


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Then get the data from the form
        tag = request.form['upload']
        tag1 = request.form['fname']
        videotoimage(tag)
        videotoimage1(tag1)
        ret = os.system('python pose_detector.py')
        
        return render_template('page1.html')

    else:
        return render_template('page1.html')


if __name__ == "__main__":
    app.run(debug=True)
