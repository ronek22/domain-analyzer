from app import app, db
from app.models import Domain

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Domain': Domain}