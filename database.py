import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']



engine = create_engine(db_connection_string, connect_args={
                          "ssl": {
                              "ca": "/home/runner/workspace/ca.pem",
                          }
                      },)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from job_lists"))

    jobs = []

    for row in result.all():
        jobs.append(row._asdict())

    return jobs