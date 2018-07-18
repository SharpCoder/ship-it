import requests

class Api:

    ''' invoke a rest endpoint
    
    kwargs: 
        opertion = {
            method: 'String',
            url: 'String',
            headers: {
                key1: "value1",
                key2: "value2"
            }
        }
    
    '''
    def invoke(self, operation):
        return requests.request(operation["method"], operation["url"], headers=operation["headers"])