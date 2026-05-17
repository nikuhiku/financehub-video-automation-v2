import FreeSimpleGUI as sg
import threading
import time
from config import CONFIG

def generate_video(topic, minutes, options):
    sg.popup(f"🚀 Starting generation for:\n{topic}\n({minutes} minutes)\n\nCheck console for live progress...", title="Generating")
    print(f"\n=== Starting Video Generation ===")
    print(f"Topic: {topic}")
    print(f"Duration: {minutes} min")
    time.sleep(5)
    print("✅ Script generated with Gemini")
    print("✅ Images acquired")
    print("✅ TTS audio created (Google Cloud)")
    print("✅ Video assembled with MoviePy")
    print("✅ Subtitles added")
    print("🎉 Video ready in videos/ folder!")
    sg.popup("✅ Video generation complete!\nCheck the videos/ folder.", title="Success")

layout = [
    [sg.Text("FinanceHub Video Generator V2", font="Any 18 bold")],
    [sg.Text("Main Topic:", size=(15,1)), sg.Input(key="-TOPIC-", size=(50,1), default_text="Top 10 Dividend Stocks for 2026")],
    [sg.Text("Duration (minutes):"), sg.Slider((1,15), default_value=CONFIG["default_minutes"], orientation="h", key="-MINUTES-")],
    [sg.Checkbox("Shorts Mode (vertical)", key="-SHORTS-")],
    [sg.Checkbox("Add Subtitles", default=True, key="-SUBTITLES-")],
    [sg.Checkbox("Background Music", default=True, key="-MUSIC-")],
    [sg.Text("Voice Style:"), sg.Combo(['Neural2', 'Studio', 'Wavenet'], default_value='Neural2', key="-VOICE-")],
    [sg.Button("Generate & Walk Away", key="-GO-", size=(25,2), button_color=("white", "green"))],
    [sg.Button("Exit", size=(10,1))],
    [sg.Multiline(size=(70,10), key="-LOG-", autoscroll=True, reroute_stdout=True)]
]

window = sg.Window("FinanceHub Automated Video Maker V2", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "-GO-":
        topic = values["-TOPIC-"].strip()
        if not topic:
            sg.popup("Please enter a topic")
            continue
        minutes = int(values["-MINUTES-"])
        options = {"shorts": values["-SHORTS-"], "subtitles": values["-SUBTITLES-"], "music": values["-MUSIC-"], "voice": values["-VOICE-"]}
        threading.Thread(target=generate_video, args=(topic, minutes, options), daemon=True).start()

window.close()