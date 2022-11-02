import time
import pysolr
import redis
import psycopg2
import requests
import datetime
from flask import Flask

app = Flask(__name__)
conn = psycopg2.connect('postgresql://ckan:ckan@db/ckan')
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    result = {'db': ping_db(), 'redis': ping_redis(), 'solr': ping_solr()}
    return result

def ping_db():
    with conn.cursor() as cur:
        cur.execute('select NOW()')
        result = cur.fetchall()
        conn.commit()
    return result[0][0].strftime('%Y%m%dT%H%M%S')

def ping_redis():
    count = get_hit_count()
    return count

def ping_solr():
    # pong = solr.ping()
    # return 'Health check: {}.\n'.format(pong)
    r = requests.get('http://solr:8983/solr')
    return r.status_code
