import os

mysql_config = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'dbname':   os.environ.get('DB_NAME'),
}


def alchemy_uri():
    return 'mysql+pymysql://%s:%s@%s:13306/%s?charset=utf8' % (mysql_config['user'], mysql_config['password'], mysql_config['host'], mysql_config['dbname'])