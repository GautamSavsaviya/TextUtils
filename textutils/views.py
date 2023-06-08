# This file is create explicitly

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get row_data from user using get request
    row_data = str(request.POST.get('text', 'nothing is get'))

    # Get status of checkbox value
    remove_punctuations = request.POST.get('remove_punctuations', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remove_newline = request.POST.get('remove_newline', 'off')
    remove_spaces = request.POST.get('remove_spaces', 'off')
    char_count = request.POST.get('char_count', 'off')
    purpose = ''

    # Create a variable that store the analyzed text after perform some operations on row text
    analyzed_text = ''

    # Check which checkbox is on and perform operation according to it

    # Remove Punctuations
    if remove_punctuations == 'on':
        punctuations = """!()-[];:'"\\,<>./?@#$%^&*_~{}"""
        for ch in row_data:
            if ch not in punctuations:
                analyzed_text += ch

        row_data = analyzed_text
        purpose += 'Remove Punctuations, '

    # Convert into upper case
    if capitalize == 'on':
        analyzed_text = row_data.upper()

        row_data = analyzed_text
        purpose += 'Convert into upper case, '

    # Remove newline
    if remove_newline == 'on':
        if '\n' in row_data and '\r' in row_data:
            analyzed_text = row_data.replace('\n', '')
            analyzed_text = analyzed_text.replace('\r', ' ')
        row_data = analyzed_text
        purpose += 'Remove new line, '

    # Remove extra white spaces
    if remove_spaces == 'on':
        for index in range(len(row_data)):
            if not (row_data[index] == ' ' and row_data[index + 1] == ' '):
                analyzed_text += row_data[index]

        row_data = analyzed_text
        purpose += 'Remove extra white spaces, '

    # Count total no of characters
    if char_count == 'on':
        count = len(row_data)
        analyzed_text = f'Total no of characters in "{row_data}" is {count}'

        purpose += ' Count total no of characters,'

    if remove_punctuations != 'on' and capitalize != 'on' and remove_newline != 'on' and remove_spaces != 'on' and char_count != 'on':
        return HttpResponse("Error")
    else:
        parameters = {'purpose': purpose, 'analyze_text': analyzed_text}
        return render(request, 'analyze.html', parameters)
