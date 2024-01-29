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

Things to consider:

- Even though we were using poetry locall, you can do a `pip install .` too
- Do we need to change the command? Play arround
- Can you not see the api in your browser? Have you tought about networking?

### Push image to gitlab

Now that we have created an image, we can push it to gitlab. Usually we have CICD to build our images. Lets do a manual push for now.


# Part 2 - What about state?

We have an api but we are dealing with state weird. We are keeping it in memory. So if our application dies, we lose all that info. Lets do one better and save it outside of the container as a json file.

- Mount a volume
- try stopping and starting the container, does the state persist?
- At this stage there are probably too many arguments. Try putting it in a docker compose file

# Part 3 - Multi Containers

A more realistic setup is to perhaps use a DB. Lets configure Redis.

- Add Redis to your docker compose
- How does networking between redis and your api work?
- Set Redis to have auth, how do we set auth info, and how do we pass auth info to our app?

# Part 4 - Minikube

Let's have a go at moving our application to kuberentes. We can start with Minikube, which is a locally hosted kuberentes service. Lets initially focus on getting all installed and running locally, and run the [hello world example](https://minikube.sigs.k8s.io/docs/start/).

- Lets write a minimal .yaml file for our application (First the version with no Redis)
- Now the .json saving version with mounting filesystem
- Now spinning up a Redis DB