from django.test import TestCase
from courses.models import Subject, Course, Module
from django.contrib.auth.models import User


class ModelMixin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="123",
        )

        self.subject = Subject.objects.create(
            title="test-subject",
            slug="test-subject",
        )
        self.courses = Course.objects.create(
            owner=User.objects.get(id=self.user.id),
            subject=self.subject,
            title="test-course",
            slug="test-course",
        )

    def create_new_modules(self, count, order_number=None):
        for _ in range(count):
            Module.objects.create(
                course=self.courses,
                title="test-module",
                order=order_number,
            )
        return Module.objects.all()
