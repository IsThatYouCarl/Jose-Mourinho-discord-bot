import os
import glob
import mp3
from wave import Wave_write
import re

def mp3_to_pcm(mp3_file, file):
    with open(mp3_file, 'rb') as read_file, open(file, 'wb') as write_file:
        decoder = mp3.Decoder(read_file)

        sample_rate = decoder.get_sample_rate()
        nchannels = decoder.get_channels()

        wav_file = Wave_write(write_file)
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        while True:
            pcm_data = decoder.read(4000)

            if not pcm_data:
                break
            else:
                wav_file.writeframes(pcm_data)


folder_path = 'D:\\jose-mourinho bot\\audio\\mp3'

mp3_files = glob.glob(os.path.join(folder_path, '*.mp3'))

for mp3_file in mp3_files:
    print("Processing:", mp3_file)
    file_name = re.findall(r'(\w+)\.mp3', mp3_file)[0]
    file = f'{file_name}.wav'
    mp3_to_pcm(mp3_file, file)
    