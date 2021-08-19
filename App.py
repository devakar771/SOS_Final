# import the opencv library
import cv2
import tensorflow as tf  
from gtts import gTTS
import os

# define a video capture object
vid = cv2.VideoCapture(0)
model = tf.keras.models.load_model("\models")

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    key = cv2.waitKey(0)
    if key == ord("q") or key == ord("s"):
        break

frame = frame.resize((250,250))
caption = model.predict(frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

language = 'en'
myobj = gTTS(text=caption, lang=language, slow=False)
# Saving the converted audio in a mp3 file 
myobj.save("speak.mp3")
# Playing the converted file
os.system("mpg321 speak.mp3")
