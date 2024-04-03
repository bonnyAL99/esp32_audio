from pydub import AudioSegment

raw_audio = AudioSegment.from_file("adc.raw", format="raw",
                                   frame_rate=44000, channels=1, sample_width=2)

raw_audio.export("voice.mp3", format="mp3")