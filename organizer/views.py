from django.http.response import HttpResponse
from django.template import Context, loader
from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    output = template.render({'tag_list': tag_list})
    return HttpResponse(output)
