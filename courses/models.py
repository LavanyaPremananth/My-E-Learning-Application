# Import necessary modules
from django.urls import reverse
from django.db import models

# Define Course model
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

# Define abstract Step model
class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title

# Define Text model, inherits from Step
class Text(Step):
    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('text_detail', kwargs={'course_pk': self.course_id, 'step_pk': self.id})

# Define Quiz model, inherits from Step
class Quiz(Step):
    total_questions = models.IntegerField(default=4)

    class Meta:
        verbose_name_plural = "Quizzes"

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'course_pk': self.course_id, 'step_pk': self.id})

# Define Question model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order',]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt

# Define MultipleChoiceQuestion model, inherits from Question
class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)

# Define TrueFalseQuestion model, inherits from Question
class TrueFalseQuestion(Question):
    pass

# Define Answer model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.text
