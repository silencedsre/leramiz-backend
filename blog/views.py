from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog
from .forms import Comments
from .models import CommentModel
# Create your views here.
class BlogList(ListView):
    model = Blog
    template_name = "blog/blog.html"

class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

def comment_form(request):
    form = Comments(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        comment = form.cleaned_data.get('comment')
        comment_new = CommentModel(author=name, comment=comment)
        comment_new.save()
        print(name, " ", email, "", comment)
    context = {'form': form}
    return render(request, "blog/comment_form.html", context=context)

class CommentList(ListView):
    model = CommentModel
    template_name = "blog/comments.html"