import logging

logger = logging.getLogger(__name__)

class SurveyRouter(object):
    def route_for_task(self, task, args=None, kwargs=None):
        from polls import tasks
        if task == tasks.increment_counter.name:
            return {"queue": "stats"}
        return None
