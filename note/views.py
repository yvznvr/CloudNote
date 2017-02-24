from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from .models import NoteBook
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm, CreateUserForm, NoteForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .serializers import NoteSerializer
from django.http import Http404


class MainPage(TemplateView):
    template_name = 'index.html'


class NoteList(LoginRequiredMixin, ListView):
     model = NoteBook
     template_name = 'notebook_list.html'
     login_url = 'login'

     def get_queryset(self):
         return self.model.objects.filter(linked_user=self.request.user)


class NoteCreate(CreateView):
    model = NoteBook
    form_class = NoteForm
    template_name = 'note_create.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.linked_user = self.request.user
        return super().form_valid(form)



class NoteUpdate(UpdateView):
    model = NoteBook
    form_class = NoteForm
    template_name = 'note_create.html'
    success_url = reverse_lazy('note_list')


    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.linked_user == self.request.user:
            raise Http404
        return  obj



class NoteDelete(DeleteView):
    model = NoteBook
    success_url = reverse_lazy('note_list')
    template_name = 'note_delete.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.linked_user == self.request.user:
            raise Http404
        return obj


class UserLogin(FormView):
    form_class = UserForm
    success_url = '/notlar'
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            return redirect('/notlar')
        return super().render_to_response(context, **response_kwargs)

class UserLogout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


class UserCreate(View):
    form_class = CreateUserForm
    success_url = '/notlar'
    template_name = 'createuser.html'

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/notlar')
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/notlar')
        return render(request, self.template_name, {'form': form})



#Views for Rest Api

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.linked_user == self.request.user:
            raise Http404
        return  obj

    def get_queryset(self):
        return  NoteBook.objects.filter(linked_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(linked_user=self.request.user)
