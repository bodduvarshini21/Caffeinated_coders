from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
import pandas as pd
from io import StringIO

router = APIRouter()

class Story(BaseModel):
    story: str

@router.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode('utf-8')))
    print("Uploaded CSV Columns:", df.columns)  # Debug: Print column names
    print("Uploaded CSV Data:", df.head())  # Debug: Print first few rows

    # Check if the required column exists
    if 'Title' not in df.columns:
        return {"error": "The uploaded file must contain a 'Title' column."}

    # Use the 'Title' column as user stories
    user_stories = df['Title'].tolist()
    return {"userStories": user_stories}

@router.post("/api/analyze")
async def analyze_story(story: Story):
    selected_story = story.story

    # Load user stories from a persistent storage or in-memory storage
    user_stories = ["User story 1", "User story 2", "User story 3"]  # Replace with actual user stories

    # NLP Analysis
    import spacy
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    nlp = spacy.load('en_core_web_sm')
    docs = [nlp(story) for story in user_stories]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(user_stories)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Find the impact of the selected story
    selected_index = user_stories.index(selected_story)
    impact_scores = cosine_sim[selected_index]

    # Create relationships with similarity percentages
    relationships = []
    for i, score in enumerate(impact_scores):
        if i != selected_index:  # Exclude the selected story itself
            relationships.append({
                "source": selected_index + 1,
                "target": i + 1,
                "similarity": round(score * 100, 2)  # Convert to percentage
            })

    return {"userStories": user_stories, "relationships": relationships}