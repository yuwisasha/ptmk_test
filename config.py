from sqlalchemy import URL

DATABASE = URL.create(
    "postgresql+psycopg2",
    username="sanek",
    password="panteleev",
    host="localhost",
    database="ptmk",
    port='5432',
)
