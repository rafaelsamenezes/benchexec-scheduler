import functools

from flask import Blueprint, Response
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

import json
from scheduler.models.job_run import JobRun
from scheduler.models.machine import Machine
from scheduler.models.job import Job


bp = Blueprint("job_run", __name__, url_prefix="/v0/job_run")


@bp.route("/")
def get_all_jobs():
    """Get all jobs"""
    jobs = [x.serialize() for x in JobRun.query.all()]
    RESULT = json.dumps(jobs)
    MIMETYPE = 'application/json'

    return Response(RESULT, mimetype=MIMETYPE)


@bp.route("/", methods=['POST'])
def add_new_job():
    """Add a new job"""
    body = request.get_json()
    machine_id = body['machine_id']
    job_id = body['job_id']
    machine = Machine.query.get(machine_id)
    job = Job.query.get(job_id)
    job_run = JobRun(machine=machine, job=job)
    job_run.save()
    id = job_run.id
    return {'id': str(id)}, 200


@bp.route("/<int:index>", methods=['DELETE'])
def delete_job(index):
    """Cancel a job"""
    JobRun.delete(index)
    return '', 200
