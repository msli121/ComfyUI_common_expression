class AnyToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("ANY", {"default": None, "dynamicPrompts": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "convert"
    CATEGORY = "utils/convert"

    def convert(self, input):
        if input is None:
            return ("",)
        return (str(input),)
