import time
import pysolr
import redis
import psycopg2
import requests
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
    return 'Hello world'

@app.route('/db')
def hello_db():
    cur = conn.cursor()
    cur.execute('select count(*),state from pg_stat_activity where datname = %s group by 2;',('ckan', ))
    rows = cur.fetchall()
    return rows

@app.route('/redis')
def hello_redis():
    count = get_hit_count()
    return 'Redis hit count: {}.\n'.format(count)

@app.route('/solr')
def hello_solr():
    # pong = solr.ping()
    # return 'Health check: {}.\n'.format(pong)
    r = requests.get('http://solr:8983/solr')
    return r.content