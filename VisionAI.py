import subprocess
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from visionmainfile import Ui_NARUTOAIUI
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer
import speech_recognition as sr
import cv2
import pytesseract as pyt
import pyttsx3
import datetime
import wikipedia
import pyautogui, pywhatkit, qrcode, pyjokes
import webbrowser
import os
import random
from PyQt5.QtCore import QObject, pyqtSignal, QThread
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        ui.terminalprint("Vision: Good Morning Sir...")
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        ui.terminalprint("Vision: Good Afternoon Sir...")
        speak("Good Afternoon sir!")
    else:
        ui.terminalprint("Vision: Good Evening Sir...")
        speak("Good Evening sir!")
    ui.terminalprint("Vision: I am Vision")
    speak("I am Vision")
    ui.terminalprint("Vision: Please Tell Me How May I Help You?")
    speak("Please tell me how may I help you?")

class Ui_Vision(QThread):
    def __init__(self):
        super(Ui_Vision, self).__init__()

    def run(self):
        self.runNaruto()


    def commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalprint("Vision: Listening Sir ...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            ui.terminalprint("Vision: Wait For Few Moments Sir...")
            query = r.recognize_google(audio, language = 'en-in')
            ui.terminalprint(f"Vision: You Just Said: {query}\n")
        except Exception as e:
            ui.terminalprint(e)
            ui.terminalprint("Vision: Please Tell Me Again Sir...")
            speak("Please Tell Me Again Sir")
            query = "none"
        return query

    def screenshot(self):
        folderpath = 'D:\\NARUTO\\screenshots'
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(folderpath, 'screenshot1.png'))
        ui.terminalprint("Taking Screenshot Sir")
        speak("Taking ScreenShot Sir")
        pyautogui.press('prtsc')

    def joke(self):
        joke = pyjokes.get_joke()
        ui.terminalprint("Vision: " + joke)
        speak(joke)

    def coding(self):
        """Function to assist with Python coding via voice commands"""
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.11\\IDLE (Python 3.11 64-bit).lnk")
        speak("Opening Python IDLE, please wait...")
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'n')
        speak("Sir, you can code now.")

        while True:
            import codes, inspect
            command = self.commands()

            if "print" in command:
                text_to_print = command.replace("print", "").strip()
                formatted_code = f'print("{text_to_print}")'
                pyautogui.write(formatted_code, interval=0.05)
                speak(f'Typed: {formatted_code}')

            elif "string print" in command:
                try:
                    text_to_print = command.split("string print ", 1)[1].strip()
                    formatted_code = f'print("{text_to_print}")'
                    pyautogui.write(formatted_code, interval=0.05)
                    speak(f'Typed: {formatted_code}')
                except Exception as e:
                    print(f"Error in string print command: {e}")
                    speak("Sorry, there was an error processing the command.")

            elif "create a for loop" in command:
                try:
                    parts = command.split()
                    loop_var = parts[4]
                    x = int(parts[7])
                    y = int(parts[9])
                    pyautogui.write(f"for {loop_var} in range({x}, {y}):\n    ", interval=0.1)
                    speak(f"Created a for loop with variable {loop_var} from {x} to {y}.")
                except Exception as e:
                    print(f"Error creating loop: {e}")
                    speak("Sorry, there was an error creating the for loop.")

            elif "create a while loop" in command:
                try:
                    parts = command.split()
                    loop_var = parts[4]  # Extract the loop variable
                    condition_value = parts[7]  # Extract the condition value

                    pyautogui.write(f"while {loop_var} < {condition_value}:\n    ", interval=0.1)
                    speak(f"Created a while loop with condition {loop_var} less than {condition_value}.")
                except Exception as e:
                    print(f"Error creating while loop: {e}")
                    speak("Sorry, there was an error creating the while loop.")

            elif "create an if" in command:
                try:
                    parts = command.split("create an if ", 1)[1]  # Extract condition after "create an if"
                    pyautogui.write(f"if {parts}:\n    ", interval=0.1)
                    speak(f"Created an if statement with condition {parts}.")
                except Exception as e:
                    print(f"Error creating if statement: {e}")
                    speak("Sorry, there was an error creating the if statement.")

            elif "put variable" in command:
                var_name = command.replace("put variable", "").strip()
                if var_name:
                    formatted_code = f"{var_name} = "
                    pyautogui.write(formatted_code, interval=0.05)
                    speak(f"Assigned variable {var_name}")

            elif "connect variable" in command:
                try:
                    variable_name = command.split("connect variable ", 1)[1].strip()
                    formatted_code = f'print({variable_name})'
                    pyautogui.write(formatted_code, interval=0.05)
                    speak(f'Typed: {formatted_code}')
                except Exception as e:
                    print(f"Error in connect variable command: {e}")
                    speak("Sorry, there was an error processing the command.")

            elif "remove line" in command:
                pyautogui.hotkey('shift', 'end')  # Select the line
                pyautogui.press('backspace')

            elif "remove letter" in command:
                pyautogui.press('backspace')

            elif "show output" in command:
                pyautogui.press('f5')

            elif "next line" in command:
                pyautogui.hotkey('enter')

            elif "last line" in command:
                pyautogui.hotkey('ctrl', 'end')

            elif "put input" in command:
                pyautogui.write('input("Enter value: ")', interval=0.05)

            elif "put integer input" in command:
                pyautogui.write('int(input("Enter number: "))', interval=0.05)

            elif "palindrome function" in command:
                pyautogui.write(inspect.getsource(codes.palindrome), interval=0.05)

            elif "factorial function" in command:
                pyautogui.write(inspect.getsource(codes.factorial), interval=0.05)

            elif "fibonacci function" in command:
                pyautogui.write(inspect.getsource(codes.fibonacci), interval=0.05)

            elif "prime function" in command:
                pyautogui.write(inspect.getsource(codes.is_prime), interval=0.05)

            elif "matrix addition function" in command:
                pyautogui.write(inspect.getsource(codes.add_matrices), interval=0.05)

            elif "matrix subtraction function" in command:
                pyautogui.write(inspect.getsource(codes.subtract_matrices), interval=0.05)

            elif "matrix multiplication function" in command:
                pyautogui.write(inspect.getsource(codes.multiply_matrices), interval=0.05)

            elif "inverse matrix function" in command:
                pyautogui.write(inspect.getsource(codes.inverse_matrix), interval=0.05)

            elif "transpose matrix function" in command:
                pyautogui.write(inspect.getsource(codes.transpose_matrix), interval=0.05)

            elif "even numbers function" in command:
                pyautogui.write(inspect.getsource(codes.even_numbers), interval=0.05)

            elif "odd numbers function" in command:
                pyautogui.write(inspect.getsource(codes.odd_numbers), interval=0.05)

            elif "leap year function" in command:
                pyautogui.write(inspect.getsource(codes.is_leap_year), interval=0.05)

            elif "gcd function" in command:
                pyautogui.write(inspect.getsource(codes.gcd), interval=0.05)

            elif "lcm function" in command:
                pyautogui.write(inspect.getsource(codes.lcm), interval=0.05)

            elif "sum of digits function" in command:
                pyautogui.write(inspect.getsource(codes.sum_of_digits), interval=0.05)

            elif "reverse number function" in command:
                pyautogui.write(inspect.getsource(codes.reverse_number), interval=0.05)

            elif "armstrong number function" in command:
                pyautogui.write(inspect.getsource(codes.armstrong_number), interval=0.05)

            elif "perfect number function" in command:
                pyautogui.write(inspect.getsource(codes.perfect_number), interval=0.05)

            elif "finish coding" in command:
                speak("Done, sir.")
                break

    def getlost(self):
        speak("Goodbye Sir!")
        exit()

    def Youtube(self):
        ui.terminalprint("Vision: Opening Youtube Sir...")
        speak("Opening youtube Sir")
        youtube_url = "https://www.youtube.com"
        os.startfile(youtube_url)
        while True:
            ytquery = self.commands().lower()
            if "close" in ytquery:
                ui.terminalprint("Vision: Closing Youtube Sir")
                speak("closing youtube sir")
                pyautogui.hotkey('alt', 'f4')
                return
    def open_chatgpt_and_read(self):
        """Function to open ChatGPT, send a message, and read the response"""
        folderpath = 'D:\\hack\\vision\\chatgpt'
        os.makedirs(folderpath, exist_ok=True)

        webbrowser.open("https://chat.openai.com/")
        time.sleep(5)
        pyautogui.click(500, 500)
        pyautogui.write("Hello, ChatGPT!", interval=0.1)
        pyautogui.press("enter")
        time.sleep(10)

        screenshot = pyautogui.screenshot()
        img_path = os.path.join(folderpath, 'chat_response.png')
        screenshot.save(img_path)

        img = cv2.imread(img_path)
        pyt.pytesseract.tesseract_cmd = "C:\\Users\\Ashlin John\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        text = pyt.image_to_string(img)

        response_lines = text.split("\n")
        response = "\n".join(response_lines[2:])
        print("ChatGPT's Response:\n", response)

        for word in response.split():
            speak(word)
            time.sleep(0.5)
    def chrome(self):
        ui.terminalprint("Vision: Opening Chrome Sir...")
        speak("Opening Chrome Sir")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        while True:
            chromequery = self.commands().lower()
            if "close" in chromequery:
                ui.terminalprint("Vision: Closing Chrome Sir")
                speak("closing chrome sir")
                pyautogui.hotkey('alt', 'f4')
                return

            elif "type" in chromequery:
                type()

    def create_qr_code(self):
        speak("Please enter the name for the QR code Sir.")
        qr_name = input("Vision: Enter The Name For The QR Code: ")
        speak("Please enter the data for the QR code Sir.")
        qr_data = input("Vision: Enter The Data For The QR Code: ")
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(os.path.join("D:\\NARUTO\\qrcodes", qr_name + ".png"))
        speak("QR code created successfully, Sir.")
        return

    def read_screen(self):
        """Function to capture screen and read its text content"""
        folderpath = 'D:\\hack\\vision\\reading'
        os.makedirs(folderpath, exist_ok=True)
        img_path = os.path.join(folderpath, 'img.png')

        screenshot = pyautogui.screenshot()
        screenshot.save(img_path)
        img = cv2.imread(img_path)

        pyt.pytesseract.tesseract_cmd = "C:\\Users\\Ashlin John\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        text = pyt.image_to_string(img)

        print("Vision: Screen text is:\n", text)
        speak(text)

        for word in text.split():
            speak(word)
            time.sleep(2)

        return text


    def type(self):
        speak("tell me what i need to write sir")
        while True:
            writeinnotepad = self.commands()
            if writeinnotepad == 'finish typing':
                speak("Done Sir")

            else:
                pyautogui.write(writeinnotepad)

    def read_whatsapp_messages(self):
        """Function to read WhatsApp messages"""
        folderpath = 'D:\\hack\\vision\\reading'
        os.makedirs(folderpath, exist_ok=True)

        webbrowser.open("https://web.whatsapp.com")
        time.sleep(10)

        img_path = os.path.join(folderpath, 'img.png')
        region = (100, 200, 400, 200)
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(img_path)

        img = cv2.imread(img_path)
        pyt.pytesseract.tesseract_cmd = "C:\\Users\\Ashlin John\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        text = pyt.image_to_string(img)

        speak(text)
        print("Vision: Screen text is:\n", text)

        for word in text.split():
            print(word)
            time.sleep(2)

    def play(self):
        self.query = self.commands().lower()
        music = self.query.replace('play', '')
        speak('playing' + music)

    def get_distance(self, place1, place2):
        """Function to calculate distance between two places"""
        from geopy.distance import geodesic
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="geoapi")
        # Get latitude and longitude of both places
        location1 = geolocator.geocode(place1)
        location2 = geolocator.geocode(place2)

        if location1 and location2:
            coords1 = (location1.latitude, location1.longitude)
            coords2 = (location2.latitude, location2.longitude)

            # Calculate distance
            distance_km = geodesic(coords1, coords2).kilometers
            return f"Distance between {place1} and {place2} is {distance_km:.2f} km"
        else:
            return "Could not find one or both locations."

    def navigate_to(self, destination):
        """Function to navigate to a location using Google Maps"""
        import maps
        if destination in maps.locations:
            destination = maps.locations[destination]
            base_url = "https://www.google.com/maps/search/"
            query = destination.replace(" ", "+")
            webbrowser.open(base_url + query)
            time.sleep(5)
            x, y = 200, 600
            pyautogui.leftClick(x, y)
            print("Vision: Navigation Is Under Live Sir")
            speak("Navigation Is Under Live Sir")
        else:
            print(f"Location '{destination}' not found in maps.py")
    def runNaruto(self):
        wishings()
        try:
            while True:
                self.query = self.commands().lower()
                if 'time' in self.query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    ui.terminalprint(f"Vision: Sir The Time Is {strTime}")
                    speak(f"Sir,The Time Is {strTime}")

                elif 'open chrome' in self.query:
                    self.chrome()

                elif 'open youtube' in self.query:
                    self.Youtube()

                elif 'blind code' in self.query:
                    self.coding()

                elif 'minimise window' in self.query:
                    pyautogui.hotkey('win', 'down')
                elif 'open chat gpt' in self.query:
                    webbrowser.open("https://chat.openai.com/")

                # Application commands
                elif 'open discord' in self.query:
                    os.startfile("C:\\Users\\Ashlin John\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
                elif 'open outlook' in self.query:
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
                elif 'open PowerPoint' in self.query:
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                elif 'open Excel' in self.query:
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                elif 'open ai' in self.query:
                    self.open_chatgpt_and_read()

                elif 'maximize window' in self.query:
                    pyautogui.hotkey('win', 'up')
                elif 'close window' in self.query:
                    pyautogui.hotkey('alt', 'f4')
                elif 'go to home' in self.query:
                    pyautogui.hotkey('win', 'd')
                elif 'shutdown' in query or 'turn off' in query:
                    speak("Shutting down the system in 5 seconds. Goodbye!")
                    os.system("shutdown /s /t 5")
                elif 'log off' in query or 'sign out' in query:
                    speak("Logging off in 5 seconds.")
                    os.system("shutdown /l")
                elif "sleep for" in self.query:
                    self.sleep(self.query)

                elif 'search' in self.query:
                    speak("Searching In My Data Sir...")
                    try:
                        self.query = self.query.replace("wikipedia","")
                        results = wikipedia.summary(self.query, sentences=3)
                        speak("According To My Data")
                        ui.terminalprint("Vision: " + results)
                        speak(results)
                    except:
                        speak("No Results Found")
                        ui.terminalprint("Vision: No Results Found")

                elif 'play' in self.query:
                    self.play()

                elif "create new folder named" in self.query:
                    try:
                        folder_name = self.query.split("create new folder named ", 1)[1].strip()
                        os.makedirs(folder_name, exist_ok=True)
                        speak(f"Folder named {folder_name} has been created, sir.")
                    except Exception as e:
                        print(f"Error creating folder: {e}")
                        speak("Sorry, there was an error creating the folder.")

                elif 'type' in self.query:
                    type()

                elif 'get lost' in self.query:
                    self.getlost()
                    self.exit()

                elif 'navigate to' in self.query:
                    destination = self.query.replace("navigate to", "").strip()
                    self.navigate_to(destination)

                elif 'distance from' in self.query:
                    try:
                        import maps
                        places = self.query.replace("distance from", "").strip()
                        place1, place2 = places.split(" to ")
                        distance = self.get_distance(place1.strip(), place2.strip())
                        print(f"Vision: {distance}")
                        speak(distance)
                    except Exception as e:
                        print(f"Error calculating distance: {e}")
                        print("Vision: Please say the command in format: 'distance from PLACE1 to PLACE2'.")
                        speak("Please say the command in format: 'distance from PLACE1 to PLACE2'.")
                elif 'navigate to' in self.query:
                    destination = self.query.replace("navigate to", "").strip()
                    self.navigate_to(destination)

                elif 'screenshot' in self.query:
                    self.screenshot()

                elif 'talk in japanese' in self.query:
                    import japaneseVision
                    subprocess.run("python","japaneseVision.py")

                elif 'talk in tamil' in self.query:
                    import TamilVisionai
                    subprocess.run("python","TamilVisionai.py")

                elif 'qr' in self.query.lower():
                    self.create_qr_code()
                elif "read screen" in self.query:
                    self.read_screen()
                elif 'joke' in self.query:
                    self.joke()

                else:
                    print("Vision: Command not recognized, please try again.")
                    speak("Command not recognized, please try again.")
        except Exception as e:
            print(e)

startExecution = Ui_Vision()

class UI_Naruto(QMainWindow):
    def __init__(self):
        super(UI_Naruto, self).__init__()
        self.narutoUI = Ui_NARUTOAIUI()
        self.narutoUI.setupUi(self)

        self.narutoUI.startbutton.clicked.connect(self.manualcodefromterminal)
        self.narutoUI.exitbutton.clicked.connect(self.close)
        self.runmovies()

        # Create a QTimer instance
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_terminal)
        self.timer.start(10000)  # 10000 milliseconds = 10 seconds

    def runmovies(self):
        self.narutoUI.logoMovie = QtGui.QMovie("D:\\NARUTO\\gui\\uzumkai logo.gif")
        self.narutoUI.logo.setMovie(self.narutoUI.logoMovie)
        self.narutoUI.logoMovie.start()
        startExecution.start()

    def terminalprint(self, text):
        self.narutoUI.terminalbox.append(text)

    def manualcodefromterminal(self):
        if self.narutoUI.commandbox.text():
            cmd = self.narutoUI.commandbox.text()
            self.narutoUI.commandbox.clear()
            self.narutoUI.terminalbox.setText(f"Vision: You Typed--> {cmd.capitalize()}")

            if cmd == 'exit':
                self.close()
            elif cmd == 'help':
                self.terminalprint("i am ashlin")
            else:
                pass

    def clear_terminal(self):
        self.narutoUI.terminalbox.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI_Naruto()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI_Naruto()
    ui.show()
    sys.exit(app.exec_())
