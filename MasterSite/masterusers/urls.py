from django.urls import path

# ================ imports from current app
from . import views as user_web_views

# ================== app's name ================

app_name = "masteruser"
urlpatterns = [
    # =========================== profile =====================
    path('master/user/profile',user_web_views.profile,name="profile"),

    # =================== subjects learns =============================
    path('master/user/subjects/<int:subject_id>/learns',user_web_views.topics_and_lessions,name='topics_lessions'),
    path('master/user/subject/<int:topic_id>/topic/add',user_web_views.add_lession,name="add_new_lession"),
    path('master/user/subjects/lession-<int:lession_id>/details',user_web_views.lession_details,name="lession_details"),
    path('master/user/subject/lession-<int:lession_id>/edit',user_web_views.edit_learns,name="edit_lession"),
    path('user/topic/<int:topic_id>/delete',user_web_views.delete_topic,name='delete_topic'),
    path('user/lession/<int:lession_id>/remove',user_web_views.delete_lession,name="delete_lession"),

]
