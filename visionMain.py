import sys
import os
import time
import datetime
import webbrowser

# GUI and Threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread
from OS.mainGUIFile import Ui_visiongui

# Voice and Text Processing
import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import pytesseract as pyt

# Utilities
import pyautogui
import pywhatkit
import qrcode
import cv2

# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()


def wishings():
    """Function to greet user based on time of day"""
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Vision: Good Morning Sir...")
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        print("Vision: Good Afternoon Sir...")
        speak("Good Afternoon sir!")
    else:
        print("Vision: Good Evening Sir...")
        speak("Good Evening sir!")

    print("Vision: I am Vision")
    speak("I am Vision")
    print("Vision: Please Tell Me How May I Help You?")
    speak("Please tell me how may I help you?")


class LoginWindow(QThread):
    """Main class handling voice commands and assistant functionality"""

    def __init__(self):
        super(LoginWindow, self).__init__()  # Greet the user when starting

    def commands(self):
        """Function to listen for voice commands and convert to text"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Vision: Listening Sir ...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            print("Vision: Wait For Few Moments Sir...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Vision: You Just Said: {query}\n")
        except:
            print("Vision: Please Tell Me Again Sir...")
            speak("Please Tell Me Again Sir")
            query = "none"

        return query.lower()

    def screenshot(self):
        """Function to take and save a screenshot"""
        folderpath = 'D:\\hack\\vision\\screenshots'
        os.makedirs(folderpath, exist_ok=True)
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(folderpath, 'screenshot1.png'))
        print("Taking Screenshot Sir")
        speak("Taking Screenshot Sir")

    def joke(self):
        """Function to tell a joke"""
        joke = pyjokes.get_joke()
        print("Vision: " + joke)
        speak(joke)

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

    def getlost(self):
        """Function to exit the program"""
        speak("Goodbye Sir!")
        exit()

    def youtube(self):
        """Function to open YouTube"""
        print("Vision: Opening YouTube Sir...")
        speak("Opening YouTube Sir")
        webbrowser.open("https://www.youtube.com")

    def chrome(self):
        """Function to open Chrome browser"""
        print("Vision: Opening Chrome Sir...")
        speak("Opening Chrome Sir")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def closechrome(self):
        """Function to close Chrome browser"""
        print("Vision: Closing Chrome Sir...")
        speak("Closing Chrome Sir")
        os.system("taskkill /F /IM chrome.exe")

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

    def create_qr_code(self):
        """Function to create a QR code"""
        qr_folder = "D:\\Vision\\qrcodes"
        os.makedirs(qr_folder, exist_ok=True)

        speak("Please enter the name for the QR code Sir.")
        qr_name = input("Vision: Enter The Name For The QR Code: ")

        speak("Please enter the data for the QR code Sir.")
        qr_data = input("Vision: Enter The Data For The QR Code: ")

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(os.path.join(qr_folder, qr_name + ".png"))

        speak("QR code created successfully, Sir.")

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
    def type_text(self):
        """Function to type text as dictated by voice"""
        speak("Tell me what I need to write Sir")

        while True:
            text = self.commands()
            if text == 'finish typing':
                speak("Done Sir")
                break
            else:
                pyautogui.write(text)

    def shutdown(self):
        """Function to shut down the computer"""
        speak("Shutting down, sir.")
        os.system("shutdown /s /t 42")

    def sleep(self, command):
        """Function to pause the assistant for a specified duration"""
        try:
            parts = command.split("sleep for ", 1)[1].split()[0]
            seconds = int(parts)
            speak(f"Sleeping for {seconds} seconds, sir.")
            time.sleep(seconds)
            print("Vision: I am Back Sir...")
            speak("I am back sir")
        except Exception as e:
            print(f"Error in sleep command: {e}")
            speak("Sorry, there was an error processing the sleep command.")

    def play(self):
        """Function to play music or videos on YouTube"""
        query = self.commands()
        music = query.replace('play', '')
        speak('Playing ' + music)
        pywhatkit.playonyt(music)

    def runVision(self):
        """Main function to run the Vision assistant"""
        while True:  # Continuous loop to keep listening for commands
            self.query = self.commands().lower()

            # Time related commands
            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                print(f"Vision: Sir, The Time Is {strTime}")
                speak(f"Sir, The Time Is {strTime}")

            # Browser related commands
            elif 'open chrome' in self.query:
                self.chrome()
            elif 'close chrome' in self.query:
                self.closechrome()
            elif 'open youtube' in self.query:
                self.youtube()
            elif 'open chat gpt' in self.query:
                webbrowser.open("https://chat.openai.com/")

            # Application commands
            elif 'open discord' in self.query:
                os.startfile(
                    "C:\\Users\\Ashlin John\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
            elif 'open outlook' in self.query:
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
            elif 'open powerpoint' in self.query:
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            elif 'open excel' in self.query:
                os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            elif 'open ai' in self.query:
                self.open_chatgpt_and_read()

            # Coding assistance
            elif 'blind code' in self.query:
                self.coding()

            # File management
            elif "create new folder named" in self.query:
                try:
                    folder_name = self.query.split("create new folder named ", 1)[1].strip()
                    os.makedirs(folder_name, exist_ok=True)
                    speak(f"Folder named {folder_name} has been created, sir.")
                except Exception as e:
                    print(f"Error creating folder: {e}")
                    speak("Sorry, there was an error creating the folder.")

            # Information retrieval
            elif 'what is' in self.query or 'tell me about' in self.query:
                speak("Searching In My Data Sir...")
                try:
                    query = self.query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
                    results = wikipedia.summary(query, sentences=3)
                    speak("According To My Data")
                    print("Vision: " + results)
                    speak(results)
                    time.sleep(2)
                except:
                    speak("No Results Found")
                    print("Vision: No Results Found")
                    time.sleep(2)

            # Media commands
            elif 'play' in self.query:
                self.play()

            # Navigation and location
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

            # Text input/output
            elif 'type' in self.query:
                self.type_text()
            elif "read message" in self.query:
                self.read_whatsapp_messages()
            elif 'in chatgpt' in self.query:
                self.open_chatgpt_and_read()
            elif "read screen" in self.query:
                self.read_screen()

            # Window management
            elif 'minimise window' in self.query:
                pyautogui.hotkey('win', 'down')
            elif 'maximize window' in self.query:
                pyautogui.hotkey('win', 'up')
            elif 'close window' in self.query:
                pyautogui.hotkey('alt', 'f4')
            elif 'go to home' in self.query:
                pyautogui.hotkey('win', 'd')

            # System commands
            elif "sleep for" in self.query:
                self.sleep(self.query)
            elif 'get lost' in self.query:
                self.getlost()
            elif 'screenshot' in self.query:
                self.screenshot()
            elif 'shutdown' in self.query:
                self.shutdown()
            elif 'qr' in self.query:
                self.create_qr_code()

            # Information about Vision
            elif 'who are you' in self.query:
                print(
                    "I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")
                speak(
                    "I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")
            elif 'what can you do' in self.query:
                print(
                    "I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")
                speak(
                    "I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")

            # Entertainment
            elif 'joke' in self.query:
                self.joke()

            # Exit commands
            elif 'exit' in self.query or 'quit' in self.query:
                speak("Goodbye, sir!")
                exit()

            # Unrecognized command
            else:
                print("Vision: Command not recognized, please try again.")
                speak("Command not recognized, please try again.")


class Ui_VISION(QMainWindow):
    """UI class for the Vision assistant"""

    def __init__(self):
        super(Ui_VISION, self).__init__()
        self.VisionUI = Ui_visiongui()
        self.VisionUI.setupUi(self)
        self.query = ""  # Initialize query attribute
        wishings()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_VISION()
    ui.show()
    sys.exit(app.exec_())