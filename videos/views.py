from django.shortcuts import render, get_object_or_404
from .models import Video
from catalog.models import Subject, GradeLevel

# Create your views here.

def video_library(request):
    subject_id = request.GET.get('subject')
    grade_id = request.GET.get('grade')
    videos = Video.objects.all()
    if subject_id:
        videos = videos.filter(subject_id=subject_id)
    if grade_id:
        videos = videos.filter(grade_level_id=grade_id)
    subjects = Subject.objects.all()
    grades = GradeLevel.objects.all()
    return render(request, 'videos/library.html', {
        'videos': videos,
        'subjects': subjects,
        'grades': grades,
        'selected_subject': subject_id,
        'selected_grade': grade_id,
    })

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'videos/detail.html', {'video': video})
