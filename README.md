# fast_docker
Fast api running in a docker container to upload to aws beanstalk 

Specifically:
my stretch goal for the weekend is to refamiliarize myself with AWS. I am going to do this by creating a fastapi app, running on uvicorn web server(like Mike was using), connected to a postgresql db, where I have route examples for Post Get Put Delete (CRUD), make sure I implement database.fetch_all(query) instead of fetch_one,  put everything into a docker-container and then upload to aws elastic beanstalk to test it out live.
This is exciting puzzle week


Following along the link at 
https://testdriven.io/blog/fastapi-crud/

Dependencies:

FastAPI v0.46.0
Docker v19.03.5
Python v3.8.1
Pytest v5.3.2
Databases v0.2.6

I needed to update the databases repo to version 0.3.2 to be compatible with python 3.8.1

also added 

$ pip install databases[postgresql] for production/dev db
$ pip install databases[sqlite] for testing db

So, we started with an Alpine-based Docker image for Python 3.8.1. We then set a working directory along with two environment variables:

PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
Finally, we copied over the requirements.txt file, installed some system-level dependencies, updated Pip, installed the requirements, and copied over the FastAPI app itself.



So, when the container spins up, Uvicorn will run with the following settings:

--reload enables auto-reload so the server will restart after changes are made to the code base.
--workers 1 provides a single worker process.
--host 0.0.0.0 defines the address to host the server on.
--port 8000 defines the port to host the server on.
app.main:app tells Uvicorn where it can find the FastAPI ASGI application -- e.g., "within the 'app' module, you'll find the ASGI app, app = FastAPI(), in the 'main.py' file.