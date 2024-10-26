#SIMPLE CALCULATOR

import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np


class Button:
    def __init__(self,pos, width, height,value):

        self.pos=pos
        self.width=width
        self.height=height
        self.value=value

    def draw(self,frame):
        # Draw rectangles (ensure they are in a visible area)
        cv2.rectangle(frame, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height), (225,225,225), cv2.FILLED)  # Blue rectangle with thickness 2
        cv2.rectangle(frame, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height), 3)  # Green rectangle with thickness 2
        cv2.putText(frame, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self,x,y,frame):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225),
                          cv2.FILLED)
            cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          3)
            cv2.putText(frame, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0,0,0), 5)
            return True
        else:
            return False

def smooth_hand_positions(positions, alpha=0.5):
    smoothed_positions = np.copy(positions[0])
    for pos in positions[1:]:
        smoothed_positions = alpha * np.array(pos) + (1 - alpha) * smoothed_positions
    return smoothed_positions

# Open the laptop camera (usually 0 is the default camera)
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8 )

#creating buttons
buttonListValues=[['7','8','9','*'],
                  ['4','5','6','+'],
                  ['1','2','3','-'],
                  ['0','/','.','=','C'],]

buttonList=[]
for x in range(4):
    for y in range(4):
       xpos=x*100+800
       ypos=y*100+150
       buttonList.append(Button((xpos,ypos),100,100,buttonListValues[y][x]))

#variables
myEquation=""
delayCounter =0


if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break
    # detection hands
    hands, frame = detector.findHands(frame)


    # creating buttons
    cv2.rectangle(frame, (800, 50), (1200,  150), (225, 225, 225),
                  cv2.FILLED)
    cv2.rectangle(frame, (800, 50), (1200, 150), (50, 50, 50), 3)

    # displaying the text
    cv2.putText(frame, myEquation, (820, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    for button in buttonList:
        button.draw(frame)

    # Check for hands and process clicks
    if hands:
          lmList = hands[0]['lmList']

          # Extract x, y coordinates of the tip of the index finger (landmark 8)
          x1, y1 = lmList[8][:2]
          x2, y2 = lmList[12][:2]

          # Calculate the distance between index finger tip and middle finger tip
          length, info, frame = detector.findDistance((x1, y1), (x2, y2), frame)

          # Check if any button is clicked
          if length < 90:
              for i, button in enumerate(buttonList):
                  if button.checkClick(x1, y1, frame) and delayCounter == 0:
                      myValue = buttonListValues[int(i % 4)][int(i / 4)]
                      if myValue == '=':
                          try:
                              myEquation = str(eval(myEquation))  # Evaluate the equation safely
                          except:
                              myEquation = "Error"
                      elif myValue == 'C':
                          myEquation = ""  # Clear the equation
                      else:
                          myEquation += myValue
                      delayCounter = 1

    # section to avoid duplicates
    if delayCounter!=0:
        delayCounter+=1
        if delayCounter>10:
            delayCounter=0



    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()



#SCIENTIFIC CALCULATOR

import cv2
from cvzone.HandTrackingModule import HandDetector
import math

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, frame):
        cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), 3)
        cv2.putText(frame, self.value, (self.pos[0] + 10, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y, frame):
        margin = 2  # Adding a small margin for easier clicking
        if (self.pos[0] - margin < x < self.pos[0] + self.width + margin and
                self.pos[1] - margin < y < self.pos[1] + self.height + margin):
            cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225),
                          cv2.FILLED)
            cv2.rectangle(frame, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 3)
            cv2.putText(frame, self.value, (self.pos[0] + 10, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0),
                        2)
            print(f"Clicked on {self.value}")  # Debugging statement
            return True
        return False

# Open the laptop camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

# Define buttons for scientific calculator
buttonListValues = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['sqrt', 'pow', 'log', 'ln'],
    ['sin', 'cos', 'tan', 'C']
]

buttonList = []
button_size = 80
for x in range(4):
    for y in range(6):
        if y < 4:
            xpos = x * button_size + 800
            ypos = y * button_size + 150
        else:
            xpos = x * button_size + 800
            ypos = (y - 4) * button_size + 150+310
        value = buttonListValues[y][x]
        buttonList.append(Button((xpos, ypos), button_size, button_size, value))

# Variables
myEquation = ""
delayCounter = 0

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Detect hands
    hands, frame = detector.findHands(frame, flipType=False)

    # creating buttons
    cv2.rectangle(frame, (800, 50), (1200, 150), (225, 225, 225),
                  cv2.FILLED)
    cv2.rectangle(frame, (800, 50), (1200, 150), (50, 50, 50), 3)

    # displaying the text
    cv2.putText(frame, myEquation, (820, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    for button in buttonList:
        button.draw(frame)


    # Check for hands and process clicks
    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmList[8][:2]
        x2, y2 = lmList[12][:2]
        length, info, frame = detector.findDistance((x1, y1), (x2, y2), frame)

        if length < 90:
            for i, button in enumerate(buttonList):
                if button.checkClick(x1, y1, frame) and delayCounter == 0:
                    # Calculate the correct row and column indices
                    col_index = i % 4  # column (0 to 3)
                    row_index = i // 4  # row (0 to 5)

                    try:
                        # Access the correct value from buttonListValues
                        myValue = buttonListValues[row_index][col_index]
                    except IndexError:
                        # This should not happen but it's good to handle any possible error
                        print(f"Error: Index ({row_index}, {col_index}) out of range for buttonListValues.")
                        continue  # Skip this iteration if there's an error

                    # Process the clicked button's value
                    if myValue == '=':
                        try:
                            myEquation = str(eval(myEquation))
                        except:
                            myEquation = "Error"
                    elif myValue == 'C':
                        myEquation = ""
                    elif myValue in ['sqrt', 'pow', 'log', 'ln', 'sin', 'cos', 'tan']:
                        print(f"Function {myValue} pressed.")  # Debugging statement
                        try:
                            if myValue == 'pow':
                                base, exp = map(float, myEquation.split(','))
                                myEquation = str(math.pow(base, exp))
                            elif myValue == 'log':
                                myEquation = str(math.log10(float(myEquation)))
                            elif myValue == 'ln':
                                myEquation = str(math.log(float(myEquation)))
                            elif myValue == 'sin':
                                myEquation = str(math.sin(math.radians(float(myEquation))))
                            elif myValue == 'cos':
                                myEquation = str(math.cos(math.radians(float(myEquation))))
                            elif myValue == 'tan':
                                myEquation = str(math.tan(math.radians(float(myEquation))))
                        except:
                            myEquation = "Error"
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # Section to avoid duplicates
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()



