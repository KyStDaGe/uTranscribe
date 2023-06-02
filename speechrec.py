
import speech_recognition as sr
import os

r = sr.Recognizer()
def transcribe_large_audio():
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    dir = os.path.join(directory,"parts")
    
    object = os.scandir(dir)
    
    whole_text = ""
    
    # Process each chunk
    for n in object:
        if n.is_file():
            chunk_filename = os.path.join(dir,n.name)
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
            # Convert to text
                try:
                    text = r.recognize_google(audio_listened)
                except sr.RequestError as e:
                    text = r.recognize_sphinx(audio_listened)
                    text = f"{text.capitalize()} "
                    print(chunk_filename, ":Done.")
                    whole_text += text
            
                except sr.UnknownValueError as e:
                    
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()} "
                    print(chunk_filename, ":Done")
                    whole_text += text
            os.remove(chunk_filename)        
                    
    return whole_text
transcribe_large_audio()


