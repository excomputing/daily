"""Module main.py"""
import logging
import os
import sys

import boto3


def main():
    """
    Entry point

    :return:
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)

    # The temporary local storage area
    storage: str = src.algorithms.storage.Storage(
        s3_parameters=s3_parameters).exc()

    # The dates
    datestr_ = src.algorithms.dates.Dates().exc()
    logger.info(datestr_)

    # Reference
    reference = src.algorithms.reference.Reference(s3_parameters=s3_parameters).exc()
    logger.info(reference.head())

    # A parallel execution matrix: [metadata of sequences] ⊗ [dates], i.e., the outer product.
    sequences: list[sq.Sequence] = src.algorithms.vectors.Vectors(
        reference=reference, datestr_=datestr_).exc()
    logger.info(sequences)

    # Execute
    src.data.interface.Interface(service=service, s3_parameters=s3_parameters,
                                 sequences=sequences).exc(storage=storage)

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


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
    import src.algorithms.reference
    import src.algorithms.storage
    import src.algorithms.vectors
    import src.data.interface

    import src.elements.s3_parameters as s3p
    import src.elements.sequence as sq
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service
    import src.s3.s3_parameters
    import src.setup

    # S3 S3Parameters, Service Instance
    connector = boto3.session.Session()
    s3_parameters: s3p.S3Parameters = src.s3.s3_parameters.S3Parameters(connector=connector).exc()
    service: sr.Service = src.functions.service.Service(
        connector=connector, region_name=s3_parameters.region_name).exc()

    # Setting-up
    setup: bool = src.setup.Setup(
        service=service, s3_parameters=s3_parameters).exc()

    main()
