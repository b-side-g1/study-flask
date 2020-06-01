import os

mysql_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
	'user': os.environ.get('DB_USER', 'root'),
	'password': os.environ.get('DB_PASSWORD', ''),
	'dbname':   os.environ.get('DB_NAME', 'my_flask'),
}

def alchemy_uri():
    return 'mysql://%s:%s@%s/%s?charset=utf8' % (mysql_config['user'],mysql_config['password'],mysql_config['host'],mysql_config['dbname'])