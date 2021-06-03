from django import forms
from .models import Tag, Startup, NewsLink  
from django.core.exceptions import ValidationError

class TagForm(CleanSlugMixin, forms.ModelForm):
    # Alongside inheriting from forms.ModelForm instead of forms.Form
    # This was done so any changes in the Tag model would automatically
    # reflect on this corresponding form
    class Meta:
        model = Tag
        fields = '__all__'

    def save(self):
        new_tag = Tag.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'])
        return new_tag

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class StartupForm(CleanSlugMixin, forms.ModelForm):
    class Meta:
	model = Startup
	fields = '__all__'

class NewsLinkForm(forms.ModelForm):
    class Meta:
	model = NewsLink
	fields = '__all__'

class CleanSlugMixin:
    def clean_slug(self):
	new_slug = self.cleaned_data['slug'].lower()
	if new_slug == 'create':
	    raise ValidationError('Slug may not be "create"')
        return new_slug

