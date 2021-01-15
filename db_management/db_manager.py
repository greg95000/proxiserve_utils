from db_management.base import Base
from db_management.singleton import SingletonMeta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists

from models.users import User
from models.consumptions import Consumption
from models.apartments import Apartment

AVAILABLE_DATABASES = ('postgresql', 'mysql', 'sqlite')


class DatabaseManager(metaclass=SingletonMeta):

    def __init__(self):
        self.session = None

    def connect_to_database(self,
                            database_driver,
                            database_url,
                            user=None,
                            password=None,
                            database_name=None,
                            database_port=None,
                            encoding='utf-8',
                            verbose=False):
        """Connect to database and init it if it doesn't exist

        Args:
            database_driver (string): The database driver used for the connection ('postgresql', 'mysql', 'sqlite')
            database_url (string): The database url (use the file path for sqlite)
            user (string, optional): The username for the database. Defaults to None.
            password (string, optional): The password to connect on the database. Defaults to None.
            database_name (string, optional): The database name. Defaults to None.
            database_port (int, optional): The database port. Defaults to None.
            encoding (string, optional): The encoding used in the database. Defaults to 'utf-8'.
            verbose (bool, optional): Put the database in verbose mode to debug. Defaults to False.

        Raises:
            Exception: When the driver is not supported by the util
        """
        if database_driver not in AVAILABLE_DATABASES:
            raise Exception('Database driver not supported')
        url = self._construct_url(
            database_driver,
            database_url,
            user,
            password,
            database_name,
            database_port
        )
        engine = create_engine(url, encoding=encoding, echo=verbose)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self._init_database(url, engine)

    def _construct_url(
                        self,
                        database_driver,
                        database_url,
                        user=None,
                        password=None,
                        database_name=None,
                        database_port=None
                    ):
        """Construct the database url

        Args:
            database_driver (string): The database driver used for the connection ('postgresql', 'mysql', 'sqlite')
            database_url (string): The database url (use the file path for sqlite)
            user (string, optional): The username for the database. Defaults to None.
            password (string, optional): The password to connect on the database. Defaults to None.
            database_name (string, optional): The database name. Defaults to None.
            database_port (int, optional): The database port. Defaults to None.


        Returns:
            string: The url
        """
        if database_driver == "sqlite":
            url = "{db_driver}:///{db_url}".format(
                    db_driver=database_driver,
                    db_url=database_url
                )
        else:
            if database_port:
                url = "{db_driver}://{user}:{password}@{db_url}:{port}".format(
                    db_driver=database_driver,
                    user=user,
                    password=password,
                    db_url=database_url,
                    port=database_port
                )
            else:
                url = "{db_driver}://{user}:{password}@{db_url}".format(
                    db_driver=database_driver,
                    user=user,
                    password=password,
                    db_url=database_url
                )
            if database_name:
                url = "{url}/{db_name}".format(url=url, db_name=database_name)
        return url

    def _init_database(self, database_url, engine):
        """Init the database if it doesn't exist

        Args:
            database_url (string): The database url
        """
        if not database_exists(database_url):
            Base.metadata.create_all(engine)
