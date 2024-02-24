import datetime
import logging

import pandas as pd


class Dates:

    def __init__(self):
        """

        """

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, starting: str = '') -> list[str]:

        ends = datetime.datetime.today()

        if starting:
            starts = datetime.datetime.strptime(starting, '%Y-%m-%d')
            values = pd.date_range(start=starts, end=ends, freq='MS').to_list()
            datestr_ = [str(value.date()) for value in values]
        else:
            datestr_ = [str(ends.replace(day=1).date())]

        self.__logger.info('Dates\n%s', datestr_)

        return datestr_
