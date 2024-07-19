from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Gebruik absolute imports in plaats van relatieve imports
from backend.routers import homerouter, templaterouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [homerouter, templaterouter]

for router in routers:
    app.include_router(router.router)

# Voeg een eenvoudige root route toe
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
