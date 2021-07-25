from kapsoya.models import Neighbourhood
from kapsoya.forms import NewNeighbourHood, SignupForm, UserProfileForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    all_hoods = Neighbourhood.objects.all()

    return render(request,'index.html',{"all_hoods":all_hoods})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
  
    return render(request, 'index.html',{'all_hoods':all_hoods})

@login_required(login_url='/accounts/login/')
def create_neighbourhood(request):
    if request.method == 'POST':
        form = NewNeighbourHood(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = request.user
            neighbourhood.save()
            messages.success(request, 'A new Neighbourhood has been created! Join it and become a member')
            return redirect('index')
    else:
        form = NewNeighbourHood()
    return render(request, 'new_neighbourhood.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def leave_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    messages.success(
        request, 'Success! You have succesfully exited this Neighbourhood ')
    return redirect('index')
