from fastapi import FastAPI, Request
from pydantic import BaseModel
from services.script_generator import create_script
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from services.scene_splitter import split_script
from services.prompt_generator import create_image_prompts
from services.image_generator import generate_images
app = FastAPI(title="ShortsAI Backend V2")
app.mount("/static", StaticFiles(directory="static"), name="static")

class ScriptRequest(BaseModel):
    topic: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "2.0"
    }


@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    script = create_script(topic)

    scenes = split_script(script)
    prompts = create_image_prompts(scenes)
    image_paths = generate_images(prompts)
    return repr(script)
0







