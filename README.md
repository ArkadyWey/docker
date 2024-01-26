# Docker tutorial

## About

This is a tutorial for the MLE fellowship (last updated Jan 2024).

In this tutorial we will start with a small fast-api application, and we will dockerise and host it!

## Part 1 - Dockerise

Under `src/` folder you will find thee shop_api, which is a simple fast api script which adds items to a shop. We have the poetry config.

### Running locally

 To run this locally, you need poetry installed (`pip install poetry` should do). In the `src/shop_api` folder you need to run `poetry install`. This will create you a virtual environment to work with and install the dependencies as defined in `pyproject.toml` and `pyproject.lock`. Once that is done, start the api server with:
 ```bash
poetry run uvicorn shop_api.main:app --reload
```
Then visit: <http://127.0.0.1:8000/docs>. This is the swagger ui where we can interact with the api. Try sending putting an item, getting that item and listing all the items.

### Now to dockerise

We have code that works localy, lets also try and get it working in docker. Start editing Dockerfile.

Once you are happy try building the image with `docker build -t shop_api .`

Once you are happy with your image run it with `docker run shop_api`