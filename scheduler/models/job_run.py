from datetime import datetime
from .db import db
from .job import Job
from .machine import Machine

class JobRun(db.Model):
    """
    ORM for a Job Execution

    Attributes
    ----------
    id : int
        the PK of the Machine
    machine : Machine
        the machine assigned to run the job
    job : str
        the job assigned
    result_path : str
        the path were the result will stored e.g /tmp/output.zip
    created_at : datetime
        when this machine was added
    """

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('machine.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    result_path = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relations
    ## A machine can have multiple jobs (this will be determined by the scheduler)
    machine = db.relationship('Machine', backref=db.backref('jobruns'))
    ## A job can be executed by only one machine
    job = db.relationship('Job', uselist=False, backref=db.backref('jobrun'))

    # Metadata


    def __repr__(self):
        return "<JobRun (machine='%s', job='%s')>" % (
            self.machine,
            self.job)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {'id': self.id,
                'machine': self.machine.serialize(),
                'job': self.job.serialize()}

    @staticmethod
    def delete(pk: int):
        JobRun.query.filter_by(id=pk).delete()
        db.session.commit()