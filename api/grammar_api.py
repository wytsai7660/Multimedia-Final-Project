import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).resolve().parent.parent))
import grammar

app = FastAPI()


@app.post("/grammar")
async def grammar_correction(input: str):
    return grammar.main(input)


if __name__ == "__main__":
    uvicorn.run("grammar_api:app", host="127.0.0.1", port=8000, log_level="info")
