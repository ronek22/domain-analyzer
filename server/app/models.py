from app import db

def dump_datetime(value):
    if value is None:
        return None
    # return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]
    return value.timestamp()

class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    registration_date = db.Column(db.DateTime())
    expiration_date = db.Column(db.DateTime())
    checked = db.Column(db.Boolean(), nullable=False, default=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'registration_date': dump_datetime(self.registration_date),
            'expiration_date': dump_datetime(self.expiration_date),
            'checked': self.checked
        }

    def __repr__(self):
        return f"<Domain: {self.name}, checked={self.checked}, expiration_date={self.expiration_date}>"