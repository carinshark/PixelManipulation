from pixelgrid import Pixelgrid
from guizero import App,Text,Picture,PushButton,Text,Box,MenuBar
from guizero import select_file,question,error
from PIL import Image
from webbrowser import open_new_tab as openurl



textColor = "#C5EBC3"
repeatTime = 150
maxSize=300
buttonSize=50

#images in numpy format cuz i cant figure out executables...




def playSort():
    pic.repeat(repeatTime,sortCycle)
    idleBox.visible=False
    runningBox.visible=True


def selectFile():
    stopSort()
    file = select_file(filetypes=[["images",[".png",".jpg",".jpeg"]]])
    if (file):
        switchImage(file)

def switchImage(file):
    
    global creechur
    creechur=Pixelgrid(file,creechur.maxResolution)
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
    if (creechur.image.size[1]>creechur.image.size[0]):
        imgSize=(int((maxSize/creechur.image.height)*creechur.image.width),maxSize)
    else:
        imgSize=(maxSize,int((maxSize/creechur.image.width)*creechur.image.height))

    
    pic.image=creechur.image.resize(imgSize,resample=Image.Resampling.NEAREST)

    pic.width,pic.height=imgSize


def updateSize():
    a=getNumberInput()
    if (a):
        global maxSize
        maxSize=a
        updateImage()
        updateRenderText()

    

def getNumberInput(text="Please enter a number!"):
    try:
        a = question("Number Input",text)
        a=int(a)
        return a
    except ValueError:
        error("WRONG!","Please enter a whole number greater than 1!")

def exitApp():
    exit()

def changeResolution():
    a=getNumberInput()
    if (a):
        global creechur
        creechur=Pixelgrid(creechur.filename,a)
        updateImage()
        updateResolutionText()

def githubLink():
    openurl("https://github.com/carinshark/PixelManipulation")


def frameTime():
    a=getNumberInput("(in milliseconds btw)")
    if a:
        global repeatTime
        repeatTime=a
        stopSort()
        updateRenderText()


def downloadCurrent():
    a=select_file("Choose where to save",
                    filetypes=[[creechur.filetype,creechur.filetype]],
                    save=True)
    if (a):
        a=a if (a.endswith(creechur.filetype)) else a+creechur.filetype
        pic.image.save(a)

def resetImage():
    global creechur
    if not creechur.wasRandom:
        creechur=Pixelgrid(creechur.filename,creechur.maxResolution)
        updateImage()

def updateRenderText():
    renderText.value =f"Visually in: {maxSize}px, {repeatTime} ms between frames"

def updateResolutionText():
    maxResText.value = f"Actual Max Pixel Size: {creechur.maxResolution}px"

creechur=Pixelgrid("_internal/sprites/ship.png")

myApp = App(title="the app",bg="#4E6E58",width=700,height=600)
myApp.text_color=textColor

menu = MenuBar(myApp,
               toplevel=["File","Settings","Help"],
               options=[
                   [["New Image",selectFile],
                    ["Reset Image",resetImage]
                    ],

                   [["Actual Pixel Size",changeResolution],
                    ["Visual Pixel Size",updateSize],
                    ["Time Between Frames",frameTime]
                    ],

                   [["View on Github",githubLink]]
               ]
               )




title = Text(myApp,"sort image!",size=24)

pic = Picture(myApp,image=creechur.image)
updateImage()

idleBox = Box(myApp,layout="grid")

startButton = PushButton(idleBox,command=playSort,
                         text="Click to Start!",
                         image="_internal/sprites/PlayButton.png",
                         grid=[0,0],
                         width=buttonSize,height=buttonSize)
nextFrameButton = PushButton(idleBox,command=nextFrame,
                             text="next frame",
                             image="_internal/sprites/nextButton.png",
                             grid=[1,0],
                             width=buttonSize,height=buttonSize)
fileButton = PushButton(idleBox,command=selectFile,
                        text="Select Image",
                        image="_internal/sprites/folderButton.png",
                        grid=[2,0],
                        width=buttonSize,height=buttonSize)

downloadButton = PushButton(idleBox,command=downloadCurrent,
                            text="Download Image",
                            image="_internal/sprites/downloadButton.png",
                            grid=[3,0],
                            width=buttonSize,height=buttonSize
                            )


runningBox = Box(myApp,layout="grid",visible=False)

stopButton = PushButton(runningBox,command=stopSort
                        ,text="stop",
                        image="_internal/sprites/cancelButton.png",
                        grid=[0,0],
                        width=buttonSize,height=buttonSize)


infoBox = Box(myApp,layout="grid",align="bottom")

infoText = Text(infoBox,
                text="Higher resolution and faster framerates\n   may cause window to freeze. adjust accordingly     ",
                grid=[0,0,1,2],size=12
                )
renderText = Text(infoBox,
                  grid=[1,0,1,1],
                  size=12
                  )
updateRenderText()

maxResText = Text(infoBox,
                  grid=[1,1,1,1],
                  size=12
                  )
updateResolutionText()




myApp.display()