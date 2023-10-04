from django import forms

from mainapp import models

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    description = forms.Textarea()
    create_date = forms.DateTimeField()

    class Meta:
        model = models.Books
        fields = ["title","description",]