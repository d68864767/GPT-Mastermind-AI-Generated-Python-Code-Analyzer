```python
from gpt_integration import GPTIntegration

class ErrorDetection:
    def __init__(self, api_key):
        self.gpt = GPTIntegration(api_key)

    def detect_errors(self, code):
        try:
            response = self.gpt.analyze_code(code)
            if "error" in response.lower():
                return response
            else:
                return "No errors detected"
        except Exception as e:
            print(f"An error occurred while detecting errors: {str(e)}")
            return None

    def suggest_error_resolution(self, code):
        try:
            response = self.gpt.generate_code_suggestions(code)
            if "error" in response.lower():
                return response
            else:
                return "No error resolution suggestions"
        except Exception as e:
            print(f"An error occurred while suggesting error resolution: {str(e)}")
            return None

    def analyze_code(self, code):
        error_detection = self.detect_errors(code)
        error_resolution_suggestion = self.suggest_error_resolution(code)

        return {
            "error_detection": error_detection,
            "error_resolution_suggestion": error_resolution_suggestion
        }
```
