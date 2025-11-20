from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import SignUpForm, PostCreationForm, CommentCreationForm
from .models import Post, Like, Comment, CustomUser


def index(request):
    post_pages = Post.objects.all()
    paginator = Paginator(post_pages, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    post_pages = Post.objects.filter(author=request.user)
    paginator = Paginator(post_pages, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'registration/profile.html', {'page_obj': page_obj})


@login_required
def like(request, pk):
    post = get_object_or_404(Post, id=pk)

    if Like.objects.filter(user=request.user, post=post).exists():
        Like.objects.filter(user=request.user, post=post).delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect('index')


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'avatar', 'bio']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreationForm()
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreationForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('profile')


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreationForm

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, id=post_id)
        fields.post = post
        fields.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})