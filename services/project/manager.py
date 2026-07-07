from models.project import ShortsProject

def create_project(topic: str):
    return ShortsProject(topic=topic)

def update_script(project: ShortsProject, script: str):
    project.script = script
    return project

def update_scenes(project: ShortsProject, scenes: list):
    project.scenes = scenes
    return project

def update_prompts(project: ShortsProject, prompts: list):
    project.prompts = prompts
    return project

def update_images(project: ShortsProject, images: list):
    project.images = images
    return project
0

