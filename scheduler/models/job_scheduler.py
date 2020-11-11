import abc
from .job import Job

class JobScheduler(abc.ABC):
    """This ABC will handle scheduling algorithms for benchexec"""

    @abc.abstractmethod
    def schedule_job(self):
        raise NotImplementedError

    @abc.abstractmethod
    def available_machines(self):
        raise NotImplementedError

class PRIOc(JobScheduler):

    def __init__():
        self.scheduler = []

    @staticmethod
    def _priority_sort(job: Job):
        return job.priority

    def next_job(self):
        jobs = Job.query.all()
        jobs.sort(reverse=True, key=PRIOc._priority_sort)
        try:
            return jobs[0]
        except:
            return None