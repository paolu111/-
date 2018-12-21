from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as S


class SQLALchemy(S):
    @contextmanager
    def auto_commit(self):
        yield
        try:
            self.session.add()
            self.session.commit()
        except:
            self.session.rollback()





