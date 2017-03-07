"""Unit Test Case for aztec calculator."""
# -*- coding: utf-8 -*-
import unittest

from aztec_calculator.aztec import Aztec

"""Run Test.

$ python -m unittest discover -v tests -p test_aztec.py

"""


class AztecTestCase(unittest.TestCase):
    """Test class for validate correct functionality of Aztec Calculator."""

    VERSION = '0.1.5'
    NAME = 'azTec'
    MODE = [1, 2, 3]
    DEFAULT_MODE = 1

    def setUp(self):
        """Setup for each test."""
        self.calc = Aztec(self.DEFAULT_MODE)

    def tearDown(self):
        """Shutdown of calc instance."""
        self.calc = None

    def test_get_calculator_name(self):
        """Calculator name test."""
        self.assertEqual(
            self.NAME,
            self.calc.get_calculator_name(),
            'message'
        )

    def test_get_calculator_version(self):
        """Calculator version test."""
        self.assertEqual(
            self.VERSION, self.calc.get_calculator_version(),
            'message'
        )

    def test_get_calculator_mode(self):
        """Calculator mode test."""
        for i in self.MODE:
            self.calc.set_calculator_mode(i + 1)
            self.assertEqual(i + 1, self.calc.get_calculator_mode(), 'message')

    def test_calculate_large(self):
        """Calculator large test."""
        self.calc.set_calculator_mode(1)
        map_area = 100
        dd = 0.2
        self.assertEqual(
            {'Hr': 113.63636363636363},
            self.calc.calculate(map_area=map_area, dd=dd),
            'message'
        )

    def test_calculate_small(self):
        """Calculator small test."""
        self.calc.set_calculator_mode(2)
        dd = 0.2
        rounded = 2
        self.assertEqual(
            {'Hr': 9.02},
            self.calc.calculate(dd=dd, rounded=rounded),
            'message'
        )

    def test_calculate_photometry(self):
        """Calculator photometry test."""
        self.calc.set_calculator_mode(3)
        s = 5
        snr = 10
        rounded = 2
        self.assertEqual(
            {'Sec': 1318.51, 'arcsec': 0.06},
            self.calc.calculate(s=s, snr=snr, rounded=rounded),
            'message'
        )

    def test_expect_error_divided_by_cero(self):
        """Catch calculator divided by cero error."""
        self.calc.set_calculator_mode(1)
        dd = 0
        map_area = 100
        with self.assertRaises(ZeroDivisionError) as context:
            self.calc.calculate(dd=dd, map_area=map_area)

    def test_expect_error_mode_code_greater(self):
        """Expected raises an exception when passing a value greater than 3."""
        self.calc.set_calculator_mode(4)
        with self.assertRaises(Exception) as context:
            self.calculate()

    def test_expect_error_mode_code_less(self):
        """Expected raises an exception when passing a value lesser than 1."""
        self.calc.set_calculator_mode(0)
        with self.assertRaises(Exception) as context:
            self.calculate()

    def test_round_decimals(self):
        """Expected a return value with no more than 2 decimals."""
        self.calc.set_calculator_mode(1)
        map_area = 100
        dd = 0.2
        rounded = 2
        self.assertEqual(
            {'Hr': 113.64},
            self.calc.calculate(map_area=map_area, dd=dd, rounded=rounded),
            'message'
        )

suite = unittest.TestLoader().loadTestsFromTestCase(AztecTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
