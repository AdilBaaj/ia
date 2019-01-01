#########################
# Database configuration
#########################

postgresql_conf = {
    'user': 'postgres',
    'database': 'ia',
    'host': 'postgres',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s@%(host)s:%(port)s/%(database)s' % postgresql_conf
SQLALCHEMY_TRACK_MODIFICATIONS = True
