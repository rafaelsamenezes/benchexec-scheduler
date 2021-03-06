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
from scheduler.models.machine import Machine


bp = Blueprint("machine", __name__, url_prefix="/v0/machine")


@bp.route("/")
def get_all_machines():
    """Get all machines"""
    machines = [x.serialize() for x in Machine.query.all()]
    RESULT = json.dumps(machines)
    MIMETYPE = 'application/json'

    return Response(RESULT, mimetype=MIMETYPE)


@bp.route("/available")
def get_all_available_machines():
    """Get all available machines"""
    machines = [x.serialize() for x in Machine.get_available_machines()]
    RESULT = json.dumps(machines)
    MIMETYPE = 'application/json'

    return Response(RESULT, mimetype=MIMETYPE)


@bp.route("/", methods=['POST'])
def add_new_machine():
    """Add a new machine"""
    body = request.get_json()
    machine = Machine(**body)
    machine.save()
    id = machine.id
    return {'id': str(id)}, 200


@bp.route("/<int:index>", methods=['DELETE'])
def delete_machine(index):
    """Add a new machine"""
    Machine.delete(index)
    return '', 200
