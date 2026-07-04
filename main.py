from fastapi import FastAPI, Request
from pydantic import BaseModel
from services.script.generator import generate_script
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from services.scenes.splitter import split_into_scenes
from services.prompts.generator import generate_prompts
from services.images.generator import generate_scene_images
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
    script = generate_script(topic)

    scenes = split_into_scenes(script)
    prompts = generate_prompts(scenes)
    image_paths = generate_scene_images(prompts)
    return repr(script)
0













