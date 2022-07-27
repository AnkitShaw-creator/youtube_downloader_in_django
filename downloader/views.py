from turtle import title
from django.shortcuts import render, redirect
from pytube import YouTube
# Create your views here.

URL = ''

def home(request):
    return render(request, 'downloader/home.html')


def downloadLink(request):
    lnk = request.GET.get('request_url')
    #print(lnk)
    yt = YouTube(lnk)
    res = yt.streams
    
    res = list(dict.fromkeys(res))
    print(res)
    video_meta_data = {}
    video_meta_data['request_link']= lnk
    video_meta_data['title']= yt.title
    video_meta_data['thumbnail_url']= yt.thumbnail_url
    video_meta_data['rating']=yt.rating
    video_meta_data['author']= yt.author
    video_meta_data['age_restriction']= yt.age_restricted
    video_meta_data['length']= yt.length
    
    if request.method == 'GET':
        return render(request, 'downloader/download.html', {'meta_data': video_meta_data,'rsl': res})

    if request.method == 'POST':
        ys = yt.streams.get_by_itag(int(request.POST['i_tag']))
        #'C:\\Users\\ankishaw\\Desktop'
        ys.download('C:\\Users\\ankishaw\\Desktop')
        return render(request, 'downloader/download.html', {'meta_data': video_meta_data, 'rsl': res, 'message': 'Video downloaded in your desktop'})
    