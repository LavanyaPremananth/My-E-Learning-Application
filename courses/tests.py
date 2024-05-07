# Import necessary modules
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Course, Step

# Test case for Course model
class CourseModelTests(TestCase):
    # Test method for course creation
    def test_course_creation(self):
        # Create a course object
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expression in Python"
        )
        now = timezone.now()
        # Assert that the course creation time is less than the current time
        self.assertLess(course.created_at, now)

# Test case for Step model
class StepModelTests(TestCase):
    # Set up method to create a course
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python"
        )
    # Test method for step creation
    def test_step_creation(self):
        # Create a step object
        step = Step.objects.create(
            title="Intro Docttest",
            description="Learn to write Docttest string",
            course=self.course
        )
        # Assert that the step is associated with the course
        self.assertIn(step, self.course.step_set.all())

# Test case for course views
class CourseViewsTests(TestCase):
    # Set up method to create courses and steps
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in Python"
        )
        self.course2 = Course.objects.create(
            title="New Course",
            description="A new course"
        )
        self.step = Step.objects.create(
            title="Introduction to Doctest",
            description="Learn to write tests in Your Doc String",
            course=self.course
        )
    # Test method for course list view
    def test_course_list_view(self):
        # Get response from course list view
        resp = self.client.get(reverse('course_list'))
        # Assert that the response status code is 200
        self.assertEqual(resp.status_code, 200)
        # Assert that the created courses are in the context
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
