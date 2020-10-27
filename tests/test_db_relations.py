import sys, os
import tempfile

import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import scheduler.models.machine as M
import scheduler.models.job as J
import scheduler.models.job_run as JR

@pytest.fixture
def machines():
    M0 = M.Machine.create_machine("M0", '0.0.0.0', True)
    M1 = M.Machine.create_machine("M1", '0.0.0.1', False)
    M2 = M.Machine.create_machine("M2", '0.0.0.2', True)
    return [M0,M1,M2]


def test_machines(machines):
    assert machines[0].is_active == True
    assert machines[1].is_active == False
    assert machines[2].is_active == True

    assert machines[0].name == "M0"
    assert machines[1].name == "M1"
    assert machines[2].name == "M2"

    assert machines[0].address == "0.0.0.0"
    assert machines[1].address == "0.0.0.1"
    assert machines[2].address == "0.0.0.2"

    assert machines[0] != machines[1]
    assert machines[0] == machines[0]

@pytest.fixture
def jobs():
    J0 = J.Job(description="Job Equal")
    J1 = J.Job(description="Job Equal")
    J2 = J.Job(description="Job 2")

    return [J0, J1, J2]

def test_jobs(jobs):
    assert jobs[0].description == "Job Equal"
    assert jobs[1].description == "Job Equal"
    assert jobs[2].description == "Job 2"

    assert jobs[0] != jobs[1]
    assert jobs[0] == jobs[0]

@pytest.fixture
def job_runs(machines, jobs):
    JR0 = JR.JobRun(machine=machines[0], job=jobs[0])
    JR1 = JR.JobRun(machine=machines[1], job=jobs[1])
    return [JR0, JR1]

def test_job_run(job_runs, machines, jobs):
    assert job_runs[0] == job_runs[0]
    assert job_runs[1] != job_runs[0]

    assert job_runs[0].machine == machines[0]
    assert job_runs[0].job == jobs[0]

    assert job_runs[1].machine == machines[1]
    assert job_runs[1].job == jobs[1]
