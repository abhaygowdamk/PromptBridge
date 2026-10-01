from fastapi import FastAPI

app = FastAPI(title="PromptBridge")


@app.get("/")
def health_check():
    return {"message": "PromptBridge is running!"}  