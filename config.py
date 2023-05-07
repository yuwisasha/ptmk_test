from sqlalchemy import URL

DATABASE = URL.create(
    "postgresql+psycopg2",
    username="db_username",
    password="db_username_password",
    host="localhost",
    database="ptmk",  # allowed to change
    port='5432',
)
