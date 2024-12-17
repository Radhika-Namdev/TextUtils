from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text 
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extra_spaceremover=request.POST.get('extra_spaceremover', 'off')

# check whch box is on
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'removepunctuations','analyzed_text':analyzed}
        djtext=analyzed
        
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to upperCase','analyzed_text':analyzed}
        djtext=analyzed

    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'remove new lines','analyzed_text':analyzed}
        djtext=analyzed

    if (extra_spaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'remove Spaces','analyzed_text':analyzed}
        djtext=analyzed

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extra_spaceremover!="on"):
        return HttpResponse("Error! You have not selected any options.")

    return render(request,'analyze.html',params)
    