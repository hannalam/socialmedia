# I wrote this code

from django.shortcuts import render, redirect
from .forms import CreateStatusForm
from django.contrib.auth.decorators import login_required
from .models import Status
from django.shortcuts import get_object_or_404

# Create your views here.


@login_required
def create_status(request):
    if request.method == 'POST':
        form = CreateStatusForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')

    else:
        form = CreateStatusForm(data=request.GET)
    return render(request, 'status/newpost.html', {'form': form})


def main(request):
    status = Status.objects.all()
    logged_user = request.user
    return render(request, 'status/main.html', {'status': status, 'logged_user': logged_user})


def likes(request):
    status_id = request.POST.get('status_id')
    status = get_object_or_404(Status, id=status_id)
    if status.likes.filter(id=request.user.id).exists():
        status.likes.remove(request.user)
    else:
        status.likes.add(request.user)
    return redirect('main')

# end of code I wrote
