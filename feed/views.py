from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message, Comment, Like
from .forms import MessageForm 
from django.contrib.auth import logout

@login_required
def feed(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'feed/feed.html', {'messages': messages})

@login_required
def post_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(user=request.user, content=content)
    return redirect('feed:feed')

@login_required
def post_comment(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, message=message, content=content)
    return redirect('feed:feed')

@login_required
def like_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    Like.objects.get_or_create(user=request.user, message=message)
    return redirect('feed:feed')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.user:
        message.delete()
    return redirect('feed:feed')

@login_required
def add_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)  
            message.user = request.user        
            message.save()                     
            return redirect('feed:feed')       
    else:
        form = MessageForm()
    return render(request, 'feed/add_message.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  
