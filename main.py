import pyttsx3
import datetime
import time
import webbrowser
from googleapiclient.discovery import build
from google.oauth2 import service_account

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def cal_day():
    day = datetime.datetime.today().weekday() + 1 
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    return day_dict.get(day, "Unknown Day")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()
    speak(f"Sup Jayden, it's {day} and the time is {t}. Here's everything that happened today:")
    get_appointments()

def open_website(command):
    website_dict = {
        "facebook": "facebook.com",
        "instagram": "instagram.com",
        "twitter": "twitter.com",
        "youtube": "youtube.com",
        "google": "google.com",
        "reddit": "reddit.com",
        "github": "github.com",
        "school": "calendar.google.com"
    }
    words = command.split()
    for word in words:
        if word.lower() in website_dict:
            url = f"https://{website_dict[word.lower()]}"
            print(f"Opening {url}...")
            speak(f"Opening {word}")
            webbrowser.open(url)
            return
        elif any(ext in word for ext in [".com", ".org", ".net", ".io"]):
            url = f"https://{word}" if not word.startswith("http") else word
            print(f"Opening {url}...")
            speak(f"Opening {word}")
            webbrowser.open(url)
            return
    print("Invalid website name. Please try again.")
    speak("Please specify a valid website.")

def get_appointments():
    """Fetch and announce all events from Google Calendar for the entire day."""
    try:
        SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
        SERVICE_ACCOUNT_FILE = "credentials.json"

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        service = build("calendar", "v3", credentials=credentials)

        now = datetime.datetime.utcnow().isoformat() + "Z"
        end_of_day = (datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)).isoformat() + "Z"

        events_result = service.events().list(
            calendarId="primary", timeMin=now, timeMax=end_of_day, maxResults=50,
            singleEvents=True, orderBy="startTime"
        ).execute()
        events = events_result.get("items", [])

        if not events:
            speak("You had no events scheduled for today.")
        else:
            speak("Here is what happened today:")
            for event in events:
                event_summary = event["summary"]
                start = event["start"].get("dateTime", event["start"].get("date"))
                start_time = datetime.datetime.fromisoformat(start[:-1]).strftime("%I:%M %p") if "T" in start else start
                speak(f"{event_summary} at {start_time}")
    except Exception as e:
        speak("I couldn't retrieve your calendar events. Please check your credentials.")
        print(f"Error: {e}")

'''if __name__ == "__main__":
    wishMe()
    while True:
        query = input("Enter your command: ").lower()
        open_website(query)'''
if __name__ == "__main__":
    wishMe()
    use_speech = True  # Set to True for voice input
    
    while True:
        query = command().lower() if use_speech else input("Enter your command: ").lower()
        open_website(query)

