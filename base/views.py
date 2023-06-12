from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Room, Topic
from django.http import JsonResponse
# Create your views here.

@login_required
def home(request):
    #  make filter rooms with topic
    topic_filter = request.GET.get('topic', '')
    current_page = request.GET.get('p', '')

    if not current_page:
        current_page = 1

    try:
        current_page = int(current_page)
        if current_page <= 0:
            current_page = 1
    except:
        current_page = 1

    # variable for paginator
    number_rooms_in_page = 2

    if topic_filter:
        topic_filter = topic_filter.strip()
        topics = Topic.objects.filter(name__icontains=topic_filter).all()
        rooms_list = []
        for topic in topics:
            rooms_ = Room.objects.filter(topic = topic).all()
            rooms_list.extend(rooms_)

        room_paginator = Paginator(rooms_list, number_rooms_in_page)
    else:
        rooms_ = Room.objects.all()
        room_paginator = Paginator(rooms_, number_rooms_in_page)

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

    rooms_in_page = room_paginator.get_page(current_page)

    current_page_neighbours = list(room_paginator.get_elided_page_range(current_page, on_each_side=1))

    context = {
        "number_of_all_rooms": Room.objects.all().count(),
        "current_user": request.user,
        "rooms_page": rooms_in_page,
        "most_topic_rooms": most_topic_rooms,
        "paginator_obj": room_paginator,
        "current_page": current_page,
        "topic_filter": topic_filter,
        "current_page_neighbours": current_page_neighbours,
    }
    return render(request, "base\home.html", context)

def all_topics_view(request):
    topics_per_page = 2
    current_page_number = request.GET.get('p', '')
    try:
        current_page_number = int(current_page_number)
    except:
        current_page_number = 1

    query_string = request.GET.get('topic', '')
    print(query_string)
    if query_string:
        topics_ = Topic.objects.filter(name__icontains=query_string).all()
    else:
        topics_ = Topic.objects.all()

    topics = Paginator(topics_, topics_per_page)
    topics_in_page = topics.get_page(current_page_number)
    current_page_neighbours = list(topics.get_elided_page_range(current_page_number, on_each_side=1))
    context = {
        "paginator_obj": topics,
        "topics": topics_in_page,
        "current_page_number": current_page_number,
        "query_string": query_string,
        "current_page_neighbours": current_page_neighbours,
    }
    return render(request, "base/topics.html", context)