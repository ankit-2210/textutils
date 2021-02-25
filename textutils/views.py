# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Happy Coding")
#
# def about(request):
#     return HttpResponse("About Myself")

# def navigation(request):
#     s = '''<h2>Navigation Bar <br></h2>
#              <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
#              <a href="https://www.facebook.com/">Facebook</a><br>
#              <a href="https://www.flipkart.com/">Flipkart</a><br>
#              <a href="https://www.hindustantimes.com">News</a><br>
#              <a href="https://www.google.com/">Google</a>  '''
#
#     return HttpResponse(s)


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'No text entered')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    str = djtext
    purpose = ""
    # Check which checked is on
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        str = analyzed
        purpose += "| Remove Punctuations"

        #return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        str = analyzed
        purpose += "| Changed to uppercase"

        #return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        str = analyzed
        purpose += "| Removed NewLines"

        #return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        str = analyzed
        purpose += "| Remove Extra Space"

        #return render(request, 'analyze.html', params)

    elif(charcount == "on"):
        analyzed = ""
        analyzed = len(djtext)

        params = {'purpose': 'Length of Char', 'analyzed_text': analyzed}
        str = analyzed
        purpose += "| Length of Char"

        #return render(request, 'analyze.html', params)

        params = {'purpose': purpose, 'analyzed_text': str}

    if(removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on' or charcount == 'on'):
            return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")






















     
     

