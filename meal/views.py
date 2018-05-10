from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
def keyboard(request):
    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['선택1']
        }
    )

@csrf_exempt    
def message(request):
    json_str = ((request.body).decode('urf-8'))#resquest를 한글호환되는 utf8로 변환
    received_json = json.loads(json_str)#json문자열로 되어있는걸 python 타입으로 변경시킴
    content_name = received_json['content']#사용자가 보낸 명령어에서 필드명이 content인 항목을 변수저장.
    requestMode = content_name.encode('utf-8')
    if requestMode == '선택1' :
        return JsonResponse(
            {
               'message' : {
                    'text' : "번역할 내용을 다음과 같이 입력해 주세요.(개발중)\n ex)번역 뭐해?, 번역 안녕ㅋㅋ\n 형식을 갖추지 않으면 답변이 나오지 않습니다ㅜㅜ."
                },
               'keyboard' : {
                    'type' : 'buttons', # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
		    'buttons': ['school','test']			
                }
            }
        )
