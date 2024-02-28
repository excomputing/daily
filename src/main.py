"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point

    :return:
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)

    # The dates
    datestr_ = src.algorithms.dates.Dates().exc()
    logger.info(datestr_)

    # Does the target bucket exist?


if __name__ == '__main__':

    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.algorithms.dates

    main()
