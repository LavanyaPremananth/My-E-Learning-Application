# Import necessary modules
from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from . import forms, models

# View for listing courses
def course_list(request):
    courses = models.Course.objects.all()
    email = 'questions@learning_site.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})

# View for course detail
def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()), key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {'course': course, 'steps': steps})

# View for text detail
def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

# View for quiz detail
def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/quiz_detail.html', {'step': step})

# View for creating a quiz
@login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(models.Course, pk=course_pk)
    form = forms.QuizForm()

    if request.method == 'POST':
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.add_message(request, messages.SUCCESS, "Quiz Added!")
            return HttpResponseRedirect(quiz.get_absolute_url())

    return render(request, 'courses/quiz_form.html', {'form': form, 'course': course})

# View for editing a quiz
@login_required
def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course_id=course_pk)
    form = forms.QuizForm(instance=quiz)

    if request.method == 'POST':
        form = forms.QuizForm(instance=quiz, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data['title']))
            return HttpResponseRedirect(quiz.get_absolute_url())

    return render(request, 'courses/quiz_form.html', {'form': form, 'course': quiz.course})

# View for creating a question
@login_required
def create_question(request, quiz_pk, question_type):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
    form_class = forms.TrueFalseQuestionForm if question_type == 'tf' else forms.MultipleChoiceQuestionForm
    form = form_class()
    answer_forms = forms.AnswerInlineFormSet(queryset=models.Answer.objects.none())

    if request.method == 'POST':
        form = form_class(request.POST)
        answer_forms = forms.AnswerInlineFormSet(request.POST, queryset=models.Answer.objects.none())

        if form.is_valid() and answer_forms.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()
            messages.success(request, "Added Question")
            return HttpResponseRedirect(quiz.get_absolute_url())

    return render(request, 'courses/question_form.html', {'form': form, 'quiz': quiz, 'formset': answer_forms})

# View for editing a question
@login_required
def edit_question(request, quiz_pk, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk, quiz_id=quiz_pk)
    form_class = forms.TrueFalseQuestionForm if isinstance(question, models.TrueFalseQuestion) else forms.MultipleChoiceQuestionForm
    form = form_class(instance=question)
    answer_forms = forms.AnswerInlineFormSet(queryset=form.instance.answer_set.all())

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        answer_forms = forms.AnswerInlineFormSet(request.POST, queryset=form.instance.answer_set.all())

        if form.is_valid() and answer_forms.is_valid():
            form.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()

            for answer in answer_forms.deleted_objects:
                answer.delete()
            messages.success(request, "Updated Question")
            return HttpResponseRedirect(question.quiz.get_absolute_url())

    return render(request, 'courses/question_form.html', {'form': form, 'quiz': question.quiz, 'formset': answer_forms})

# View for answering a question
@login_required
def answer_form(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk)
    formset = forms.AnswerFormSet(queryset=question.answer_set.all())

    if request.method == 'POST':
        formset = forms.AnswerFormSet(request.POST, queryset=question.answer_set.all())
        if formset.is_valid():
            answers = formset.save(commit=False)

            for answer in answers:
                answer.question = question
                answer.save()
            messages.success(request, "Added Answers")
            return HttpResponseRedirect(question.quiz.get_absolute_url())

    return render(request, 'courses/answer_form.html', {'formset': formset, 'question': question})
