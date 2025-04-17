import time
from plyer import notification
# from playsound import playsound  # Optional
# from simpleaudio import WaveObject


def break_reminder():
    while True:
        # Wait for 2 hours (7200 seconds)
        time.sleep(30)  

        # Show a popup notification
        notification.notify(
            title="Take a Break! 🕒",
            message="You've been working for 2 hours. Stand up, stretch, and rest your eyes!",
            app_name="Break Reminder",
            timeout=10  # Notification stays for 10 sec
        )

        # (Optional) Play a sound
#         try:
# # Load and play a WAV file
#             WaveObject.from_wave_file("file_example_WAV_1MG.wav").play()  # You need an MP3 file
#         except:
#             print("Sound file missing (or error)")

if __name__ == "__main__":
    print("Break Reminder started! (Close terminal to stop)")
    break_reminder()
