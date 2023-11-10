from routes import health, username

from fastapi import FastAPI
import uvicorn
app = FastAPI()

app.include_router(health.router)
app.include_router(username.router)
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)