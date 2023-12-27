```python
class ErrorHandling:
    def __init__(self):
        pass

    def handle_errors(self, function, *args):
        try:
            return function(*args)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def handle_gpt_errors(self, gpt_function, code):
        try:
            return gpt_function(code)
        except Exception as e:
            print(f"An error occurred while processing GPT function: {str(e)}")
            return None

    def handle_file_errors(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")
            return None
```
