from django.shortcuts import render,redirect
from .models import Video
from .forms import VideForm

# Create your views here.
def index(request):
    videos=Video.objects.all()
    return render(request,'index.html',{'videos':videos})

def upload(request):
    if request.method == 'POST':
        form=VideForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=VideForm()
    return render(request,'upload.html',{'form':form})


def player(request,pk):
    if request.method =='POST':
        videos=Video.objects.get(pk=pk)
        url=videos.video.url 
        print(url)
        return render(request,'player.html',{'url':url})
    return render(request,'player.html')

def delete_video(request,pk):
    if request.method == 'POST':
        videos=Video.objects.get(pk=pk)
        videos.delete()
    return redirect('/')

    
