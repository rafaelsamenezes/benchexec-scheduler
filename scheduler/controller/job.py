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
from scheduler.models.job import Job


bp = Blueprint("job", __name__, url_prefix="/v0/job")


@bp.route("/")
def get_all_jobs():
    """Get all jobs"""
    jobs = [x.serialize() for x in Job.query.all()]
    RESULT = json.dumps(jobs)
    MIMETYPE = 'application/json'

    return Response(RESULT, mimetype=MIMETYPE)


@bp.route("/", methods=['POST'])
def add_new_job():
    """Add a new job"""
    body = request.get_json()
    job = Job(**body)
    job.save()
    id = job.id
    return {'id': str(id)}, 200


@bp.route("/<int:index>", methods=['DELETE'])
def delete_job(index):
    """Cancel a job"""
    Job.delete(index)
    return '', 200
