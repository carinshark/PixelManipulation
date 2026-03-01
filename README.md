# Welcome to the Pixel Sorter!

<img width="868" height="814" alt="image" src="https://github.com/user-attachments/assets/6d4ec4e0-bc83-4f43-981e-f91d7a64873e" />

## Dependencies (modules required)
(if youre running the python files directly)
- numpy
- guizero
- pillow 


### Menubar
File:
- New Image
  - same as button, prompts you to select a new image
- Reset Image
  - gets the same image from the original file location it's stored in

Settings:
- Actual Pixel Size
  - If an image is too big, it can cause a lot of lag. This automatically resizes the pixels to a maximum width/height (default is 100x100px)
- Visual Pixel Size
  - This is what you see on your screen. Since pixels are usually small, this feature scales the pixels to an easier visual point. This is also what it saves as when you click the save button.(default is 300x300px)
- Time Between Frames
  - This is the time the app waits between each frame it processes during the aanimation. Make this a larger number if your window is lagging too often and the visual animation does not update.

Help:
- View on Github
  - Leads to this repository



### Buttons

<img width="100" height="100" alt="downloadButton" src="https://github.com/user-attachments/assets/6f87a8ec-ece9-4dcb-9fef-731a8c1be94d" /> <br> Save Current Image

<img width="100" height="100" alt="nextButton" src="https://github.com/user-attachments/assets/88ffcb38-9c3b-420e-a65b-2a4728489396" /> <br> Go to next frame

<img width="100" height="100" alt="PlayButton" src="https://github.com/user-attachments/assets/104d7d43-4766-441c-b1bf-46ca6a7d10a3" /> <br> Play Animation

<img width="100" height="100" alt="folderButton" src="https://github.com/user-attachments/assets/acfa645d-c9f7-4e44-8104-e8e616130c4a" /> <br> Open New Image

<img width="100" height="100" alt="cancelButton" src="https://github.com/user-attachments/assets/366ae99b-07c6-44a6-8a52-b15dadf7b123" /> <br> Cancel Animation (You may have to keep clicking this for a while until it stops if the resolution you set was too high and it freezes the window.
