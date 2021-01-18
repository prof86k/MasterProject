from django.urls import path

# ================ imports from current app
from . import views as web_views

# ================== app's name ================

app_name = "master"
urlpatterns = [
    path('',web_views.index,name="home"),
    # ====================== programming questions ,answers and comments =====================
    path('master/languages',web_views.languages,name='programming_languages'),
    path('master/add_language',web_views.add_language,name='add_language'),
    path('master/language/<int:language_id>/questions',web_views.languages_questions,name='language_questions'),
    path('master/question/<int:question_id>answers',web_views.question_answers,name='question_answers'),
    path('ask-question/',web_views.ask_question,name='ask_question'),
    path('add/response/to/<int:question_id>',web_views.add_response,name='add_response'),
    path('add/comments/<int:solution_id>',web_views.add_comment,name="add_comment"),
    path('all/comments/<int:solution_id>',web_views.all_comments,name="all_comments"),
]
