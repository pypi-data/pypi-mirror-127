# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flywheel.api_client import ApiClient
import flywheel.models

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class CallbacksApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def callback_virus_scan(self, container_type, container_id, file_name, body, **kwargs):  # noqa: E501
        """Callback url to send the virus scan result of a file.

        This endpoint accepts the result from the anti-virus service.  NOTE: this endpoint only can be used via a signed url. 
        This method makes a synchronous HTTP request by default.

        :param str container_type: (required)
        :param str container_id: (required)
        :param str file_name: (required)
        :param CallbacksVirusScanInput body: (required)
        :param str signature: Url's signature (signed callback url)
        :param str expires: Signed url expiration time (epoch time)
        :param bool async_: Perform the request asynchronously
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.callback_virus_scan_with_http_info(container_type, container_id, file_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.callback_virus_scan_with_http_info(container_type, container_id, file_name, body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def callback_virus_scan_with_http_info(self, container_type, container_id, file_name, body, **kwargs):  # noqa: E501
        """Callback url to send the virus scan result of a file.

        This endpoint accepts the result from the anti-virus service.  NOTE: this endpoint only can be used via a signed url. 
        This method makes a synchronous HTTP request by default.

        :param str container_type: (required)
        :param str container_id: (required)
        :param str file_name: (required)
        :param CallbacksVirusScanInput body: (required)
        :param str signature: Url's signature (signed callback url)
        :param str expires: Signed url expiration time (epoch time)
        :param bool async: Perform the request asynchronously
        :return: None
        """

        all_params = ['container_type','container_id','file_name','body','signature','expires',]  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method callback_virus_scan" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_type' is set
        if ('container_type' not in params or
                params['container_type'] is None):
            raise ValueError("Missing the required parameter `container_type` when calling `callback_virus_scan`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `callback_virus_scan`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `callback_virus_scan`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `callback_virus_scan`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_type' in params:
            path_params['ContainerType'] = params['container_type']  # noqa: E501
        if 'container_id' in params:
            path_params['ContainerId'] = params['container_id']  # noqa: E501
        if 'file_name' in params:
            path_params['FileName'] = params['file_name']  # noqa: E501

        query_params = []
        if 'signature' in params:
            query_params.append(('signature', params['signature']))  # noqa: E501
        if 'expires' in params:
            query_params.append(('expires', params['expires']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.CallbacksVirusScanInput.positional_to_model(params['body'])
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/callbacks/virus-scan/{ContainerType}/{ContainerId}/files/{FileName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)
