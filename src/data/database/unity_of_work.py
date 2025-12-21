from sqlalchemy.orm import Session

from src.data.database.db import SessionLocal

class UnityOfWork:
    def __init__(self):
        self.session: Session | None = None

    def __enter__(self) -> "UnityOfWork": 
        self.session = SessionLocal()
        return self
    
    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        

        self.session.close()