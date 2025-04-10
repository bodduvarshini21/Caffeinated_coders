from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router# Create the FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Include the router
app.include_router(router)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)