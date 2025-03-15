from fastapi import APIRouter, UploadFile, File , Depends , HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.base import get_db
import numpy as np
import cv2
from src.models import KnownFace
import face_recognition

router = APIRouter()

@router.post("/add_user")
async def add_user(first_name: str, last_name: str, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    try:
        image_bytes = await file.read()
        np_arr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_image)
        
        if not face_encodings:
            raise HTTPException(status_code=400, detail="No face found in the image.")
        
        new_face = KnownFace(first_name=first_name, last_name=last_name, encoding=face_encodings[0].tolist())
        db.add(new_face)
        await db.commit()
        return {"message": "User added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))