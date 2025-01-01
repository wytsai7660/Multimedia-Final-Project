import json
import sys

import requests
from dotenv import get_key


def main(input: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        },
        data=json.dumps(
            {
                "model": "google/gemini-flash-1.5",
                # This prompt mostly comes from https://chatgptaihub.com/chatgpt-prompts-for-grammar-check/#99-expertly-crafted-chatgpt-prompts-for-flawless-grammar-checks
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            "Please analyze the given text generated with automatic "
                            "speech recognition for grammatical errors and provide "
                            "corrections. Focus on punctuation, sentence structure, "
                            "and overall clarity to ensure a polished and error-free "
                            "piece. Please reply only the corrected sentences "
                            f"(do not write explanations).\nInput text:\n{input}"
                        ),
                    }
                ],
            }
        ),
    )
    print(response.json()["choices"][0]["message"]["content"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <INPUT_STRING>")
        sys.exit(1)

    OPENROUTER_API_KEY = get_key(".env", "OPENROUTER_API_KEY")
    if OPENROUTER_API_KEY == None:
        sys.exit(1)

    main(sys.argv[1])
