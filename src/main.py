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

    # Reference
    reference = src.algorithms.reference.Reference(service=service, s3_parameters=s3_parameters).exc()
    logger.info(reference.head())


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
    import src.s3.s3_parameters
    import src.functions.service
    import src.setup
    import src.algorithms.reference

    # S3 Parameters
    s3_parameters = src.s3.s3_parameters.S3Parameters().exc()

    # Services
    service = src.functions.service.Service(region_name=s3_parameters.region_name).exc()

    # Setting-up
    setup: bool = src.setup.Setup(
        service=service, s3_parameters=s3_parameters).exc()

    main()
