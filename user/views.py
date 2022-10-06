from django.shortcuts import render
from user.models import User

# Create your views here.
def profile(request):
    new_user = User.objects.all()
    context = {'users':new_user}
    return render(request, 'user/profile.html', context)

