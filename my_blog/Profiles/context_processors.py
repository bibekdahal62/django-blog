from .models import UserProfile

def user_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()
        return {'nav_profile': profile}
    return {'nav_profile': None}