import json
import requests
import base64
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

# image upload endpoint
@app.post("/encode")
def image_upload_test(
    upload_image : UploadFile = None
):
    try:
        base64_str = base64.b64encode(upload_image.file.read())
        result_str = base64_str.decode('utf-8')
        
        
        decode_url = "http://localhost:8001/decode"
        
        data = {"b64_img": result_str}
        res = requests.post(decode_url, data=json.dumps(data))
        
        if res.status_code==200:
            return True
        else:
            raise Exception(f"status_code={res.status_code}")
    except Exception as e:
        print(e)
        


if __name__ == "__main__":
    uvicorn.run("encode:app", host="0.0.0.0", port=8000, reload=True)