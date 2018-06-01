# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.controllers.e911s_controller

    This file was automatically generated by APIMATIC v2.0 (https://apimatic.io)
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration


class E911sController(BaseController):

    """A Controller to access Endpoints in the
        flowroutenumbersandmessaging API."""

    def list_e911s(self,
                   limit=None,
                   offset=None,
                   state=None):
        """Does a GET request to /v2/e911s.

        Returns a list of all Central Office (exchange) codes containing
        purchasable phone numbers.

        Args:
            limit (int, optional): Limits the number of items to retrieve. A
                maximum of 200 items can be retrieved.
            offset (int, optional): Offsets the list of phone numbers by your
                specified value. For example, if you have 4 phone numbers and
                you entered 1 as your offset value, then only 3 of your phone
                numbers will be displayed in the response.
            state (2 char, optional): Restricts the results to the specified
                state.

        Returns:
            mixed: Response from the API. A JSON object of E911 Records
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s'
        _query_parameters = {
            'limit': limit,
            'offset': offset,
            'state': state
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder, _query_parameters,
            Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def get_e911(self, e911_id):
        """Does a GET request to /v2/e911s/<e911_id>.

        Returns a record detail for the E911 Record Id specified

        Args:

        Returns:
            mixed: Response from the API. A JSON object of of an E911 record
             that satisfy your search criteria.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s/{}'.format(e911_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

    def validate_address(self,
                         label,
                         first_name,
                         last_name,
                         street_name,
                         street_number,
                         city,
                         state,
                         country,
                         zipcode):
        """Does a POST request to /v2/e911s/validate.

        Returns a 204 No Content on success, or a 404 with error data

        Args:
            label (string): the alias or friendly name of your entry
            first_name (string):
            last_name (string):
            street_name (string):
            street_number (string):
            city (string):
            state (2 character string):
            country (string USA or Canada):
            zipcode (string postal code)

        Returns:
            mixed: Response from the API. A 204 - No Content or a
            JSON object ith error data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        body = {
            'data': {
                'type': 'e911',
                'attributes': {
                    'label': label,
                    'first_name': first_name,
                    'last_name': last_name,
                    'street_name': street_name,
                    'street_number': street_number,
                    'city': city,
                    'state': state,
                    'country': country,
                    'zip': zipcode
                }
            }
        }

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s/validate'

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=APIHelper.json_serialize(
                                             body))

        return self.handle_request_and_response(_request)

    def create_address(self,
                       label,
                       first_name,
                       last_name,
                       street_name,
                       street_number,
                       city,
                       state,
                       country,
                       zipcode):
        """Does a POST request to /v2/e911s.

        Creates an address record that can then be associated
        with 1 or more DIDs

        Args:
            label (string): the alias or friendly name of your entry
            first_name (string):
            last_name (string):
            street_name (string):
            street_number (string):
            city (string):
            state (2 character string):
            country (string USA or Canada):
            zipcode (string postal code)

        Returns:
            mixed: Response from the API. A JSON object containing the new
            record information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        body = {
            'data': {
                'type': 'e911',
                'attributes': {
                    'label': label,
                    'first_name': first_name,
                    'last_name': last_name,
                    'street_name': street_name,
                    'street_number': street_number,
                    'city': city,
                    'state': state,
                    'country': country,
                    'zip': zipcode
                }
            }
        }

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s'

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=APIHelper.json_serialize(
                                             body))

        return self.handle_request_and_response(_request)

    def update_address(self,
                       e911_id,
                       label=None,
                       first_name=None,
                       last_name=None,
                       street_name=None,
                       street_number=None,
                       city=None,
                       state=None,
                       country=None,
                       zipcode=None):

        """Does a PATCH request to /v2/e911s/<e911_id>.

        Updates an existing address record and any associations it may have

        Args:
            e911_id (integer, required): the id of the e911 record to update
            label (string, optional): the alias or friendly name of your entry
            first_name (string, optional):
            last_name (string, optional):
            street_name (string, optional):
            street_number (string, optional):
            city (string, optional):
            state (2 character string, optional):
            country (string USA or Canada, optional):
            zipcode (string postal code, optional)

        Returns:
            mixed: Response from the API. A JSON object containing the
            new record information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        cur_record = self.get_e911(e911_id)
        record_data = cur_record

        # Only update the fields specified
        if label is not None:
            record_data['data']['attributes']['label'] = label
        if first_name is not None:
            record_data['data']['attributes']['first_name'] = first_name
        if last_name is not None:
            record_data['data']['attributes']['last_name'] = last_name
        if street_name is not None:
            record_data['data']['attributes']['street_name'] = street_name
        if street_number is not None:
            record_data['data']['attributes']['street_number'] = \
                str(street_number)
        if city is not None:
            record_data['data']['attributes']['city'] = city
        if state is not None:
            record_data['data']['attributes']['state'] = state
        if country is not None:
            record_data['data']['attributes']['country'] = country
        if zipcode is not None:
            record_data['data']['attributes']['zip'] = str(zipcode)
            record_data['data']['attributes']['zip_code'] = str(zipcode)

        # Fix address_type if not used
        if 'address_type' in record_data['data']['attributes'] and \
                record_data['data']['attributes']['address_type'] == u'':
            record_data['data']['attributes'].pop('address_type', None)
            record_data['data']['attributes'].pop('address_type_number', None)

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s/{}'.format(e911_id)

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers,
                                          parameters=APIHelper.json_serialize(
                                              record_data))

        return self.handle_request_and_response(_request)

    def delete_address(self, e911_id):
        """Performs a DELETE request to /v2/e911s/<e911_id>.

        Removes the existing address record and any associations it may have

        Args:
            e911_id (integer, required): the id of the e911 record to update

        Returns:
            mixed: Response from the API. A 204 - No Content or a
            JSON object ith error data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s/{}'.format(e911_id)

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def associate(self, e911_id, did):
        """Does a PATCH request to /v2/numbers/<did>/relationships/e911s/<e911_id>.

        Associates the specified e911 record with the specified did

        Args:
            e911_id (integer, required): the id of the e911 record to update
            did (string, required): the phone number to associate with

        Returns:
            mixed: Response from the API. A 204 - No Content or a
            JSON object ith error data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/e911s/{}'.format(did,
                                                                         e911_id)

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def disconnect(self, did):
        """Does a DELETE request to /v2/numbers/<did>/relationships/e911s.

        Un-Associates the specified e911 record with the specified did

        Args:
            did (string, required): the phone number to associate with

        Returns:
            mixed: Response from the API. A 204 - No Content or a
            JSON object ith error data

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/numbers/{}/relationships/e911s'.format(did)

        # Return appropriate type
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/vnd.api+json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)

        return self.handle_request_and_response(_request)

    def list_dids_for_e911(self, e911_id):
        """Does a GET request to /v2/e911s/<e911_id>/relationships/numbers

        Lists all Did records associated with the specified E911 record

        Args:
            e911_id (integer, required): the id of the e911 record to query

        Returns:
            mixed: Response from the API. A JSON Object list with the associated
              DID records
        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/v2/e911s/{}'.format(e911_id)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)

        return self.handle_request_and_response(_request)

