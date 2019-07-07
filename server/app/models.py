from app import db

class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    registration_date = db.Column(db.DateTime())
    expiration_date = db.Column(db.DateTime())
    checked = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f"<Domain: {self.name}, checked={self.checked}, expiration_date={self.expiration_date}>"