FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN apk update \ 
	&& apk upgrade

# Install python libraries required
RUN apk --no-cache add icu-libs icu-dev gcc g++ \
    && pip3 install --no-cache-dir polyglot futures Morfessor pycld2 PyICU six Flask \
    && apk del icu-dev gcc g++

RUN export FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
