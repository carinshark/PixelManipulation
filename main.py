from pixelgrid import Pixelgrid
from guizero import App,Text,Picture,PushButton, select_file,Box

textColor = "#9cfff2"

def playSort():
    creechur.sortImage()

def selectFile():
    global creechur
    file = select_file(filetypes=[["images",[".png",".jpg",".jpeg"]]])
    if (file):
        creechur=Pixelgrid(file)
        pic.image=file

def nextFrame():
    creechur.sortOnce()

def stopSort():
    pass







creechur = Pixelgrid("images1/ship.png")

myApp = App(title="the app",bg="#001C24")

myApp.text_color=textColor

title = Text(myApp,"sort image!",size=24)

pic = Picture(myApp,image="images1/psuedo.png",width=300,height=300)


idleBox = Box(myApp)
runningBox = Box(myApp)

startButton = PushButton(idleBox,command=playSort,
                         text="Click to Start!",visible=False)

nextFrameButton = PushButton(idleBox,command=nextFrame,text="next frame")

fileButton = PushButton(idleBox,command=selectFile,text="Select Image (Try less than 500x500)")

stopButton = PushButton(runningBox,command=stopSort,text="stop")

myApp.display()