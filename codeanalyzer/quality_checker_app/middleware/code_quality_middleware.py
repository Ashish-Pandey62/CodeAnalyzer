from django.http import JsonResponse
from quality_checker_app.utils.gemini_api import generate_gemini_response

class CodeQualityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/analyze_code/' and request.method == 'POST':
            code = request.POST.get('code', '')
            if code:
                try:
                    analysis = generate_gemini_response(code)
                    return JsonResponse({'analysis': analysis})
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=400)
        
        response = self.get_response(request)
        return response