FROM python:3

RUN pip install flask
COPY ./target_app/app.py /app/app.py
ENV FLASK_APP=/app/app.py

CMD ["python", "app/app.py"]
