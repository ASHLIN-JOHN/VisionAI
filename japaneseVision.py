import sys
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyautogui, pywhatkit, qrcode, pyjokes
import webbrowser
import os
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Vision: おはようございます...")
        speak("oyagosaimasu")
    elif 12 <= hour < 18:
        print("Vision:こんにちは...")
        speak("Konnichiwa")
    else:
        print("Vision: こんばんは。...")
        speak("Konbanwa")
    print("Vision: 私はビジョンです")
    speak("Watashi wa")
    print("Vision: どのようにお手伝いできるか教えてください?")
    speak("Doano yo ni otetsudai dekiru ka oshietekudasai")
class VisionAssistant:
    def commands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Vision:聞いてください ...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            print("Vision: ちょっと待ってください、先生...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Vision: さっき言ったね: {query}\n")
        except:
            print("Vision: Please Tell Me Again Sir...")
            speak("もう一度教えてください先生")
            query = "none"
        return query.lower()

    def screenshot(self):
        folderpath = 'D:\\hack\\vision\\screenshots'
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(folderpath, 'screenshot1.png'))
        print("スクリーンショットを撮る")
        speak("Sukurīnshotto o toru")
    def joke(self):
        joke = pyjokes.get_joke()
        print("Vision: " + joke)
        speak(joke)
    def read_screen(self):
        import pytesseract as pyt
        import cv2
        folderpath = 'D:\\hack\\vision\\reading'
        img_path = os.path.join(folderpath, 'img.png')
        screenshot = pyautogui.screenshot()
        screenshot.save(img_path)
        img = cv2.imread(img_path)
        pyt.pytesseract.tesseract_cmd = "C:\\Users\\Ashlin John\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        text = pyt.image_to_string(img)
        print("Vision: 画面テキストは:\n", text)
        speak(text)
        for word in text.split():
            speak(word)
            time.sleep(2)
    def getlost(self):
        speak("Sayonara!")
        exit()

    def youtube(self):
        print("Vision: Opening YouTube Sir...")
        speak("Opening YouTube Sir")
        webbrowser.open("https://www.youtube.com")
    def chrome(self):
        print("Vision: Opening Chrome Sir...")
        speak("Opening Chrome Sir")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def closechrome(self):
        print("Vision: Opening Chrome Sir...")
        speak("Closing Chrome Sir")
        os.system("taskkill /F /IM chrome.exe")

    def get_distance(self,place1, place2):
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
        import maps
        if destination in maps.locations:
            destination = maps.locations[destination]
            base_url = "https://www.google.com/maps/search/"
            query = destination.replace(" ", "+")
            webbrowser.open(base_url + query)
            time.sleep(5)
            x,y = 200,600
            pyautogui.leftClick(x,y)
            print("Vision: Navigation Is Under Live Sir")
            speak("Navigation Is Under Live Sir")

        else:
            print(f"Location '{destination}' not found in maps.py")
    def coding(self):
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

            elif "remove line" in command:
                pyautogui.hotkey('shift', 'end')  # Select the line
                pyautogui.press('backspace')

            elif "remove word" in command:
                pyautogui.press('backspace ')

            elif "next line" in command:
                pyautogui.hotkey('enter')

            elif "last line" in command:
                pyautogui.hotkey('ctrl','end')

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
        import webbrowser
        import pyautogui
        import time
        import pytesseract as pyt
        import cv2
        webbrowser.open("https://chat.openai.com/")
        time.sleep(5)
        pyautogui.click(500, 500)
        pyautogui.write("Hello, ChatGPT!", interval=0.1)
        pyautogui.press("enter")
        time.sleep(10)
        screenshot = pyautogui.screenshot()
        folderpath = 'D:\\hack\\vision\\chatgpt'
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
        speak("Please enter the name for the QR code Sir.")
        qr_name = input("Vision: Enter The Name For The QR Code: ")
        speak("Please enter the data for the QR code Sir.")
        qr_data = input("Vision: Enter The Data For The QR Code: ")
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(os.path.join("D:\\Vision\\qrcodes", qr_name + ".png"))
        speak("QR code created successfully, Sir.")

    def read_whatsapp_messages(self):
        import cv2,pytesseract as pyt
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(10)
        folderpath = 'D:\\hack\\vision\\reading'
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
    def type_text(self):
        speak("Tell me what I need to write Sir")
        while True:
            text = self.commands()
            if text == 'finish typing':
                speak("Done Sir")
                break
            else:
                pyautogui.write(text)

    def play(self):
        query = self.commands()
        music = query.replace('play', '')
        speak('Playing ' + music)
        pywhatkit.playonyt(music)

    def run(self):
        wishings()
        while True:
            query = self.commands()
            if 'time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                print(f"Vision: Sir, The Time Is {strTime}")
                speak(f"Sir, The Time Is {strTime}")
            elif 'open chrome' in query:
                self.chrome()
            elif 'close chrome' in query:
                self.closechrome()
            elif 'open disord' in query:
                os.open("C:\\Users\\Ashlin John\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
            elif 'open outlook' in query:
                os.open("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
            elif 'open power point' in query:
                os.open("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            elif 'open excel' in query:
                os.open("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

            elif 'open ai' in query:
                self.open_chatgpt_and_read()
            elif 'blind code' in query:
                self.coding()
            elif 'open youtube' in query:
                self.youtube()
            elif 'what is' in query or 'tell me about' in query:
                speak("Searching In My Data Sir...")
                try:
                    query = query.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
                    results = wikipedia.summary(query, sentences=3)
                    speak("According To My Data")
                    print("Vision: " + results)
                    speak(results)
                    time.sleep(2)
                except:
                    speak("No Results Found")
                    print("Vision: No Results Found")
                    time.sleep(2)

            elif 'play' in query:
                self.play()

            elif 'distance from' in query:
                try:
                    import maps
                    places = query.replace("distance from", "").strip()
                    place1, place2 = places.split(" to ")
                    distance = self.get_distance(place1.strip(), place2.strip())
                    print(f"Vision: {distance}")
                    speak(distance)
                except:
                    print("Vision: Please say the command in format: 'distance from PLACE1 to PLACE2'.")
                    speak("Please say the command in format: 'distance from PLACE1 to PLACE2'.")

            elif 'type' in query:
                self.type_text()
            elif 'navigate to' in query:
                destination = query.replace("navigate to", "").strip()
                self.navigate_to(destination)
            elif "read message" in query:
                self.read_whatsapp_messages()
            elif 'in chatgpt' in query:
                self.open_chatgpt_and_read()

            elif 'minimise window' in query:
                pyautogui.hotkey('win', 'down')

            elif 'maximize window' in query:
                pyautogui.hotkey('win', 'up')

            elif 'close window' in query:
                pyautogui.hotkey('alt', 'f4')

            elif 'go to home' in query:
                pyautogui.hotkey('win', 'd')

            elif 'get lost' in query:
                self.getlost()
            elif "read screen" in query:
                screen_text = self.read_screen()
                print(f"Vision: Screen text is:\n{screen_text}")
                speak(f"Screen text is {screen_text}")
            elif 'screenshot' in query:
                self.screenshot()
            elif 'qr' in query:
                self.create_qr_code()
            elif 'who are you' in query:
                print("I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")
                speak("I'm Vision, an AI assistant ready to help you with information, writing, navigation, programming and Conversation.")
            elif 'joke' in query:
                self.joke()
            else:
                print("Vision: Command not recognized, please try again.")
                speak("")
                continue

if __name__ == '__main__':
    while True:
        try:
            assistant = VisionAssistant()
            assistant.run()
        except Exception as e:
            print(f"Vision encountered an error: {e}")
            speak("An error occurred, restarting the assistant.")
            time.sleep(2)

