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
from scheduler.view.base import Base
from scheduler.view.dashboard import Dashboard
from scheduler.view.machines import Machines
from scheduler.view.jobs import Jobs
from scheduler.view.results import Results
from scheduler.models.checks import Checks

bp = Blueprint("web", __name__, url_prefix="/")

M = Machines()
J = Jobs()
R = Results()


def _get_system_info():
        return {"system_check": True, "database_check": False, "machines": 15, "jobs": 74, "active_jobs": 15, "algorithm": "Priority Queue", "version": "0.0.1"}


def _template(layout):
    return render_template(layout._template_path(),
                           **layout.generate_template_args())


@bp.route("/test")
def hello_world():
    """For test"""
    return "OK", 200


@bp.route("/")
def dashboard():
    """Return the dashboard view"""
    return _template(Dashboard(_get_system_info()))


@bp.route("/machines")
def machines():
    """Return the machines view"""
    return _template(M)


@bp.route("/jobs")
def jobs():
    """Return the jobs view"""
    return _template(J)


@bp.route("/results")
def results():
    """Return the results view"""
    return _template(R)
