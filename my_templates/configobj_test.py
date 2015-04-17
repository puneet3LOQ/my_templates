
from configobj import ConfigObj

'''
Writing a config.
'''
conf = ConfigObj('./test.ini')

#Section1-Database config
database = {}
database['dbname'] = 'master.db'
database['tasktable'] = 'tasks'
database['taskcols'] = ['name', 'id', 'config', 'created', 
                        'lastsuccess', 'lastfail', 'onsuccess', 
                        'onfail', 'precedents', 'loopnumber']

conf['database'] = database

conf.write()

'''
Reading a config.
'''
config = ConfigObj('./test.ini')
print config['database']
print config['database']['dbname']
print config['database']['taskcols'][3]