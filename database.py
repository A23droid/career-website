import sqlalchemy
from sqlalchemy import create_engine, text
import os

ca_cert_path = os.path.join(os.getcwd(), "ca.pem")  # Dynamically get the path

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
                          "ssl": {
                              "ca": ca_cert_path,
                          }
                      },)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from job_lists"))

    jobs = []

    for row in result.all():
        jobs.append(row._asdict())

    return jobs