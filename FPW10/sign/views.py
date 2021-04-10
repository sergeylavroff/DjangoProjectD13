from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BasicSignupForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BasicSignupForm
    success_url = '/'

@login_required
def become_author(request):
    user = request.user
    premium_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        premium_group.user_set.add(user)
    return redirect('/')