FROM python:3.9

WORKDIR ./

COPY ./app /app/
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# Expose the port
ENV PORT=3000
EXPOSE ${PORT}

CMD ["unvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "$PORT"]