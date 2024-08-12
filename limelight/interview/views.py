from django.shortcuts import render, get_object_or_404
from .models import Interview

# Create your views here.
def interview(request):
    interviews = Interview.objects.all()
    context = {
        'interviews': interviews,
    }
    return render(request, 'interview.html', context)

def interview_detail(request, pk):
    interview_det = get_object_or_404(Interview, pk=pk)
    context = {
        'interview_det': interview_det,
    }
    return render(request, 'interview_det.html', context)
