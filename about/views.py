from django.shortcuts import render
from .models import About
from django.shortcuts import render, get_object_or_404
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.
def about_detail(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )   
    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form":collaborate_form
        },
        
    )


#  if request.method == "POST":
#         print("Received a POST request")
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Comment submitted and awaiting approval'
#             )   

#     comment_form = CommentForm()