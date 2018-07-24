from django.views import View
from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from messenger.models import *
from messenger.forms import *
import ipdb
class message_view(LoginRequiredMixin,ListView):
    # login_url = '/login/'
    queryset = User.objects.all()
    template_name = "sarikamsghtml.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super(message_view, self).get_context_data(**kwargs)
        context['userid'] = self.request.user.id
        # name=User.objects.get(id=self.kwargs['pk'])
        # context['username']=name.username
        return context

class chat_view(LoginRequiredMixin,CreateView):
    # login_url = '/login/'
    queryset = User.objects.all()
    form_class=MessageForm
    template_name = "chathtml.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super(chat_view, self).get_context_data(**kwargs)
        context['object_list']=User.objects.all()
        context['from'] = self.request.user.id
        context['userid'] = self.request.user.id
        context['myname']=self.request.user
        unique=User.objects.get(id=self.kwargs['pk'])
        context['frdname']=unique.username
        context['to'] = self.kwargs['pk']
        context['chat']=Message.objects.filter(fromuser__in=[self.request.user.id,self.kwargs['pk']])
        return context
    def post(self, request, *args, **kwargs):
        username = self.request.user.get_username()
        data= MessageForm(request.POST, request.FILES, initial={'user': request.user})
        if data.is_valid():
            credit_card = data.save(commit=False)
            credit_card.fromuser=self.request.user.id
            credit_card.touser=self.kwargs['pk']
            credit_card.save()
            return redirect('messenger:chat',pk=self.kwargs['pk'])
        else:
            return redirect('messenger:loginpage')