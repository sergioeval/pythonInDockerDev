FROM python:3.12.2-alpine 

WORKDIR /code

COPY ./requirements.txt ./
RUN apk add gcc musl-dev linux-headers
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./code ./code

#CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]

#ENTRYPOINT [ "/bin/sh" ]