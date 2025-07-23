import json

class AnyToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_data": ("*",),  # Accept any type
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string_result",)
    FUNCTION = "to_string"
    CATEGORY = "utils/string"

    def to_string(self, input_data):
        try:
            # Try converting to JSON string if possible (for better structure)
            string_result = json.dumps(input_data, ensure_ascii=False)
        except (TypeError, ValueError):
            # Fallback to Python str()
            string_result = str(input_data)
        return (string_result,)
