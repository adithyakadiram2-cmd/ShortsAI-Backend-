from pydantic import BaseModel

class ShortsProject(BaseModel):
    topic: str
    script: str = ""
    scenes: list = []
    prompts: list = []
    images: list = []
    voice: str = ""
    subtitles: str = ""
    video: str = ""
0

