import sounddevice as sd
import numpy as np

# Definisci i parametri dell'audio
freq_campionamento = 44000  # Frequenza di campionamento
durata = 10  # Durata in secondi
num_canali = 1 # Numero di canali
risoluzione_bit = 16  # Risoluzione dei bit

# Carica il file audio raw
with open("adc.raw", "rb") as f:
    dati_audio = np.frombuffer(f.read(), dtype=np.int16)

# Riproduci l'audio
sd.play(dati_audio, freq_campionamento)

# Attendi il completamento della riproduzione
sd.wait()
