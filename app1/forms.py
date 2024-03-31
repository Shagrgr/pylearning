from django import forms
from .models import Post
from .models import Comment
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'content']
