from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # Meta tells Django which model should be used to create this form
    class Meta:
        model = Post
        fields = {'title', 'text',} # Fields that will be in the form