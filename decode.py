import io
import base64
import uvicorn
from PIL import Image
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class ReqeustBody(BaseModel):
    b64_img: str


@app.post("/decode")
def image_preprocessing(
    inbound_data: ReqeustBody
):
    b_object = inbound_data.b64_img.encode('UTF-8')
    img_data = base64.b64decode(b_object)
    
    io_obejct = io.BytesIO(img_data)
    img = Image.open(io_obejct)
    


if __name__ == "__main__":
    uvicorn.run("decode:app", host="0.0.0.0", port=8001, reload=True)