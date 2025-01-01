# C.K.Chiang Grammar Correction & Voice Regeneration

![C.K.Chiang](https://www.cs.ccu.edu.tw/~ckchiang/Big.jpg)

▲ Professor Chiang, our most beloved professor.

Professor Chiang has recently started teaching all-English (EMI) courses. However, despite his immense intelligence and wisdom, Professor Chiang occasionally makes negligible grammatical errors in very rare and specific situations. While these errors are minor, they can still increase the difficulty of understanding for students with weaker English skills.

## Overview

Our project aims to correct these extremely rare errors and reconstruct the pleasant voice of Professor Chiang from a given audio file.

The project is divided into three parts:

- Automatic Speech Recognition (ASR)
- Grammar Correction
- Text to Speech (TTS)

## Usage

Since the computation may be heavy, we recommend distributing these three parts to different machines. You can do this using [ngrok](https://ngrok.com/) (which is how we do it).

1. (ngrok) Run `ngrok http <port_number>`, remember the URL.

2. Install the required packages.

3. (Only required for grammar correction) Create a `.env` file in the project root with the following content.

    ```text
    OPENROUTER_API_KEY = <your_openrouter_api_key>
    ```

4. Run the desired API script on the corresponding machine.

    | Function                     | Script           |
    |------------------------------|------------------|
    | Automatic Speech Recognition | `asr_api.py`     |
    | Grammar Correction           | `grammar_api.py` |
    | Text to Speech               | `tts_api.py`     |
