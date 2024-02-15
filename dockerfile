FROM python:3
WORKDIR /home/Docker/rec
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
COPY . .
CMD ["python", "./recommender_driver.py"]