#!/usr/bin/env python

"""Tests for `pitrading` package."""


from pitrading.holidays import Holidays
import unittest

from pitrading import pitrading


class TestPitrading(unittest.TestCase):
    """Tests for `pitrading` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        # Holidays.range_exp("20150101", "20280101")
        # Holidays.range_exp("20050101", "20180101")
        Holidays.range_exp("20150101", "20180101")
