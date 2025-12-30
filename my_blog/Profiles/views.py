from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

def get_profile(request):
    # Always get exactly ONE profile
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/profile.html', {
        'form': form,
        'user_profile': user_profile,
    })