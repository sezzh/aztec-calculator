"""Class which executes all logic of caculation."""
# -*- coding: utf-8 -*-


class Aztec(object):
    """Aztec calculator class."""

    # Class attributes.
    FWHM = 444
    NEFD = 4.9
    VERSION = '0.1.5'
    NAME = 'azTec'

    def __init__(self, mode):
        """Constructor which recives at least a mode.

        Params:
            mode -> (Integer) between 1 to 3.
        """
        self.__mode = mode
        self.__name = self.NAME
        self.__version = self.VERSION
        self.__kwargs = None
        self.__validate_mode()

    def get_calculator_name(self):
        """Return the defined calculator's name."""
        return self.__name

    def get_calculator_version(self):
        """Return the defined calculator's version."""
        return self.__version

    def get_calculator_mode(self):
        """Return current calculator's mode."""
        return self.__mode

    def set_calculator_mode(self, mode):
        """Change the current calculator's mode.

        This method changes calculator's mode which will be use to perform the
        calculation via aztec.calculate(**kwargs) method.

        Params args:
        mode -> (Integer) between 1 to 3.
        """
        self.__mode = mode

    def __calculate_large(self):
        """Return the result of large's formula."""
        return (self.__kwargs['map_area'] / (22 * (self.__kwargs['dd']**2)))

    def __calculate_small(self):
        """Return the result of small's formula."""
        return (((((float(2.6) * float(self.__kwargs['nefd']))) /
                float(self.__kwargs['dd']))**2) *
                (float(8) / float(3600)))

    def __calculate_photometry(self):
        """Return the result dict of Time integration & positional methods."""
        result = {}
        result['Sec'] = self.__round_decimals(
            self.__calculate_time_integration()
        )
        result['arcsec'] = self.__round_decimals(
            self.__calculate_positional_uncertainty()
        )
        return result

    def __calculate_time_integration(self):
        """Return the result of time integration's formula."""
        return ((8) * (((1.31 * self.__kwargs['nefd'] * self.__kwargs['snr']) /
                (self.__kwargs['s']))**2))

    def __calculate_positional_uncertainty(self):
        """Return the result of positional's formula."""
        return ((0.6 * self.FWHM) / (self.__kwargs['snr']))

    def calculate(self, **kwargs):
        """Return the result of the given mode. with the expected keyword args.

        This is the method you must execute in order to perform calculus and
        get a result dict.

        Params keyword arguments:

        map_area -> (Integer).
        dd -> (Float).
        nefd -> (Float).
        s -> (Integer).
        snr -> (Integer).
        rounded -> (Integer).

        Returns:

        Dict
        """
        # validate mode must be between 1 to 3.
        self.__validate_mode()

        result = {}
        self.__kwargs = kwargs
        self.__kwargs['nefd'] = self.NEFD
        try:
            if self.__mode == 1:
                result['Hr'] = self.__round_decimals(self.__calculate_large())
            elif self.__mode == 2:
                result['Hr'] = self.__round_decimals(self.__calculate_small())
            elif self.__mode == 3:
                result = self.__calculate_photometry()
        except Exception as e:
            raise e
        return result

    def __validate_mode(self):
        """Method which validates modes between 1 to 3."""
        if self.__mode < 1:
            raise Exception('MODE must be greater than 0')
        elif self.__mode > 3:
            raise Exception('MODE must be lesser than 4')

    def __round_decimals(self, callback):
        """Method which returns the result of the formulas rounded."""
        if 'rounded' in self.__kwargs:
            return round(callback, self.__kwargs['rounded'])
        else:
            return callback
