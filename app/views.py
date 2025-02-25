from django.shortcuts import redirect, render
from .models import SlangWord
from .forms import SlangForm

## project/app/views.py
from django.shortcuts import render

# from .app.forms import SlangForm

def slang_list(request):
    slang_words = SlangWord.objects.all()
    return render(request, 'new_slang_list.html', {'slang_words': slang_words})

def add_slang(request):
    if request.method == 'POST':
        form = SlangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('slang_list')
    else:
        form = SlangForm()
    return render(request, 'add_slang.html', {'form': form})

def category_view(request, slug):
    # Filter slang words by category (you'll need to add a category field to your model)
    slang_words = SlangWord.objects.filter(category=slug)
    return render(request, 'new_slang_list.html', {'slang_words': slang_words})
