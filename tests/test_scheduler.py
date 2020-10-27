import sys, os
import tempfile

import pytest

def test_config(default_create_app):
    """Test create_app without passing test config."""
    assert not default_create_app().testing
    assert default_create_app({"TESTING": True}).testing