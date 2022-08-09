FROM python:3

COPY ./load_balancer .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=/loadbalancer.py

CMD ["python", "loadbalancer.py"]
