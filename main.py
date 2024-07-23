import pyautogui
import keyboard
import pytesseract
import cv2
import numpy as np
import string

def main():
    # Move mouse to textbox and press 'p'
    print("Please move your mouse to the textbox and press 'p'")
    while True:
        try:
            if keyboard.is_pressed('p'):
                textbox_pos = pyautogui.position()
                print("TextBox Position recorded")
                break
        except:
            break

    # Move mouse to commission name textbox and press 'o'
    print("Please move your mouse to the Commission name textbox and press 'o'")
    while True:
        try:
            if keyboard.is_pressed('o'):
                commission_name_pos = pyautogui.position()
                print("Commission Name Position recorded")
                break
        except:
            break

    # Move mouse to dropdown field and press 'i'
    print("Please move your mouse to the Left of the Commission Name dropdown and press 'i'")
    while True:
        try:
            if keyboard.is_pressed('i'):
                drop_down_pos = pyautogui.position()
                print("Commission Name Position recorded")
                break
        except:
            break

    ###
    # Main Sequence
    ###

    # Define Input File
    input_file = open("./input/example-policy#.txt", "r")

    # Iterate through each line in the input file
    for line in input_file:
        # Click on textbox
        pyautogui.click(textbox_pos)

        # Press 'ctrl + a' to select all
        pyautogui.hotkey('ctrl', 'a')

        # Press 'delete' to clear textbox
        pyautogui.press('delete')

        # Enter the line
        pyautogui.typewrite(line)

        # Click on commission name textbox
        pyautogui.click(commission_name_pos)

        # Hover over the dropdown
        pyautogui.moveTo(drop_down_pos)

        # Take Screenshot and identify region
        try:
            a = pyautogui.locateOnScreen('./images/image_fullres.png', grayscale=False, confidence=0.75)
            pyautogui.screenshot('./images/comm_name.png', region=(int(a[0]), int(a[1]), int(a[2]), int(a[3])))
             # Wait for screenshot to be taken
            pyautogui.sleep(1)
        except:
            continue

        # Identify text from screenshot
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # Transform Image
        img = cv2.imread('./images/comm_name.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invert = gray

        # Extract text from image
        data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
        print(data)

        # Open and append to output file
        output_file = open("./output/output.txt", "a")
        output_file.write(data.translate(str.maketrans('', '', string.punctuation)))
        output_file.close()

    # Close input file
    input_file.close()

if __name__ == "__main__":
    main()