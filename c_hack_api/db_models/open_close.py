"""
Module containing database models for everything concerning Open/Close.
"""

from .. import DB
from . import STD_STRING_SIZE

class OpenClose(DB.Model):
    """
    The representation of a Beverage
    """

    __tablename__ = 'OpenClose'

    id = DB.Column(DB.Integer, primary_key=True)
    begin = DB.Column(DB.BigInteger)
    end = DB.Column(DB.BigInteger)
    comment = DB.Column(DB.Text)

    def __init__(self, begin: int, end: int, comment: str = ""):
        self.begin = begin
        self.end = end
        self.comment = comment

    def update(self, begin: int, end: int, comment: str = ""):
        self.begin = begin
        self.end = end
        self.comment = comment