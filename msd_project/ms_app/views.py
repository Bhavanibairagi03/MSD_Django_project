from django.shortcuts import render, redirect
from .forms import GeekForm

# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = GeekForm(request.POST, request.FILES)
        if form.is_valid():
            geek_instance = form.save()

            # Store relevant information about the uploaded file in the session
            request.session['uploaded_file_info'] = {
                'file_path': geek_instance.img.url,
                'file_name': geek_instance.img.name,
                'title': geek_instance.title,
                'discription': geek_instance.discription,
            }

            return render(request, "success.html")
    else:
        form = GeekForm()

    return render(request, 'home.html', {'form': form})
