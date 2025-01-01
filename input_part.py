import asyncio
import httpx
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src import grammar

app = FastAPI()

# 用於暫存流式數據的緩存
buffer = []
fifo_queue = asyncio.Queue()
repeated = ""
line_buffer = ""

# 用於讀取時的索引
read_index = 0

# 從 /stream 接收數據的協程
async def fetch_stream():
    global buffer
    global repeated
    global line_buffer
    url = "http://localhost:8000/stream"  # 修改為你的 /stream 端點 URL
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", url) as response:
            async for line in response.aiter_lines():
                if line != repeated:
                    repeated = line
                    if repeated != "":
                        line_buffer += repeated
                    else:
                        line_buffer = grammar.main(line_buffer)
                        await fifo_queue.put(line_buffer) 
                        print(f"Received: {line_buffer.strip()}")
                        line_buffer = ""

# 從緩存中提供數據的端口
@app.get("/read")
async def read_data():
    text = await fifo_queue.get()
    return JSONResponse(content={"data": text})
    # global buffer, read_index
    # if read_index < len(buffer):
    #     data = buffer[read_index]
    #     read_index += 1
    #     return {"data": data}
    # else:
    #     return JSONResponse(content={"error": "No new data available"}, status_code=404)

# 啟動背景任務以持續接收流式數據
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(fetch_stream())

# 啟動 FastAPI 服務器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
