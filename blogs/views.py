from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm, PostCreationForm
from .models import Post


def index(request):
    post_pages = Post.objects.all()
    paginator = Paginator(post_pages, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    user_posts_list = Post.objects.filter(author=request.user)
    return render(request, 'registration/profile.html', {'user_posts_list': user_posts_list})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)