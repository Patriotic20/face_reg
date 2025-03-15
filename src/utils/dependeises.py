import face_recognition
import numpy as np
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.knownface import KnownFace
import cv2

async def recognize_face(image_bytes: bytes, db: AsyncSession):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
    
    result = await db.execute(select(KnownFace))
    known_faces = result.scalars().all()
    
    for face_encoding in face_encodings:
        for known_face in known_faces:
            known_encoding = np.array(known_face.encoding, dtype=np.float64) 
            matches = face_recognition.compare_faces([known_encoding], face_encoding)
            if True in matches:
                return f"Face recognized: {known_face.first_name} {known_face.last_name}"
    return "No match found."