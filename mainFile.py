# # we will be making an AI Assistant.
import assemblyai as aai
from elevenlabs import generate
from openai import OpenAI
from playsound import playsound
import tempfile

class AI_ASSISTANT:

    def __init__(self):
        aai.settings.api_key = "enter api key here"
        self.openai_client = OpenAI(api_key="enter api key here")
        self.elevenlabs_api_key = "enter api key here"
        self.transcriber = None

        # Initial Prompt
        self.full_transcript = [
            {"role": "system", "content": "You are a personal assistant, be resourceful and expalain well"}
        ]

    ### Real-Time transcription with 'assemblyai'

    def start_transcription(self):
        print("Starting transcription...")
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data=self.on_data,
            on_error=self.on_error,
            on_open=self.on_open,
            on_close=self.on_close,
            end_utterance_silence_threshold=1000
        )
        self.transcriber.connect()
        mic_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(mic_stream)

    def stp_transcription(self):
        if self.transcriber:
            print("Stopping transcription...")
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        print("Transcription session opened.")
        return

    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            print(f"Final transcript: {transcript.text}")
            self.generate_ai_response(transcript)
        else:
            print(f"Interim transcript: {transcript.text}", end="\r")

    def on_error(self, error: aai.RealtimeError):
        print(f"An error occurred: {error}")
        return

    def on_close(self):
        print("Closing transcription session.")
        return

    # pass real-time transcript to openAI

    def generate_ai_response(self, transcript):
        self.stp_transcription()
        self.full_transcript.append({"role": "user", "content": transcript.text})
        print(f'\nUser: {transcript.text}', end='\n\r')
        response = self.openai_client.chat.completions.create(
            model='gpt-4',
            messages=self.full_transcript,
        )
        ai_response = response.choices[0].message.content
        self.generate_audio(ai_response)
        self.start_transcription()

    # Generating Audio with elevenLabs
    def generate_audio(self, text):
        self.full_transcript.append({'role': 'assistant', 'content': text})
        print(f'AI Assistant: {text}')

        audio_stream = generate(
            api_key=self.elevenlabs_api_key,
            text=text,
            voice='Rachel'
        )

        # Save the audio stream to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            temp_audio_file.write(audio_stream)
            temp_audio_file_path = temp_audio_file.name

        # Play the audio using playsound
        playsound(temp_audio_file_path)

greeting = 'Hey Hammad! How may I help you today?'
ai_assist = AI_ASSISTANT()
ai_assist.generate_audio(greeting)
ai_assist.start_transcription()

# ignore the following or remove it

#
# # the following packages will be used:
#
# # assemblyai, pip install "assemblyai[extras]"
# # openai, pip install openai
# # elevenlabs, pip install elevenlabs==0.3.0b0
# # mpv not added yet
# # portaudio not added yet
#
# import assemblyai as aai
# from elevenlabs import generate, stream
# from openai import OpenAI
# from playsound import playsound
# import tempfile
#
# class AI_ASSISTANT:
#
#     def __init__(self):
#         aai.settings.api_key = "enter api key"
#         self.openai_client = OpenAI(api_key="enter api key")
#         self.elevenlabs_api_key = "enter api key"
#         self.transcriber = None
#
#         # Initial Prompt
#         self.full_transcript = [
#             {"role": "system", "Content": "You are a personal assistant, be resourceful and explain well"}
#         ]
#
#     ### Real-Time transcription with 'assemblyai'
#
#     def start_transcription(self):
#         self.transcriber = aai.RealtimeTranscriber(
#             sample_rate=16000,
#             on_data = self.on_data,
#             on_error = self.on_error,
#             on_open = self.on_open,
#             on_close = self.on_close,
#             end_utterance_silence_threshold = 1000
#         )
#         self.transcriber.connect()
#         mic_stream = aai.extras.MicrophoneStream(sample_rate=16000)
#         self.transcriber.stream(mic_stream)
#
#     def stp_transcription(self):
#         if self.transcriber:
#             self.transcriber.close()
#             self.transcriber = None
#
#     def on_open(self,session_opened: aai.RealtimeSessionOpened):
#         # print("Session ID:", session_opened.session_id)
#         return
#
#     def on_data(self,transcript: aai.RealtimeTranscript):
#         if not transcript.text:
#             return
#
#         if isinstance(transcript, aai.RealtimeFinalTranscript):
#             # print(transcript.text, end="\r\n")
#             self.generate_ai_response(transcript)
#         else:
#             print(transcript.text, end="\r")
#
#     def on_error(self, error: aai.RealtimeError):
#         # print("An error occurred:", error)
#         return
#
#     def on_close(self):
#         # print("Closing Session")
#         return
#
#     # pass real-time transcript to openAI
#
#     def generate_ai_response(self, transcript):
#         self.stp_transcription()
#         self.full_transcript.append({"role": "system", "Content": transcript.text})
#         print(f'\nPatient: {transcript.text}', end='\n\r')
#         response = self.openai_client.chat.completions.create(
#             model='gpt-4',
#             messages=transcript.full_transcript,
#         )
#         ai_response = response.choices[0].message.content
#         self.generate_audio(ai_response)
#         self.start_transcription()
#
#     # Generating Audio with elevenLabs
#     def generate_audio(self, text):
#         self.full_transcript.append({'role': 'assistant', 'content': text})
#         print(f'AI Receptionist: {text}')
#
#         audio_stream = generate(
#             api_key=self.elevenlabs_api_key,
#             text=text,
#             voice='Rachel'
#         )
#
#         # stream(audio_stream)
#         # Save the audio stream to a temporary file
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
#             temp_audio_file.write(audio_stream)
#             temp_audio_file_path = temp_audio_file.name
#
#         # Play the audio using playsound
#         playsound(temp_audio_file_path)
#
#
# greeting = 'Hey Hammad! How may I help you today?'
# ai_assist = AI_ASSISTANT()
# ai_assist.generate_audio(greeting)
# ai_assist.start_transcription()

