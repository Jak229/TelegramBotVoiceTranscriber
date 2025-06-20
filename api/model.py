import os
from pydub import AudioSegment
import speech_recognition as sr


r = sr.Recognizer()


class Transcriber:
    def __init__(self, path: str, lang: str = "en-GB"):
        self.path = path
        self.lang = self.__lang(lang)
        self.recognizer = r

    def __lang(self, lang: str):
        """
        Convert the language code to the format required by the recognizer. 
        :param lang: The language code (e.g., "en", "ru", "de", "fr", "es").
        :return: The language code in the format required by the recognizer (e.g., "en-GB", "ru-RU").
        """
        if lang == "ru":
            return "ru-RU"
        elif lang == "en":
            return "en-GB"
        elif lang == "de":
            return "de-DE"
        elif lang == "fr":
            return "fr-FR"
        elif lang == "es":
            return "es-ES"
        elif lang == "ua":
            return "uk-UA"
        elif lang == "it":
            return "it-IT"
        elif lang == "pl":
            return "pl-PL"
        elif lang == "pt":
            return "pt-PT"
        elif lang == "tr":
            return "tr-TR"
        elif lang == "ro":
            return "ro-RO"
        else:
            raise ValueError(
                "Unsupported language. Supported languages: ru, en, de, fr, es"
            )

    def convert_audio(self):
        """
        Convert the audio file to WAV format with 16kHz sample rate, mono channel, and 16-bit sample width.
        :return: The path to the converted WAV file.
        """
        # Check if the file exists
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File {self.path} not found.")

        # Convert the audio file to WAV format
        audio = AudioSegment.from_file(self.path)
        audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
        wav_path = self.path.replace(os.path.splitext(self.path)[1], ".wav")
        audio.export(wav_path, format="wav")
        os.remove(self.path)
        return wav_path

    def transcribe(self):
        """
        Transcribe the audio file to text.
        :return: The transcribed text.
        """
        # Check if the file exists
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File {self.path} not found.")

        # Check if the file is a valid audio file
        if not self.path.endswith((".wav", ".mp3", ".flac", ".ogg")):
            raise ValueError(
                "Invalid file format. Supported formats: .wav, .mp3, .flac, .ogg"
            )

        # Load the audio file
        converted_file = self.convert_audio()
        self.path = converted_file

        with sr.AudioFile(self.path) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio_data = self.recognizer.record(source)
            try:
                # Recognize the speech in the audio file
                text = self.recognizer.recognize_google(
                    audio_data, language=self.lang
                ) 
                return text
            except sr.UnknownValueError:
                raise ValueError("Could not understand the audio.")
            except sr.RequestError as e:
                raise ConnectionError(f"Could not request results; {e}")

    def __del__(self):
        if os.path.exists(self.path):
            os.remove(self.path)
