from django.shortcuts import render, get_object_or_404, redirect
from .models import EBook
from .forms import EBookForm
from django.contrib.auth.decorators import login_required

def ebook_list(request):
    ebooks = EBook.objects.all()
    return render(request, 'ebooks/ebook_list.html', {'ebooks': ebooks})

def ebook_detail(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    return render(request, 'ebooks/ebook_detail.html', {'ebook': ebook})

@login_required
def add_ebook(request):
    if request.method == 'POST':
        form = EBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EBookForm()
    return render(request, 'ebooks/add_ebook.html', {'form': form})
