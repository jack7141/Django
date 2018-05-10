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
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    
    
    return JsonResponse({
            'message': {
                'text':' 중식 메뉴입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['상록원', '그루터기', '아리수', '기숙사식당', '교직원식당']
            }

        })
