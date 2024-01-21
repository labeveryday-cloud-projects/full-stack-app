from fastapi import FastAPI, HTTPException, Form
import requests

app = FastAPI()

@app.post("/process-url")
async def process_url(url: str = Form(...)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        text_content = response.text

        # Here you would add your logic to send text_content to an LLM
        # For this demo, we'll just return the text content
        return {"content": text_content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
