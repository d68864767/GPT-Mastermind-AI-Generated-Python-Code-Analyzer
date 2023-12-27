```python
from gpt_integration import GPTIntegration

class ReadabilityEnhancements:
    def __init__(self, api_key):
        self.gpt = GPTIntegration(api_key)

    def enhance_readability(self, code):
        try:
            response = self.gpt.generate_code_suggestions(f"{code}\n# How can I make this code more readable?")
            return response
        except Exception as e:
            print(f"An error occurred while enhancing readability: {str(e)}")
            return None

    def suggest_comments(self, code):
        try:
            response = self.gpt.generate_code_suggestions(f"{code}\n# Suggest comments for this code")
            return response
        except Exception as e:
            print(f"An error occurred while suggesting comments: {str(e)}")
            return None

    def generate_readability_enhancements(self, code):
        readability_enhancements = self.enhance_readability(code)
        comment_suggestions = self.suggest_comments(code)

        return {
            "readability_enhancements": readability_enhancements,
            "comment_suggestions": comment_suggestions
        }
```
