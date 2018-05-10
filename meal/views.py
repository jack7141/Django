from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def keyboard(request):

    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['이름','나이','키']
        }
    )

@csrf_exempt    
def message(request):
    
    return JsonResponse(
        {
            'message': {
                'text': '나의 세계에 온걸 환영해',
                'photo': {
                    'url':'http://ishilly.tistory.com/30',
                    'width': 640,
                    'height': 480
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['이름','나이','키']

            }
        }
    )    

# Create your views here.
