from sqlalchemy import URL

DATABASE = URL.create(
    "postgresql+psycopg2",
    username="db_username",
    password="db_password",
    host="localhost",
    database="ptmk",
    port='5432',
)
