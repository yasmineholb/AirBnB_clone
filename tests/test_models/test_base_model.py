#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class testbase(unittest.TestCase):
    """
    unittests for BaseModel class
    """
    def test_id(self):
        """
        check id
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
