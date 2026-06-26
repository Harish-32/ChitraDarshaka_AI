from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from story_generator import generate_story
from pipeline import generate_trailer_from_story

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)

class StoryRequest(BaseModel):
    prompt: str
    language: str

class TrailerRequest(BaseModel):
    story: str
    language: str

@app.get("/")
def home():
    return {
        "message": "AI Director API Running"
    }

@app.post("/generate-story")
def generate_story_api(data: StoryRequest):

    story = generate_story(
        data.prompt,
        data.language
    )

    return {
        "story": story
    }

@app.post("/generate-trailer")
def generate_trailer_api(data: TrailerRequest):

    result = generate_trailer_from_story(
        data.story,
        data.language
    )

    return {
        "trailer_script": result["trailer_script"],
        "video": "http://localhost:8000/outputs/final_trailer.mp4"
    }
