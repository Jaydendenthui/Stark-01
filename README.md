# Stark-01
This Python-powered AI voice assistant is designed for smart glasses for the blind, enabling hands-free interaction through voice commands. The system integrates speech recognition, text-to-speech (TTS), web automation, and Google Calendar integration to assist visually impaired users in navigating daily tasks.

✨ Features
✅ Voice-Controlled Commands – Hands-free interaction with natural language processing.
✅ Web Navigation – Open popular websites (e.g., Facebook, YouTube, Google) via voice input.
✅ Google Calendar Integration – Fetch and announce upcoming events.
✅ Time & Day Announcements – Provides real-time updates on the current time and day.
✅ Customizable & Expandable – Easily extendable to support more commands and functionalities.

🔧 Tech Stack
🔹 Python (Core programming)
🔹 SpeechRecognition (Voice input processing)
🔹 pyttsx3 (Text-to-speech synthesis)
🔹 Google Calendar API (Event management)
🔹 OpenCV (Future Scope) – Can be integrated for object detection.

🚀 How It Works
The system listens for voice commands using speech_recognition.
It processes the input and performs the required action (e.g., opening a website, checking the calendar, announcing time).
It responds through AI-driven voice output via pyttsx3.
For scheduling, it fetches Google Calendar events and reads them aloud.
🛠️ Google Calendar Setup
To use the Google Calendar feature, you need to create a credentials.json file. Follow these steps:

1️⃣ Enable Google Calendar API
Go to the Google Cloud Console.
Create a new project (or select an existing one).
Navigate to "APIs & Services" > "Library".
Search for Google Calendar API and enable it.
2️⃣ Create Credentials
Go to "APIs & Services" > "Credentials".
Click "Create Credentials" > "Service Account".
Fill in the details and grant "Editor" access.
Go to "Keys" > "Add Key" > "JSON", then download the file.
Rename the file to credentials.json and place it in your project folder.
3️⃣ Share Your Calendar with the Service Account
Open Google Calendar.
Go to Settings > Your Calendar > "Share with Specific People".
Add the service account email (found in credentials.json).
Grant "Make changes to events" permission.
