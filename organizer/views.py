from django.http.response import HttpResponse, Http404
from django.template import Context, loader
from .models import Startup, Tag
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TagForm

def startup_list(request):
    return render(request,
                  'organizer/startup_list.html',
                  {'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request,
                  'organizer/startup_detail.html',
                  {'startup': startup})

def tag_list(request):
    return render(request,
                  'organizer/tag_list.html',
                  {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request,
                  'organizer/tag_detail.html',
                  {'tag': tag})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag) 
        else:
            return render(
                request, 
                'organizer/tag_form.html',
                {'form': form})
    else:
        form = TagForm()
        return render(
            request,
            'organizer/tag_form.html',
            {'form': form})    

