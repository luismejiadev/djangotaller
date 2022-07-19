FROM python:3

# Force the stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED 1

# set env variable for working dir
ENV APP_PROJ=/djangoapp

# create django directory inside docker container & install django
COPY . $APP_PROJ

# create limited user and assign ownership for working directory
RUN useradd polls && chown polls:polls -R $APP_PROJ

# Change working directoring
WORKDIR $APP_PROJ

# install requirements
RUN pip install -r requirements.txt
COPY compose/django/start.sh /start.sh
#set permission for our bash file
RUN chmod +x /start.sh && chown polls:polls /start.sh

USER polls