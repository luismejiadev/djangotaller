#!/bin/bash
docker-compose run polls-rabbitmq watch -d '/usr/sbin/rabbitmqctl list_queues -p survey_app name messages messages_ready messages_unacknowledged consumers| sort'