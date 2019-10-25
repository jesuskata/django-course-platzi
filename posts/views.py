"""Posts Views"""
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Josue',
        'user': {
          'name': 'Josue',
          'picture': 'https://picsum.photos/id/177/64/64'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1005/600/600'
    },
    {
        'title': 'Exodo',
        'user': {
          'name': 'Moisés',
          'picture': 'https://picsum.photos/id/1082/64/64'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1010/600/600'
    },
    {
        'title': 'Génesis',
        'user': {
          'name': 'Moisés',
          'picture': 'https://picsum.photos/id/1082/64/64'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1035/600/600'
    },
]

@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
