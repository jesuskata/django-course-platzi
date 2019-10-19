"""Platzigram Views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is: {now}')

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    # import pdb; pdb.set_trace()
    # dumps traduce un diccionario a un json
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = f"Sorry {name}, you are not allowed to enter here."
    else:
        message = f'Welcome to Platzigram dear {name}'
    return HttpResponse(message)
