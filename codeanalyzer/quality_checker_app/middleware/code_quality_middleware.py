from django.http import JsonResponse
from quality_checker_app.utils.langchain_api import create_code_analysis_chain

class CodeQualityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.chain = create_code_analysis_chain()  # Initialize the analysis chain here

    def __call__(self, request):
        if request.path == '/analyze_code/' and request.method == 'POST':
            code = request.POST.get('code', '')
            if code:
                try:
                    # Call the chain with the provided code
                    analysis = self.chain.run({"code": code})
                    return JsonResponse({'analysis': analysis})
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=400)
        
        response = self.get_response(request)
        return response
