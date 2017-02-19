# -*- coding: utf-8 -*-
"""Run Test.
$ python -m unittest discover -v tests -p test_aztec.py
"""
import unittest
from aztec_calculator.aztec import Aztec

class AztecTestCase(unittest.TestCase):
    """Test class for validate correct functionality of Aztec Calculator."""
    VERSION = '0.1.0'
    NAME = 'azTec'
    MODE = [1, 2, 3]

    def setUp(self):
        self.calc = Aztec(1)

    def tearDown(self):
        self.calc = None

    def test_get_calculator_name(self):
        self.assertEqual(
            self.NAME,
            self.calc.get_calculator_name(),
            'message'
        )

    def test_get_calculator_version(self):
        self.assertEqual(
            self.VERSION, self.calc.get_calculator_version(),
            'message'
        )

    def test_get_calculator_mode(self):
        for i in self.MODE:
            self.calc.set_calculator_mode(i + 1)
            self.assertEqual(i + 1, self.calc.get_calculator_mode(), 'message')

    def test_calculate_large(self):
        self.calc.set_calculator_mode(1)
        map_area = 100
        dd = 0.2
        self.assertEqual(
            {'Hr': 113.64},
            self.calc.calculate(map_area=map_area, dd=dd),
            'message'
        )

    def test_calculate_small(self):
        self.calc.set_calculator_mode(2)
        nefd = 4.9
        dd = 0.2
        self.assertEqual(
            {'Hr': 9.02},
            self.calc.calculate(nefd=nefd, dd=dd),
            'message'
        )

    def test_calculate_photometry(self):
        self.calc.set_calculator_mode(3)
        nefd = 4.9
        s = 5
        snr = 10
        self.assertEqual(
            {'Sec': 1318.51, 'arcsec': 0.06},
            self.calc.calculate(nefd=nefd, s=s, snr=snr),
            'message'
        )


suite = unittest.TestLoader().loadTestsFromTestCase(AztecTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
