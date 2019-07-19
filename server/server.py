from app import app, db, celery
from app.models import Domain

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Domain': Domain}

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0")
