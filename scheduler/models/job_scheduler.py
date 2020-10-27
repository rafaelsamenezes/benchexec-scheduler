import abc

class JobScheduler(abc.ABC):
    """This ABC will handle scheduling algorithms for benchexec"""

    @abc.abstractmethod
    def schedule_job(self):
        raise NotImplementedError

    @abc.abstractmethod
    def available_machines(self):
        raise NotImplementedError
