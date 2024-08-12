from django.shortcuts import render, get_object_or_404
from .models import Poem

# Create your views here.
def poem(request): 
    poems = Poem.objects.all()
    context = {
        'poems': poems,
    }
    return render(request, 'poem.html', context)

def poem_detail(request, pk):
    poem_det = get_object_or_404(Poem, pk=pk)
    context = {
        'poem_det': poem_det,
    }
    return render(request, 'poem_det.html', context)
