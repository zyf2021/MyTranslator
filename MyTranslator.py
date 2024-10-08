import ffmpeg
from moviepy.editor import VideoFileClip
import speech_recognition as sr

import os


# Получаем путь к текущему каталогу
current_directory = os.getcwd()
print("Текущий каталог:", current_directory)

# Создаем пути к файлам

input_file = os.path.join(current_directory, 'video_input_1.mp4')
output_file = os.path.join(current_directory, 'audio_output.wav')

# Отделяем аудио от видео

# Попытка открыть видеофайл
try:
    video = VideoFileClip(input_file)
    video.audio.write_audiofile(output_file)
except UnicodeDecodeError as e:
    print(f"Ошибка кодировки: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

r = sr.Recognizer()

with sr.AudioFile(output_file) as source:
    audio = r.record(source)


try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio)) # , language="ru-RU")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio)) # , language="ru-RU"
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))