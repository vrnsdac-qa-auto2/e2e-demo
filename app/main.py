from fastapi import FastAPI
import random, asyncio
app = FastAPI()
@app.get("/health")
async def health():
   return {"status": "ok"}
@app.get("/unstable")
async def unstable():
   if random.random() < 0.4:
       await asyncio.sleep(0.3)
       raise Exception("Random failure")
   return {"status": "ok", "data": "success"}
@app.get("/users")
async def users():
   await asyncio.sleep(0.2)
   return {"status": "ok", "users": ["aviad", "noa"]}