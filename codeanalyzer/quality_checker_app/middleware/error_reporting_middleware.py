# quality_checker_app/middleware.py

import sys
import traceback
from django.http import JsonResponse
from quality_checker_app.utils.langchain_api import create_code_analysis_chain

class ErrorReportingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.chain = create_code_analysis_chain()  # Initialize the analysis chain once

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            error_details = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))

            prompt = f"Explain this error and suggest possible fixes:\n\n{error_details}"
            explanation = self.chain.run({"code": prompt})  # Run the error analysis

            return JsonResponse({
                'error': str(e),
                'explanation': explanation
            }, status=500)
