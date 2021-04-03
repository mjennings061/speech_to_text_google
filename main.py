

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the streaming API.
NOTE: This module requires the dependencies `pyaudio` and `termcolor`.
To install using pip:
    pip install pyaudio
    pip install termcolor
Example usage:
    python transcribe_streaming_infinite.py
"""

# [START speech_transcribe_infinite_streaming]

import sys
import gcloud
from gcloud import GoogleSpeech, ResumableMicrophoneStream


def main():
    """start bidirectional streaming from microphone input to speech API"""

    speech = GoogleSpeech()
    mic_manager = ResumableMicrophoneStream(gcloud.SAMPLE_RATE, gcloud.CHUNK_SIZE)
    with mic_manager as stream:
        speech.transcript_in_loop(stream)


if __name__ == "__main__":
    main()

# [END speech_transcribe_infinite_streaming]