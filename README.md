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