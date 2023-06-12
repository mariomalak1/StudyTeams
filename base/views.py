from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Room, Topic
# Create your views here.

@login_required
def home(request):
    #  make filter rooms with topic
    topic_filter = request.GET.get('topic', '')
    page = request.GET.get('p', '')

    number_rooms_in_page = 5

    if topic_filter:
        topic_filter = topic_filter.strip()
        topics = Topic.objects.filter(name__icontains=topic_filter).all()
        rooms_list = []
        for topic in topics:
            rooms_ = Room.objects.filter(topic = topic).all()
            rooms_list.extend(rooms_)

        rooms_paginator = Paginator(rooms_list, number_rooms_in_page)
        rooms_count = len(rooms_list)
    else:
        rooms_ = Room.objects.all()
        rooms_paginator = Paginator(rooms_, number_rooms_in_page)
        rooms_count = rooms_.count()

    rooms = rooms_paginator.get_page(page)

    # topics with more rooms in it
    most_topic_rooms_query = Topic.objects.annotate(total_rooms = Count('room')).order_by('-total_rooms', '-name')
    most_topic_rooms = []
    counter = 0
    for topic in most_topic_rooms_query:
        if counter >= 5:
            break
        most_topic_rooms.append({topic: topic.room_set.count()})
        counter += 1
    # end of it

    context = {
        "current_user": request.user,
        "rooms": rooms,
        "rooms_count": rooms_count,
        "most_topic_rooms": most_topic_rooms,
        "page": page,
    }    
    return render(request, "base\home.html", context)

def all_topics_view(request):
    page = request.GET.get('p', '')
    topics = Paginator(Topic.objects.all(), 5)

    context = {
        "topics": topics,
        "page": page,
    }
    return render(request, "base/topics.html", context)