from django.http import JsonResponse

# Create your views here.
def hello_world(request):
    """Return jsonresponse"""
    data = {
        "mensage": "Bienvenido al Monolito, Santiago"
        }
    
    return JsonResponse(data)