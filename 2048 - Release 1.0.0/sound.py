#================================imports, checks and pre-configs================================
import time, threading, turtle, vars
print("sound.py: time, threading, turtle, vars(.py) have been imported.")
t = turtle
try:
    import soundfile as sf
    print("sound.py: soundfile was imported.")
    import sounddevice as sd
    print("sound.py: sounddevice was imported.")
    #from mutagen.wavpack import WavPack
    print("sound.py: WavPack was imported.")
    from pydub import AudioSegment
    print("sound.py: AudioSegment was imported.")
    #import numpy
    print("sound.py: numpy was imported.")
    t.forward(200)

except:
    from install import installModules
    print("sound.py: installModules was imported.")
    installModules("sound")
    import soundfile as sf
    print("sound.py: soundfile was imported.")
    import sounddevice as sd
    print("sound.py: sounddevice was imported.")
    from mutagen.wavpack import WavPack
    print("sound.py: WavPack was imported.")
    from pydub import AudioSegment
    print("sound.py: AudioSegment was imported.")
    import numpy
    print("sound.py: numpy was imported.")

file_paths = ["music/title.wav", "music/game1.wav", "music/game2.wav", "music/game3.wav"]


def get_song_length():#get's the length of the songs so that it can get looped properly
    global duration

    duration = []
    # Load the WAV file
    for file in file_paths:
        audio = AudioSegment.from_file(file)

        # Get the duration in miliseconds
        duration.append(len(audio)-100) #-100 for loading time

stop_flag = threading.Event()


def playSoundLoop():#plays the music (in a loop)
    global currentSound, duration
    
    def loadAudioFilesData(file_paths):
        loaded_data = []
        for file_path in file_paths:
            audio_data, sample_rate = sf.read(file_path)
            loaded_data.append(audio_data)
        return loaded_data
    
    def loadAudioFilesSample(file_paths):
        loaded_sample = []
        for file_path in file_paths:
            audio_data, sample_rate = sf.read(file_path)
            loaded_sample.append(sample_rate)
        return loaded_sample

    def play_audio(audio_data, sample_rate):
        if vars.music != 0:
            sd.play(audio_data, sample_rate)
        else:
            time.sleep(1)

    loaded_data = loadAudioFilesData(file_paths)
    loaded_sample = loadAudioFilesSample(file_paths)

    startTime = 0
    filePlaying = 0
    while True:
        if vars.music == 0:
            sd.stop()
            startTime = 0
            while vars.music == 0:
                time.sleep(1)
        currentTime = int(round(time.time() * 1000))
        if vars.gameOver != True and currentTime>startTime:
            play_audio(loaded_data[vars.music], loaded_sample[vars.music])
            startTime = int(round(time.time() * 1000))+duration[vars.music]
            filePlaying = 2
        if vars.gameOver == True and filePlaying == 2 and currentTime<startTime:
            sd.stop()
            startTime = 0
        
        if vars.titleScreenActive == True and currentTime>startTime:
            play_audio(loaded_data[0], loaded_sample[0])
            startTime = int(round(time.time() * 1000))+duration[0]
            filePlaying = 1
        if vars.titleScreenActive != True and filePlaying == 1 and currentTime<startTime:
            sd.stop()
            startTime = 0
               
        time.sleep(0.01)

def startSound():#starts "playSoundLoop()" in another thread
    get_song_length()
    global currentSound
    thread1 = threading.Thread(target=playSoundLoop)
    thread1.start()
    print("sound.py: NOTE: sound controller has been started.")