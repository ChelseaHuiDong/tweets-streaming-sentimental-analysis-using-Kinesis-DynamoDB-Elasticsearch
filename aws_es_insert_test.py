from datetime import datetime
from elasticsearch import Elasticsearch

from elasticsearch import RequestsHttpConnection
from requests_aws4auth import AWS4Auth

AWS_ACCESS_KEY = 'AKIAJEM2Z2WULFV2RZQA'
AWS_SECRET_KEY = '+aq3APqeCjpPDUbCWoQ8RTpHNL9+Bu6d8l2e02/g'
region = 'us-east-1' # For example, us-east-1
service = 'es'

awsauth = AWS4Auth(AWS_ACCESS_KEY, AWS_SECRET_KEY, region, service)

# by default we connect to localhost:9200
host = 'search-es-bigdata-project1-q7njkr4po2wl6uiyp3sqa5dinm.us-east-1.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
#host = 'vpc-bigdata-project-5wnppsjtigm6j457j7bs62x7ui.us-east-1.es.amazonaws.com'

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)


es.indices.create(index='my-index', ignore=400)

es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

es.get(index="my-index", doc_type="test-type", id=42)['_source']