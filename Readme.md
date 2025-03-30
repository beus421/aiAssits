# AI Assistant

## Overview
AI Assistant is a Python-based voice assistant that utilizes OpenAI's GPT, AssemblyAI for speech-to-text transcription, and ElevenLabs for text-to-speech conversion. It enables real-time conversations by transcribing speech, generating AI responses, and converting text back into audio.

## Features
- **Real-time Speech Transcription** using AssemblyAI
- **AI-powered Responses** via OpenAI's GPT
- **Voice Output** generated with ElevenLabs
- **Interactive Conversations** with a personal assistant

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed.

### 1. Clone the Repository
```bash
git clone https://github.com/beus421/aiAssits.git
cd aiAssits
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a `.env` file in the project root and add your API keys:
```
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## Usage
Run the main script to start the assistant:
```bash
python mainFile.py
```
The AI Assistant will listen, transcribe, generate responses, and speak them out.

## Dependencies
- `assemblyai`
- `openai`
- `elevenlabs`
- `playsound`

## Future Improvements
- Improve error handling and logging
- Add support for multiple voices
- Enhance response generation

## License
This project is open-source. Feel free to modify and contribute!


