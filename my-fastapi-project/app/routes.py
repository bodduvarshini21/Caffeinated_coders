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
    user_stories = df['UserStory'].tolist()

    # Return user stories to the frontend
    return {"userStories": user_stories}

@router.post("/api/analyze")
async def analyze_story(story: Story):
    selected_story = story.story

    # Load user stories from a persistent storage or in-memory storage
    # For simplicity, let's assume we have the user stories in a list
    user_stories = ["User story 1", "User story 2", "User story 3"]

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

    # Create relationships based on impact scores
    relationships = []
    for i, score in enumerate(impact_scores):
        if i != selected_index and score > 0.5:  # Threshold for similarity
            relationships.append({"source": selected_index + 1, "target": i + 1})

    return {"userStories": user_stories, "relationships": relationships}
   