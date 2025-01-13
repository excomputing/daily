"""
Module reference.py
"""
import pandas as pd

import config
import src.elements.s3_parameters as s3p
import src.elements.text_attributes as txa
import src.functions.streams


class Reference:
    """

    Notes
    -----

    Each instance of the reference data frame describes the characteristics of a unique sequence of
    telemetric data.  The details include sequence identification code, the geographic coordinates of
    the telemetric device, the pollutant being measured, the unit of measure, etc.
    """

    def __init__(self, s3_parameters: s3p.S3Parameters):
        """

        :param s3_parameters:
        """

        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

        # S3 Unload Instance
        self.__streams = src.functions.streams.Streams()

    def __read(self, filename: str) -> pd.DataFrame:
        """

        :param filename: the name of the Amazon S3 (Simple Storage Service) file being read.
        :return:
        """

        uri = f's3://{self.__s3_parameters.internal}/{self.__s3_parameters.path_internal_references}{filename}'
        text = txa.TextAttributes(uri=uri, header=0)

        return self.__streams.api(text=text)

    def __excerpt(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        # Extract the records in focus.
        excerpt = blob.copy().loc[blob['sequence_id'].isin(self.__configurations.sequence_id_filter), :]

        return excerpt

    def exc(self) -> pd.DataFrame:
        """

        :return:
          data : DataFrame
            An integration of (a) substances metadata, (b) stations gazetteer data,
            and (c) telemetric devices metadata, i.e., the registry.
        """

        # The frame of reference data
        frame = self.__read(filename='reference.csv')

        # Excerpt
        reference: pd.DataFrame = self.__excerpt(blob=frame)

        return reference
