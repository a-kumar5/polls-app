# base image
FROM python:3.12

# set work directory
RUN mkdir -p /mypage

COPY requirements.txt .

RUN pip install -r requirements.txt

# where your code lives
WORKDIR /mypage

# copy whole project to your docker home directory.
COPY .. /mypage

# port where the Django app runs
EXPOSE 8000

# start server
CMD python manage.py runserver