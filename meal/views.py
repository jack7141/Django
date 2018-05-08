from django.http import JsonResponse

def keyboard(request):

    return JsonResponse(
        {
	'type': 'buttons',
	'buttons': ['home','school','etc']
        }
    )

# Create your views here.
