import sqlalchemy


class DB:
    def __init__(self):
        self.engine = sqlalchemy.create_engine('sqlite:///../db.sqlite')
        self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()

        self.images_table = sqlalchemy.Table(
            'images',
            self.metadata,
            sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
            sqlalchemy.Column('url', sqlalchemy.Text(), nullable=False)
        )
        self.metadata.create_all(self.engine)

        self.index = 1

    def put(self, url):
        query = sqlalchemy.insert(self.images_table).values(id=self.index, url=url)
        self.connection.execute(query)

        self.index += 1

    def get(self):
        return self.connection.execute(self.images_table.select()).fetchall()
