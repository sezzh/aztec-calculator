# -*- coding: utf-8 -*-

class Aztec(object):
    """docstring for AztecCalculator."""

    # Class constants
    FWHM = 1
    NEFD = 4.9
    VERSION = '0.1.0'
    NAME = 'azTec'

    def __init__(self, mode):
        self.__mode = mode
        self.__name = self.NAME
        self.__version = self.VERSION
        self.__kwargs = None

    def get_calculator_name(self):
        return self.__name

    def get_calculator_version(self):
        return self.__version

    def get_calculator_mode(self):
        return self.__mode

    def set_calculator_mode(self, mode):
        self.__mode = mode

    def __calculate_large(self):
        return float('{0:.2f}'.format(self.__kwargs['map_area']/ \
            (22*(self.__kwargs['dd']**2))))

    def __calculate_small(self):
        return float('{0:.2f}'.format(((((2.6*self.__kwargs['nefd']))/ \
                self.__kwargs['dd'])**2)*(8/3600)))

    def __calculate_photometry(self):
        result = {}
        result['Sec'] = self.__calculate_time_integration()
        result['arcsec'] = self.__calculate_positional_uncertainty()
        return result


    def __calculate_time_integration(self):
        return float('{0:.2f}'.format((8)*((\
        (1.31*self.__kwargs['nefd']*self.__kwargs['snr'])/\
        (self.__kwargs['s']))**2)))

    def __calculate_positional_uncertainty(self):
        return float('{0:.2f}'.format((0.6*self.FWHM)/(self.__kwargs['snr'])))

    def calculate(self, **kwargs):
        result = {}
        self.__kwargs = kwargs
        if self.__mode == 1:
            result['Hr'] = self.__calculate_large()
        elif self.__mode == 2:
            result['Hr'] = self.__calculate_small()
        elif self.__mode == 3:
            result = self.__calculate_photometry()
        return result
