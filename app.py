from psycopg2 import connect
from urllib.parse import urlparse

postgres_url = "postgresql://localhost:5432/python"

url = urlparse(postgres_url)

conn = connect(
    host=url.hostname,
    port=url.port,
    user=url.username,
    password=url.password,
    database=url.path[1:]
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE cpus (
        id serial primary key,
        name varchar(255),
        cores int,
        threads int,
        prices decimal
    );
""")

conn.commit()
