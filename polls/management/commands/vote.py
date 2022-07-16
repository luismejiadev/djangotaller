import os, sys
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.core.management.commands.loaddata import Command as LoadDataCommand
from django.conf import settings
from django.db import connection

from polls.models import Question, Choice
from polls.tasks import *


class Command(BaseCommand):
    help = 'vote for a choice'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('choice_id', type=int)


    def success_msg(self, question_code):
        msg = 'Vote successfully'
        self.stdout.write(self.style.SUCCESS(msg))

    def handle(self, *args, **options):
        choice_id = options.get('choice')
        if not choice_id:
            sys.exit()

        increment_vote.delay(choice_id)
        increment_counter.delay(choice_id)