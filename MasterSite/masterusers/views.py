from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

# Create your views here.
from .models import (
                    # ========= user learns models ===============
                    Subject,
                    Topic,
                    Learn,
                    )
from .forms import (
                    SubjectForm,
                    TopicForm,
                    LearnForm,
                    )

def profile(request):
    """ user profile page is rendered here"""
    subjects = Subject.objects.order_by('-date_added').all()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid() and form is not None:
            form.save()
            return redirect("masteruser:profile")
    else:
        form = SubjectForm()

    context = {
        "subjects":subjects,
        "form":form,
    }
    return render(request,'masterusers/profile.html',context)


def topics_and_lessions(request,subject_id):
    """Go to the particular subject requested for details"""
    subject_details = get_object_or_404(Subject,pk=subject_id)
    topics = subject_details.topic_set.all()
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid() and form is not None:
            new_topic = form.save(commit=False)
            new_topic.subject = subject_details
            new_topic.save()
            return redirect('masteruser:topics_lessions',subject_details.id)
    else:
        form = TopicForm()

    context = {
        "topics":topics,
        "subject":subject_details,
        'form':form,
    }
    return render(request,'masterusers/topic_and_lessions.html',context)


def add_lession(request,topic_id):
    """ add lessions learned to a topic learned about"""
    topics = get_object_or_404(Topic,pk=topic_id)
    subject = topics.subject.id
    if request.method == "POST":
        form = LearnForm(request.POST)
        if form.is_valid() and form is not None:
            new_lession = form.save(commit=False)
            new_lession.topic = topics
            new_lession.save()
            return redirect("masteruser:topics_lessions",subject)
    else:
        form = LearnForm()
    context = {
        "topic":topics,
        "form":form,
        "subject":subject,
    }
    return render(request,"masterusers/add_new_lession.html",context)


def lession_details(request,lession_id):
    """ get the detail information about the lession"""
    lession = get_object_or_404(Learn,pk=lession_id)
    context = {
        'lession':lession,
        'topic_lession':lession.topic,
    }
    return render(request,'masterusers/lession_details.html',context)


def edit_learns(request,lession_id):
    """ edit lessions learn to add or remove text"""
    lession_learned = get_object_or_404(klass=Learn,pk=lession_id)
    if request.method == "POST":
        form = LearnForm(instance=lession_learned,data=request.POST)
        if form.is_valid() and form is not None:
            form.save()
            return redirect("masteruser:topics_lessions",lession_learned.topic.subject.id)
    else:
        form = LearnForm(instance=lession_learned)
    context = {
        "form":form,
        'lession':lession_learned,
    }
    return render(request,"masterusers/edit_lession.html",context)

def delete_topic(request,topic_id):
    """ delete item from data base"""
    topic = get_object_or_404(Topic,pk=topic_id)
    topic.delete()
    return redirect("masteruser:topics_lessions",topic.subject.id)

def delete_lession(request,lession_id):
    """ delete item from data base"""
    lession = get_object_or_404(Learn,pk=lession_id)
    lession.delete()
    return redirect("masterusers:topics_lessions",lession.topic.subject.id)