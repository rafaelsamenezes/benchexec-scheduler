from datetime import datetime
from .db import db
from .machine import Machine


class Job(db.Model):
    """
    ORM for a Job description

    Attributes
    ----------
    id : int
        the PK of the Job
    description : str
        the description of the job e.g. "Run with esbmc v6.5"
    flags : str
        flags to be sent to benchexec e.g --timeout 500 --threads 4
    def_file_path : str
        path of the definition file e.g /tmp/esbmc.xml
    tool_path : str
        path of the tool e.g /tmp/esbmc.zip
    priority : int
        priority of the job (higher is more)
    status : int
        current status of job (Running, Not Running, Finished)    
    created_at : datetime
        when this machine was added

    STATUS
    """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    flags = db.Column(db.Text, default='')
    status = db.Column(db.Integer, nullable=False, default=0)
    def_file_path = db.Column(db.Text, default='')
    tool_path = db.Column(db.Text, default='')
    priority = db.Column(db.Integer, default=2)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    STATUS = {0: "Not Started", 1: "Running", 2: "Finished"}

    def __repr__(self):
        return "<Job (description='%s', status='%s', priority='%s')>" % (
            self.description,
            Job.STATUS[self.status],
            self.priority)

    @staticmethod
    def get_available_jobs():
        js = Job.query.all()
        return [j for j in js if j.status == 0]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {'id': self.id,
                'description': self.description,
                'flags': self.flags,
                'status': Job.STATUS[self.status],
                'priority': self.priority}

    @staticmethod
    def delete(pk: int):
        Job.query.filter_by(id=pk).delete()
        db.session.commit()