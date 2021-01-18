from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import (
                    ProgramSolutions,
                    ProgrammingLanguage,
                    Question,
                    )
from .forms import (
                    # ============== program questions,answers and commnents forms ===============
                    ProgrammingLanguageForm,
                    ProgramSolutionForm,
                    QuestionForm,
                    CommentForm,
                    )

def index(request):
    """home"""
    languages= ProgrammingLanguage.objects.order_by('-date_added').all()
    context={
        "languages":languages,
    }
    return render(request,"master/index.html",context)



# ============================= Questions Asked and their answers and comments here ===============
def ask_question(request):
    """ ask a question about a language you want it to be written in"""
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
                question_form.save()
                return redirect("master:home")     
    else:
        question_form = QuestionForm()

    context = {
        'question_form':question_form
    }
    return render(request,"master/ask_question.html",context)

def add_language(request):
    """ Add new language """
    if request.method == "POST":
        form = ProgrammingLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("master:ask_question")
    else:
        form = ProgrammingLanguageForm()
    context = {
        'form':form,
    }

    return render(request,"master/add_language.html",context)

def languages(request):
    """ all languages"""
    languages = ProgrammingLanguage.objects.all()
    context = {
        "languages":languages,
    }
    return render(request,"master/languages.html",context)

def languages_questions(request,language_id):
    """ all questions about a language """
    language = get_object_or_404(ProgrammingLanguage,pk=language_id)
    context = {
        "language":language,
    }
    return render(request,"master/language_questions.html",context)

def question_answers(request,question_id):
    """ all answers to a qustion"""
    question = get_object_or_404(Question,pk=question_id)
    context = {
        "question":question,
    }
    return render(request,'master/question_answers.html',context)


def add_response(request,question_id):
    """ add your response to a question desire"""
    question = get_object_or_404(Question,pk=question_id)
    if request.method == "POST":
        form = ProgramSolutionForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.program_question = question
            response.save()
            return redirect('master:home')
    else:
        form = ProgramSolutionForm()
    context = {
        'question':question,
        'form':form,
    }
    return render(request,'master/add_response.html',context)

# ======================= comments section =========================

def add_comment(request,solution_id):
    """add comment to the solution"""
    solution = get_object_or_404(ProgramSolutions,pk=solution_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.program_solution = solution
            new_comment.save()
            return redirect("master:home")
    else:
        form = CommentForm()
    
    context={
        'form':form,
        'solution':solution,
    }
    return render(request,'master/add_comment.html',context)

def all_comments(request,solution_id):
    """show all comments of a solution"""
    solution = get_object_or_404(ProgramSolutions,pk=solution_id)
    return render(request,'master/all_comments.html',
    context={"solution":solution,
    })
# ============================= Questions Asked and their answers and comments ends here ============