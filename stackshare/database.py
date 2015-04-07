import uuid
import logging
from functools import wraps
import sqlalchemy
from stackshare.settings import DATABASE_URL
from sqlalchemy import  Boolean, Table, Column, Integer, String, TIMESTAMP,Text,MetaData, text


LOG = logging.getLogger(__name__)


if DATABASE_URL.startswith('mysql'):
    ENGINE = sqlalchemy.create_engine(DATABASE_URL,
        pool_size=20, pool_recycle=3600, echo = False,
        encoding='utf8',  convert_unicode=True,connect_args={'charset':'utf8'})
else:
    ENGINE = sqlalchemy.create_engine(DATABASE_URL, echo = False)


METADATA = MetaData()

class Connection:
    def __init__(self, engine):
        self.engine = engine
        
    def __enter__(self):
        self.conn = self.engine.connect()  # @UndefinedVariable
        return  self.conn
        
    def __exit__(self, type, value, traceback):
        self.conn.close()
        

def ensure_schema():
    LOG.info('schema syncing ...')
    METADATA.create_all(ENGINE)
    LOG.info('schema syncing success')


def require_connection(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if (kwargs and kwargs.get('conn')!=None) or \
            (len(args) > 0 and args[-1].__class__.__name__=='Connection'):
            return func(*args,**kwargs)

        with Connection(ENGINE) as conn:
            kwargs['conn'] = conn
            return func(*args,**kwargs)
    return inner

LOG = logging.getLogger(__name__)

Service = Table('service', METADATA,
    Column('service_id', String(255), default=uuid.uuid4, primary_key=True),
    
    Column('service_name', String(255), nullable=False, unique=True),
    Column('service_title', String(255)),
    Column('service_description', Text),
    Column('service_image_url', String(1024)),
    Column('service_guide_url',String(1024)), 
    
    Column('service_type',String(255)), 
    
    Column('category_name', String(255)),
    

    Column('created_at', TIMESTAMP, nullable=False, server_default=text('0')),
    Column('updated_at', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    Column('is_deleted', Boolean, nullable=False, server_default=text('0')),

    mysql_engine='InnoDB',
    mysql_charset='utf8'
)

ServiceReason = Table('service_reason', METADATA,
    Column('service_id', String(255), primary_key=True),
    Column('service_reason_name', String(255), primary_key=True),

    Column('service_reason_count', Integer),

    Column('created_at', TIMESTAMP, nullable=False, server_default=text('0')),
    Column('updated_at', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),

    mysql_engine='InnoDB',
    mysql_charset='utf8'
)

    