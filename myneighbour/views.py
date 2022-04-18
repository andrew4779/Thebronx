from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse

from myneighbour.models import Business, NeighbourHood, Post, Profile
from .forms import ProfileUpdateForm,UserUpdateForm,NeighbourHoodForm,PostForm,BusinessForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime as dt
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        
    context = {
        'u_form' : u_form,
        'p_form' : p_form,

    }
    return render(request,'profile.html',context)