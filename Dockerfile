FROM python:3.10.11-alpine

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#lib for crytography in python
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

COPY . .

EXPOSE 5000

# CMD [ "flask", "db", "upgrade", "&&", "python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD flask db upgrade && python3 -m flask run --host=0.0.0.0
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

