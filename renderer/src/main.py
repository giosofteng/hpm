from amqp import AMQP
from db import DB


db = DB()
amqp = AMQP(db)


if __name__ == '__main__':
    amqp.start_storing_data()
