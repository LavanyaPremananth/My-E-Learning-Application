# Import necessary modules
from django import forms
from . import models

# Define form for Quiz model
class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

# Define form for Question model
class QuestionForm(forms.ModelForm):
    class Media:
        css = {'all': ('courses/css/order.css',)}  # CSS files to include
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',  # JavaScript file for sorting
            'courses/js/order.js'  # Custom JavaScript file
        )

# Define form for TrueFalseQuestion model, inherits from QuestionForm
class TrueFalseQuestionForm(QuestionForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
        ]

# Define form for MultipleChoiceQuestion model, inherits from QuestionForm
class MultipleChoiceQuestionForm(QuestionForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers',
        ]

# Define form for Answer model
class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct',
        ]

# Define formset for Answer model
AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,
)

# Define inline formset for Answer model
AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,
    models.Answer,
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1,
)
