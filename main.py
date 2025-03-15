from fastapi import FastAPI
from src.api.face_recogna import router as face_recogna
import uvicorn

app = FastAPI()

app.include_router(face_recogna)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)