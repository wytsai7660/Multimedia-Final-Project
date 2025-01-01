import asyncio

from fastapi import FastAPI

from src import grammar, test_client

fifo_queue = asyncio.Queue()


async def enqueue():
    input = str("")
    while True:
        reading = asyncio.run(
            f"{test_client.read_streaming_transcript(grammar_server)}/fake_transcript"
        )
        if reading == "":
            break
        input += reading

    corrected = grammar.main(input)
    await fifo_queue.put(corrected)
    print("pushed to queue")
    print(fifo_queue.qsize())


app = FastAPI()


@app.get("/corrected")
async def corrected_text():
    corrected: str = await fifo_queue.get()
    return corrected


def main():
    while True:
        asyncio.run(enqueue())


if __name__ == "__main__":
    grammar_server = input("Enter the server address for the Grammar API: ")
    # import uvicorn

    # uvicorn.run("input_part:app", host="127.0.0.1", port=8000, log_level="info")
    main()
