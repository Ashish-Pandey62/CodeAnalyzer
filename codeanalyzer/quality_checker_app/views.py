from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST"])
def analyze_code(request):
    return JsonResponse({'message': 'Code analysis request received'})

def trigger_error(request):
    division_by_zero = 1 / 0
    return JsonResponse({'result': division_by_zero})