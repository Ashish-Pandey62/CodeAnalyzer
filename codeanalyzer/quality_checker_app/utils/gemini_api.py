from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

fixed_description = '''
You are requested to do the detail analysis of the django code provided to you and provide any suggestions by mentioning the code quality out of 10 and mention the possible changes that might make the code better
'''

def generate_gemini_response(prompt):
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt_with_desc = f"{fixed_description} {prompt}".strip()
        response = model.generate_content(prompt_with_desc)
        return response.text
    except (ImportError, AttributeError) as e:
        return f"Error: {str(e)}"