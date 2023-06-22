from django.shortcuts import render
from django.http import HttpResponse

speakers = [
    {
        'id': 1,
        'name': 'John Smith',
        'email': 'john.smith@gmail.com',
    },
    {
        'id': 2,
        'name': 'Kenneth Kabwe',
        'email': 'kenneth.kabwe@gmail.com',
    },
    {
        'id': 3,
        'name': 'William Buto',
        'email': 'william.buto@gmail.com',
    }
]

def update_speaker (request, id:int):
    speaker = list(filter(lambda c: c['id'] == id, speakers))[0]
    return render (request, 'update_speaker.html', { 'speaker': speaker} )

