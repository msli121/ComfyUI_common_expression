import json


class AnyToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "boolean_input": ("BOOLEAN", {"default": None}),
                "int_input": ("INT", {"default": None}),
                "float_input": ("FLOAT", {"default": None}),
                "list_input": ("LIST", {"default": None}),
                "dict_input": ("DICT", {"default": None}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "to_string"
    CATEGORY = "utils/type_conversion"

    def to_string(self, boolean_input=None, int_input=None, float_input=None,
                  list_input=None, dict_input=None):
        all_inputs = [boolean_input, int_input, float_input, list_input, dict_input]
        value = next((v for v in all_inputs if v is not None), None)

        if value is None:
            return ("",)
        try:
            return (json.dumps(value, ensure_ascii=False, default=str),)
        except Exception:
            return (str(value),)
