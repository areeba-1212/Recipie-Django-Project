from faker import Faker
from .models import *
import random

fake = Faker()

def seed_db(n=10) -> None:
    for i in range(0, n):
        # Get random department
        departments = Department.objects.all()
        random_dept = random.choice(departments)
        
        # Generate student ID
        student_id = f'STU-0{random.randint(100,999)}'
        
        # Create StudentID first
        student_id_obj = StudentID.objects.create(studentID=student_id)  # Note: matches model field name
        
        # Create Student
        Student.objects.create(
            department=random_dept,
            student_id=student_id_obj,  # Matches OneToOneField name
            student_name=fake.name(),
            student_email=fake.email(),
            student_age=random.randint(20, 30),
            student_address=fake.address()
        )