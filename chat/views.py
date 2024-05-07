from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic.list import ListView

from courses.models import Course


class CourseListView(ListView):
    model = Course

    template_name = 'chat/courses.html'


def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except:
        return HttpResponseForbidden(
            render(request, 'chat/room.html',
                   context={'exception': str("You should login first to get in")})

        )
    return render(request, 'chat/room.html', {'course': course})
