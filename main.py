#AI Receptionist 
# Take down messages, maybe check calendar invites, provide information
# Schedule a meeting/appointment, google calendar, ask for information, is the doctor available
import sounddevice as sd 
import soundfile as sf
import openai
import keyboard
import tempfile
import os
from elevenlabs import generate, play, set_api_key
from execute_ai import call_agent, answer_the_call
duration = 10  # duration of each recording in seconds
fs = 44100  # sample rate
channels = 1  # number of channels
sd.default.samplerate = fs
sd.default.channels = 2

os.environ["OPENAI_API_KEY"] = "" #OpenAI Key
set_api_key("")
os.environ["OPENAI_API_KEY"] = "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" #OpenAI Key
openai.api_key = os.getenv("OPENAI_API_KEY")

set_api_key("c8c37eecf2a27ac31e34e0f580da0433")
os.environ["ZAPIER_NLA_API_KEY"] = os.environ.get("ZAPIER_NLA_API_KEY", "sk-ak-zAJqR1Fs5vsKN7pWhaFQit7Kug")

def record_audio(duration, fs, channels):
    print("Recording...")
@@ -51,6 +54,8 @@ def play_generated_audio(text, voice="Bella", model="eleven_monolingual_v1"):
        recorded_audio = record_audio(duration, fs, channels)
        message = transcribe_audio(recorded_audio, fs)
        print(f"You: {message}")
        wait_text = "Please hold on a minute, thank you!"
        play_generated_audio(wait_text)
        agent = call_agent()
        task_info = agent.run(message)answer_chain = answer_the_call()
        answer = answer_chain.predict(INFO = task_info)
        play_generated_audio(answer) 