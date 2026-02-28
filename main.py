from pixelgrid import Pixelgrid
from guizero import App,Text,Picture,PushButton, select_file,Box
from PIL import Image

textColor = "#9cfff2"
repeatTime = 250

def playSort():
    pic.repeat(repeatTime,sortCycle)
    idleBox.visible=False
    runningBox.visible=True


def selectFile():
    
    file = select_file(filetypes=[["images",[".png",".jpg",".jpeg"]]])
    if (file):
        switchImage(file)

def switchImage(file):
    global creechur
    creechur=Pixelgrid(file)
    pic.image=file
    pic.width,pic.height=creechur.image.size
    updateImage()

def nextFrame():
    out = creechur.sortOnce()
    updateImage()
    return out

def stopSort():
    pic.cancel(sortCycle)
    idleBox.visible=True
    runningBox.visible=False


def sortCycle():
    if nextFrame():
        stopSort()

def updateImage():
    imgSize=(int((500/creechur.image.height)*creechur.image.width),500)
    pic.image=creechur.image.resize(imgSize,resample=Image.Resampling.NEAREST)

    pic.width,pic.height=imgSize

creechur = Pixelgrid("images1/ship.png")

myApp = App(title="the app",bg="#001C24",width=810,height=810)
myApp.text_color=textColor

title = Text(myApp,"sort image!",size=24)

pic = Picture(myApp,image=creechur.image)
updateImage()

idleBox = Box(myApp)
runningBox = Box(myApp)

startButton = PushButton(idleBox,command=playSort,
                         text="Click to Start!")
nextFrameButton = PushButton(idleBox,command=nextFrame,text="next frame")
fileButton = PushButton(idleBox,command=selectFile,text="Select Image (Try less than 500x500)")
stopButton = PushButton(runningBox,command=stopSort,text="stop")

myApp.display()