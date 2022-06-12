import os
from fastapi import FastAPI, Body, HTTPException, status
# from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}