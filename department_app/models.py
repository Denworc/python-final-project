from department_app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department {}>'.format(self.name)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    date_of_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return self.name
