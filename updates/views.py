from django.shortcuts import render


def home(request):
    updates = [
        {
            'title': 'Freelance hosting updates live',
            'description': 'Hosting, deployment, and maintenance updates for your projects.',
            'time': '2026-05-05',
        },
        {
            'title': 'Platform built with Django + Python',
            'description': 'Clean frontend and backend ready for GitHub deployment.',
            'time': '2026-05-05',
        },
        {
            'title': 'Simple hosting dashboard',
            'description': 'White background, easy updates, no login required.',
            'time': '2026-05-05',
        },
    ]
    context = {
        'brand': 'keen_to_basic_0s_1s',
        'tagline': 'Every operation in computer all system are 1s and 0s',
        'updates': updates,
    }
    return render(request, 'updates/home.html', context)
