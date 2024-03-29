from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import keyword  # Corrected import statement

# Create a FastAPI instance
app = FastAPI(
    title="search_keyword_on_youtube",
    version="1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],  # Changed to GET method as we are only reading data
    allow_headers=["*"],
)
app.include_router(keyword)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)

