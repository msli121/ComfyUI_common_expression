class AnyToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("ANY", {"default": None, "dynamicPrompts": True}),
                "input_boolean": ("BOOLEAN", {"default": None, "optional": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "convert"
    CATEGORY = "utils/convert"

    def convert(self, input, as_boolean=None):
        if as_boolean is not None:
            return str(as_boolean)
        if input is None:
            return ("",)
        return (str(input),)
