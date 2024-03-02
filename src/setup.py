"""
Module setup.py
"""
import logging

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.functions.directories
import src.s3.bucket


class Setup:

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this project, e.g., region code
                              name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        # An instance for interacting with Amazon S3 buckets.
        bucket = src.s3.bucket.Bucket(service=self.__service, location_constraint=self.__s3_parameters.location_constraint,
                                      bucket_name=self.__s3_parameters.internal)

        return bucket.exists()

    def __local(self) -> bool:
        """

        :return:
        """

        # An instance for interacting with local directories
        directories = src.functions.directories.Directories()

        # The warehouse
        return directories.cleanup(path=self.__configurations.warehouse)

    def exc(self) -> bool:
        """

        :return:
        """

        if not self.__s3():
            logging.log(level=logging.INFO,
                        msg='The bucket does not exist, please run an instance of the image <pollutants> first.')
            exit(1)

        if not self.__local():
            logging.log(level=logging.INFO, msg='Local settings failure.')
            exit(1)

        return True
