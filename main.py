
"""Google Cloud Speech API sample application using the streaming API.
NOTE: This module requires the dependencies `pyaudio` and `termcolor`.
To install using pip:
    pip install pyaudio
    pip install termcolor
Example usage:
    python transcribe_streaming_infinite.py
"""


import sys
import gcloud
from gcloud import GoogleSpeech, ResumableMicrophoneStream
import matplotlib.pyplot as plt
import struct
import numpy as np
import xlsxwriter as xlsw
from scipy.io import wavfile


def main():
    """start bidirectional streaming from microphone input to speech API"""

    speech = GoogleSpeech()
    mic_manager = ResumableMicrophoneStream(gcloud.SAMPLE_RATE, gcloud.CHUNK_SIZE)
    with mic_manager as stream:
        transcripts = speech.transcript_in_loop(stream)     # return all detected speech as a list

    # save the transcribed data to a txt file
    transcripts_str = '\n'.join(transcripts)    # split by newlines
    with open('output/transcripts.txt', 'w') as f:
        f.write(transcripts_str)

    # combine all waveforms (chunks) into one variable and save to a csv file
    data_int = []
    for chunk in stream.last_audio_input:
        # convert data to integers, make np array, then offset it by 127
        data_int.extend(struct.unpack(str(2 * gcloud.CHUNK_SIZE) + 'B', chunk)[::2])

    data_int = [i - 127 for i in data_int]
    data_np = np.asarray(data_int, dtype=np.int16)
    np.savetxt('output/data_np.csv', data_np, delimiter=',')

    # plot a 0.5s of the waveform file
    plt.ion()
    plt.plot(data_np[0:6000])
    plt.show()


if __name__ == "__main__":
    main()
