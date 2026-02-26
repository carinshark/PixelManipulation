from guizero import App,Text,Picture,PushButton
from guizero import info,warn,error,yesno,question


def startButtonFunc():
    pic.image="sortedImages/output.jpg"

myApp = App(title="the app")

title = Text(myApp,"look my app",color="gray",size=24)

pic = Picture(myApp,image="images1/electricCat.jpeg")

startButton = PushButton(myApp,command=startButtonFunc)

myApp.display()