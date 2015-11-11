from sqlalchemy import create_engine #@UnresolvedImport
from sqlalchemy import Column #@UnresolvedImport
from sqlalchemy import String #@UnresolvedImport
from sqlalchemy.ext.declarative import declarative_base #@UnresolvedImport
from sqlalchemy.orm import scoped_session #@UnresolvedImport
from sqlalchemy.orm import sessionmaker #@UnresolvedImport
from zope.sqlalchemy import ZopeTransactionExtension #@UnresolvedImport
import transaction #@UnresolvedImport

import pyco
import pyco.log
import logging

# create logger
log = pyco.log.getLogger("indb")

DEVICE_REPO = 'devices.sqlite'

Base = declarative_base()


class NetworkNode(Base):
    __tablename__ = 'indb'
    
    name = Column(String, primary_key=True)
    type = Column(String)
    username = Column(String)
    password = Column(String)

    def __init__(self, name, type, username, password):
        self.name = name
        self.type = type
        self.username = username
        self.password = password


class Database:

    def __init__(self):
        print('creating engine for [%s]' % self.db_url())
        self.engine = create_engine(self.db_url(), echo=False)
    
        self.session = scoped_session(sessionmaker(
                                extension=ZopeTransactionExtension(), bind=self.engine))
    
        
        #self.createDB('sqlite://%s' % DEVICE_REPO)
        self.db_exists()

    def db_exists(self):
        import os.path
        if hasattr(pyco, 'pyco_home'):
            db_file = '%s/%s' % (pyco.pyco_home, DEVICE_REPO)
        else:
            db_file = '/tmp/%s' % DEVICE_REPO
        try:
            if not os.path.isfile(db_file):
                log.debug('creating cache [%s] ...' % db_file)
                self.createDB('sqlite://%s' % db_file)
        except Exception as e:
            log.error('fatal error: %s' % e)


 
    def initialize_sql(self):
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)
    
    
    def createDB(self, url):
        print('db endpoint: [%s]' % url)
        self.initialize_sql()
        
    def db_url(self):
        import os.path
        if hasattr(pyco, 'pyco_home'):
            db_url = 'sqlite:///%s/%s' % (pyco.pyco_home, DEVICE_REPO)
        else:
            db_url = 'sqlite:////tmp/%s' % DEVICE_REPO
        return db_url
    
    def create(self, name, type, username, password):
        #transaction.begin()
        
        node = NetworkNode(name, type, username, password)
        self.session.add(node)
        #transaction.commit()

    def delete(self, name):
        #transaction.begin()
        
        node = NetworkNode(name, type)
        node = self.session.query(NetworkNode).get((name))
        if(node):
            self.session.delete(node)
        #transaction.commit()
        
    def getall(self):
        return self.session.query(NetworkNode)
        