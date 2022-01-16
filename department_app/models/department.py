from department_app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    employees = db.relationship('Employee', cascade="all,delete", backref='department', lazy='select')

    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees is not None else []

    def get_average_salar(self):
        if self.employees:
            return sum(map(lambda employee: employee.salary, self.employees)) // len(self.employees)
        return 0

    def __repr__(self):
        return self.name
