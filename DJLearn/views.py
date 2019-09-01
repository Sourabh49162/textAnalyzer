from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djText = request.POST.get('text', 'default')
    djRemPun = request.POST.get('rempunc', 'off')
    djUpCase = request.POST.get('uppercase', 'off')
    djNewLineRem = request.POST.get('newlinerem', 'off')
    djExtraSpaceRem = request.POST.get('extraspacerem', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if(djRemPun == 'on'):
        analyze = ''
        for char in djText:
            if char not in punctuations:
                analyze = analyze + char
        params = {'purpose': 'Remove Punctuations', 'analyze_text': analyze}
        djText = analyze
    if(djUpCase == 'on'):
        analyze = ''
        for char in djText:
            analyze = analyze + char.upper()
        params = {'purpose': 'Upper Case', 'analyze_text': analyze}
        djText = analyze
    if(djNewLineRem == 'on'):
        analyze = ''
        for char in djText:
            if char != '\n' and char != '\r':
                analyze = analyze + char
        params = {'purpose': 'New Line Remove', 'analyze_text': analyze}
        djText = analyze
    if(djExtraSpaceRem == 'on'):
        analyze = ''
        for index, char in enumerate(djText):
            if not(djText[index] == ' ' and djText[index+1] == ' '):
                analyze = analyze + char
        params = {'purpose': 'Extra Space Remove', 'analyze_text': analyze}
        djText = analyze

    return render(request, 'analyze.html', params)
