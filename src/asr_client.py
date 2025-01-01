import httpx
import asyncio

buffer = ""  # Global variable to store the buffer

async def read_streaming_transcript(url):
    global buffer
    async with httpx.AsyncClient(timeout=None) as client:  # 無限超時
        async with client.stream("GET", url) as response:
            if response.status_code == 200:
                print("Connected to the stream. Receiving data:")
                async for line in response.aiter_lines():
                    if line != buffer:
                        buffer = line
                        yield buffer
            else:
                print(f"Failed to connect: {response.status_code}")

if __name__ == "__main__":
    endpoint_url = "http://127.0.0.1:8000/stream"
    asyncio.run(read_streaming_transcript(endpoint_url))
