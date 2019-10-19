"""Posts Views"""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Josue',
        'user': 'Josue',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1005/200/200'
    },
    {
        'name': 'Exodo',
        'user': 'Moisés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1010/200/200'
    },
    {
        'name': 'Génesis',
        'user': 'Moisés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1035/200/200'
    },
]

def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src={picture}/></figure>
        """.format(**post))
    return HttpResponse('<br/>'.join(content))
