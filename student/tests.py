from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Test",
            last_name="Student",
            email="test@student.com",
            dob="2000-01-01",
        )

    def test_student_creation(self):
        """Test that a student instance is created correctly."""
        student = self.student
        self.assertEqual(student.first_name, "Test")
        self.assertEqual(student.last_name, "Student")
        self.assertEqual(student.email, "test@student.com")
        self.assertEqual(str(student.dob), "2000-01-01")

    def test_student_string_representation(self):
        """Test the string representation of the student model."""
        self.assertEqual(str(self.student), f"{self.student.first_name} {self.student.last_name}")
