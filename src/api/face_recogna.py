from fastapi import APIRouter, UploadFile, File , Depends, HTTPException , status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.base import get_db
from src.utils.dependeises import recognize_face


router = APIRouter()


@router.post("/recognize")
async def recognize(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    try:
        image_bytes = await file.read()
        result = await recognize_face(image_bytes, db)
        return {"result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=str(e))
