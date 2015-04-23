#!/usr/bin/python
#/home/triloq/git/my_templates/my_templates/couchbase_connection.py


from couchbase import Couchbase

class CBClient():
    '''
    A wrapper class to handle connections to couchbase. It depends on 
    couchbase API
    '''
    def __init__(self, bucket, server, pwd):
        '''
        Intentionally not handling connection errors here. We expect them
        to be handled by the calling code.
        '''
        self.bucket = bucket,
        self.server = server,
        self.pwd = pwd,
        self.client = Couchbase.connect(
            bucket=self.bucket, host=self.server, password=self.pwd)

    def add(self, key, val):
        if key and type(key) == str and key <> '':
            self.client.add(key, val)

    def delete(self, key):
        if key and type(key) == str and key <> '':
            self.client.delete(key)
