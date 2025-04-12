from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string for SQL Server
DATABASE_URL = "mssql+pyodbc://localhost/DMDD_Group10?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
