import asyncio
import threading

import requests

fifo_queue = asyncio.Queue()


async def main():
    # def send_request(i: int):
    #     response = requests.get(
    #         url=f"{grammar_server}/add", json={"id": str(i), "input": str(i)}
    #     )
    #     print(response.json())

    # threads = []
    # for i in range(10):
    #     thread = threading.Thread(target=send_request, args=(i,))
    #     threads.append(thread)
    #     thread.start()
    #     print(f"Sent {i}")

    # for thread in threads:
    #     thread.join()

    while True:
        # i = input("Enter a number: ")
        response = requests.get(url=f"{grammar_server}/corrected")
        print(response.json())


if __name__ == "__main__":
    grammar_server = input("Enter the server address for the Grammar API: ")
    _ = main()
