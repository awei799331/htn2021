from Cachexplorer.transactions import add_user_txn, get_userid_txn, update_task_txn, update_cumulative_txn
from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import registry
registry.register("cockroachdb", "cockroachdb.sqlalchemy.dialect",
                  "CockroachDBDialect")

class cachexplorer:
    """
    Wraps the database connection. The class methods wrap database transactions.
    """

    def __init__(self, conn_string):
        """
        Establish a connection to the database, creating Engine and Sessionmaker objects.
        Arguments:
            conn_string {String} -- CockroachDB connection string.
        """
        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def add_user(self, new_username, new_password):
        return run_transaction(
            self.sessionmaker, lambda session: add_user_txn(
                session, new_username, new_password))

    def get_userid(self, username):
        return run_transaction(
            self.sessionmaker,
            lambda session: get_userid_txn(session, username))


    def update_task(self,  user_id, new_startpoint, new_length, new_target):
        return run_transaction(
            self.sessionmaker,
            lambda session: end_ride_txn(session, user_id, new_startpoint, new_length, new_target))

    def update_cumulative(self, user_id, new_goldstar, new_distance):
        return run_transaction(
            self.sessionmaker,
            lambda session: update_cumulative_txn(session, user_id, new_goldstar, new_distance))
