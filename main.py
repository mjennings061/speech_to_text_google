
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


def main():
    """start bidirectional streaming from microphone input to speech API"""

    speech = GoogleSpeech()
    mic_manager = ResumableMicrophoneStream(gcloud.SAMPLE_RATE, gcloud.CHUNK_SIZE)
    with mic_manager as stream:
        transcripts = speech.transcript_in_loop(stream)     # return all detected speech as a list

    # for chunk in stream.last_audio_input:
    #     audio_int = int.from_bytes(chunk, byteorder='big')
    #     print(chunk)
    #     print(audio_int)
    #     audio_int = [int.from_bytes(sample, byteorder='big') for sample in chunk]
    # plt.plot(audio_int)
    # plt.show()


if __name__ == "__main__":
    main()
