import urllib.request
from moviepy.editor import *
from os import path
import shutil
videoPaths = []
videos = []

date = "202006"
url = "http://www.trafik.gov.tr/kurumlar/trafik.gov.tr/09-Video/KGYS/"+date+"/"
savePath = "D:\\Python\\VideoEditing\\accidents\\"

def downloadVideos():
    global videoPaths
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    for i in range(1,30):
        name = str(i)+".mp4"
        path = savePath+name
        videoPaths.append(path)
        videoUrl = url+name
        if os.path.exists(path):
            print("yes",name)
        else:
            print("no",name)
            try:
                urllib.request.urlretrieve(videoUrl,path)
                print(name,"indi.")
            except:
                pass
        

def combineVideos():
    global videos
    for path in videoPaths:
        try:
            video = VideoFileClip(path)
            video = video.cutout(video.duration-5,video.duration)
            videos.append(video)
        except:
            pass
    combinedVideo = concatenate_videoclips(videos)
    combinedVideo.write_videofile(date+"Combined.mp4",codec="libx264")

def deleteAccidentFolder():
    if os.path.exists(savePath):
        shutil.rmtree(savePath)

deleteAccidentFolder()
downloadVideos()
combineVideos()
