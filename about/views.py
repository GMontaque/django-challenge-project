from django.shortcuts import render
from .models import About
from django.shortcuts import render, get_object_or_404

# Create your views here.
def about_detail(request):
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about}
    )
