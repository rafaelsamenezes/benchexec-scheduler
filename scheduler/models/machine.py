from datetime import datetime
import json
from .db import db


class Machine(db.Model):
    """
    ORM For a Machine to run Jobs

    Attributes
    ----------
    id : int
        the PK of the Machine
    name : str
        the name of the machine (This is not the hostname) e.g. 'PC1 from Lab A'
    address : str
        the IPv4 or IPv6 of the machine e.g. 127.0.0.1
    is_active : bool
        set if machine is accepting jobs.
    created_at : datetime
        when this machine was added
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(128), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return "<Machine (name='%s', address='%s', is_active='%s')>" % (
            self.name,
            self.address,
            self.is_active)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {'id': self.id,
                'name': self.name,
                'address': self.address}

    @staticmethod
    def delete(pk: int):
        Machine.query.filter_by(id=pk).delete()
        db.session.commit()

    @staticmethod
    def create_machine(name: str, address: str, is_active: bool) -> 'Machine':
        """Create a Machine"""
        return Machine(name=name, address=address, is_active=is_active)

    def check_connectivity(self) -> bool:
        """Check wether the SSH connection is Working"""
        raise NotImplementedError
