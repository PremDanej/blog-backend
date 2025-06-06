import uvicorn
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    host = os.getenv("HOST")
    port = os.getenv("PORT")

    uvicorn.run(
        app="blog.main:app",
        host=host,
        port=int(port),
        reload=True,
    )
