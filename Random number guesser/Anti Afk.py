# automatic number guesser bot messages sender by K0-M1

import pyautogui, time, random

time.sleep(float(5))    # time to open the chat application

b = int(1)


while 0 == 0:
    f = open('Text.txt', 'r')
    for word in f:
        if len(word) >= 1:
            a = str(word)
            number = random.randint(1, 5000)
            fixed = str(number)
            word = (str(a) * int(b))
            pyautogui.typewrite(word + str(" "))    # Type the word taken from the file
            pyautogui.typewrite(fixed)      # Type a random number
            pyautogui.press('enter')    # Press the enter button
            time.sleep(float(3))    # Time between each message
        else:
            print("The selected word need to be more than 1 character")