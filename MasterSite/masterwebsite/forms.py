from django import forms
# ================ user learns models import ===programming questions models import =======
from .models import (
                    ProgrammingLanguage,
                    ProgramSolutions,
                    Comment,
                    Question,
                    )

# =================== Programming questions, answers and comments forms ============= 

class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['language_name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields=['programming_language','question_text']


class ProgramSolutionForm(forms.ModelForm):
    class Meta:
        model = ProgramSolutions
        fields =['solution_code']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
