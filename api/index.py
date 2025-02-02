from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from the JSON file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

@app.get("/api")
def get_marks(name: list[str] = []):
    marks = [student_data.get(n, None) for n in name]  # Fetch marks in order
    return {"marks": marks}
