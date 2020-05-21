# connect_test.py
from boto.connection import AWSAuthConnection

class ESConnection(AWSAuthConnection):

    def __init__(self, region, **kwargs):
        super(ESConnection, self).__init__(**kwargs)
        self._set_auth_region_name(region)
        self._set_auth_service_name("es")

    def _required_auth_capability(self):
        return ['hmac-v4']

if __name__ == "__main__":
    client = ESConnection(
            region='us-west-1',
            # Be sure to put the URL for your Elasticsearch endpoint below!
            host='https://vpc-es-test-med-v4mcj7pk5ztshryxjjskncemsu.us-west-1.es.amazonaws.com',
            is_secure=False)

    resp = client.make_request(method='GET',path='/')
    print resp.read()