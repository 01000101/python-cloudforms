'''Cloudforms - Core exceptions'''


class CloudformsError(Exception):
    '''The base Cloudforms error'''


class CloudformsHTTPError(CloudformsError):
    '''Cloudforms - API request HTTP status error

    Provides faultCode and faultString properties.
    '''
    def __init__(self, fault_code, fault_string, *args):
        CloudformsError.__init__(self, fault_string, *args)
        # pylint: disable=invalid-name
        self.faultCode = fault_code
        self.reason = self.faultString = fault_string

    def __repr__(self):
        return '<%s(%s): %s>' % (self.__class__.__name__,
                                 self.faultCode,
                                 self.faultString)

    def __str__(self):
        return '%s(%s): %s' % (self.__class__.__name__,
                               self.faultCode,
                               self.faultString)


class CloudformsAPIError(CloudformsError):
    '''Cloudforms - API error

    Provides resultData and faultString properties.
    '''
    def __init__(self, result_data, fault_string, *args):
        CloudformsError.__init__(self, fault_string, *args)
        # pylint: disable=invalid-name
        self.resultData = result_data
        self.reason = self.faultString = fault_string

    def __repr__(self):
        return '<%s(%s): %s>' % (self.__class__.__name__,
                                 self.faultString,
                                 self.resultData)

    def __str__(self):
        return '%s(%s): %s' % (self.__class__.__name__,
                               self.faultString,
                               self.resultData)


class CloudformsBadResult(CloudformsAPIError):
    '''Cloudforms - API results error (malformed / unexcepted data)'''
