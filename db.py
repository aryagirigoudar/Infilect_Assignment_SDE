'''
This module implements all Database related functions 
'''
import sys
from os import getenv
from psycopg2 import connect
from dotenv import load_dotenv
from logger import logger

load_dotenv()

class DB:
    '''
    This class represents a database connection and provides methods to interact with it.
    '''
    def __init__(self):
        '''
        Initializes the database connection.
        '''
        self.conn = connect(
            database = getenv("DATABASE_NAME"),
            host = getenv("DATABASE_HOST"),
            user = getenv("DATABASE_USER"),
            password = getenv("DATABASE_PASSWORD"),
            port = getenv("DATABASE_PORT")
        )
        if not self.conn:
            logger.info("Something with database Failed")
            sys.exit()
        logger.info("Database connection was successful")
        self.cursor = self.conn.cursor()

    def close_conn(self):
        '''
        Closes the database connection.
        '''
        self.conn.close()
        logger.info("Database connection closed")

    def commit(self):
        '''
        Commits the transaction.
        '''
        self.conn.commit()
        logger.info("Committed to database")

    def insert_(self, res, req, turn_time, result):
        '''
        Inserts records into the 'logs' table.

        Parameters:
        res (str): Response message.
        req (str): Request message.
        turn_time (str): Turnaround time.
        result (str): Resultant matrix.

        Returns:
        None
        '''
        query = '''insert into logs
                   (request, response, turn_around_time, resultant_matrix) 
                   values (%s, %s, %s, %s)'''
        self.cursor.execute(query, (res, req, turn_time, result))
        self.commit()
        logger.info("Inserted records")

    def print_records(self):
        '''
        Prints all records from the 'logs' table.
        '''
        self.cursor.execute('select * from logs')
        res = self.cursor.fetchall()
        print(res)

    def delete_all(self):
        '''
        Deletes all records from the 'logs' table.
        '''
        query = 'delete from logs'
        self.cursor.execute(query)
        self.commit()
        logger.info("Deleted all records")
