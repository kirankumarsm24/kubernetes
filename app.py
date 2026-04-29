from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")

    # simple dummy AI logic
    if "good" in text.lower():
        return {"prediction": "positive"}
    else:
        return {"prediction": "negative"}
