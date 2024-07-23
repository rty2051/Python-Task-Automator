"PDF Scraper" Instruction Manual

1. Installing the Tesseract Library

* https://github.com/UB-Mannheim/tesseract/wiki
* Press "tesseract-ocr-w64-setup-5.4.0.20240606.exe (64 bit)" to install the latest version of Tesseract
  Once installed run the setup program and take the note of the installation path.
  -> Should look something like (C:\Program Files\Tesseract-OCR)

* Once completed hit the windows icon on your keyboard and search "System Variables".
  Navigate to "Edit the system environment variables" -> "Environment Variables" -> Select "PATH" -> "Edit..." -> "New" -> Paste your installation path mentioned above.
* Once done press "OK" -> "New..." and insert the information below for the following fields
      Variable Name:  TESSDATAPREFIX
      Variable Value: installation path\tessdata
  Once done press "OK" for all windows

2. Installing dependenicies (Could be optional)

   - You may need to install the proper packages in order to run the script. Just run the following commands in a command terminal open to the location of this folder:

   ```
   pip install pyautogui
   pip install keyboard
   pip install pytesseract
   pip install opencv-python
   pip install numpy
   ```
3. Running the script

   - Run the following command in any command prompt open to the file location

   ```
   py main.py
   ```
