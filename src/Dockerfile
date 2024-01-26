# this is the base image we are starting from
FROM python:3

# copy a file from local to current
COPY shop_api /shop_api

# run your commands
RUN pip install /shop_api

# This is the command that is run inside our image when
# we run `docker run <my image>`
WORKDIR /shop_api
CMD ["uvicorn", "shop_api.main:app", "--host", "0.0.0.0"]