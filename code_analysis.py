```python
from gpt_integration import GPTIntegration

class CodeAnalysis:
    def __init__(self, api_key):
        self.gpt = GPTIntegration(api_key)

    def analyze_code_structure(self, code):
        try:
            response = self.gpt.analyze_code(code)
            return response
        except Exception as e:
            print(f"An error occurred while analyzing code structure: {str(e)}")
            return None

    def analyze_code_readability(self, code):
        try:
            response = self.gpt.generate_code_suggestions(code)
            return response
        except Exception as e:
            print(f"An error occurred while analyzing code readability: {str(e)}")
            return None

    def analyze_code_efficiency(self, code):
        try:
            response = self.gpt.analyze_code(code)
            return response
        except Exception as e:
            print(f"An error occurred while analyzing code efficiency: {str(e)}")
            return None

    def analyze_code(self, code):
        structure_analysis = self.analyze_code_structure(code)
        readability_analysis = self.analyze_code_readability(code)
        efficiency_analysis = self.analyze_code_efficiency(code)

        return {
            "structure_analysis": structure_analysis,
            "readability_analysis": readability_analysis,
            "efficiency_analysis": efficiency_analysis
        }
```
