from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def keyboard(request):
    return JsonResponse(
        {
            'type': 'message',
            'text': '나의 세계에 온걸 환영해!!\n 채팅창에 "소개"라고 적는다면 나에대해서 더 많은걸 알수있어.'
        }
    )

@csrf_exempt    
def message(request):
    json_str = (request.body).decode('urf-8')#resquest를 한글호환되는 utf8로 변환
    received_json = json.loads(json_str)#json문자열로 되어있는걸 python 타입으로 변경시킴
    content_name = received_json['content']#사용자가 보낸 명령어에서 필드명이 content인 항목을 변수저장.
    requestMode = content_name.encode('utf-8')
    if requestMode == '소개':
        return JsonResponse({
            'message' : {
                 'photo': {
                    'url':'http://ishilly.tistory.com/30',
                    'width': 640,
                    'height': 480
                },
                'text': '안녕 날 소개하지 이름은 황광회\n 취미는 프로그래밍,독서,힙합감상'
            },
            'keyboard': {
                'type' : 'text'
            }
        })    

# Create your views here.
