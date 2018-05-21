# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.porting_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..exceptions.error_exception import ErrorException
from .numbers_controller import NumbersController

class PortingController(BaseController):

    """A Controller to access Endpoints in the
        flowroutenumbersandmessaging API."""

    def checkPortability(self, numbers):
        """Does a POST request to /v2/portorders/portability.

        Args:
            numbers (list: comma delimited list of strings, required):
            Phone numbers to check

        Returns:
            mixed: Response from the API. A JSON object of the status of each
            number specified

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        body = {
            "numbers": numbers
        }

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/portorders/portability'
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=body)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def associate_cnam(self, cnam_id, phone_number):
        # first, verify the number belongs to the user
        did = NumbersController().list_account_phone_numbers(contains=phone_number)

        if did is None:
            error_string = "Error, this phone number does not belong to you."
            return error_string

        did = did['data'][0]['id']

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/cnam/{}'.format(did, cnam_id)
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def unassociate_cnam(self, phone_number):
        # first, verify the number belongs to the user
        did = NumbersController().list_account_phone_numbers(contains=phone_number)

        if did is None:
            error_string = "Error, this phone number does not belong to you."
            return error_string

        did = did['data'][0]['id']

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/cnam'.format(did)
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def remove_cnam(self, cnam_id):
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/cnams/{}'.format(cnam_id)
        _query_url = APIHelper.clean_url(_query_builder)
        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise ErrorException('Unauthorized – There was an issue with your API credentials.', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('The specified resource was not found', _context)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)
