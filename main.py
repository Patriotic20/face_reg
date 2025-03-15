from fastapi import FastAPI
from src.api.face_recogna import router as face_recogna
from src.api.add_user import router as add_user
import uvicorn

app = FastAPI()

app.include_router(face_recogna)
app.include_router(add_user)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)