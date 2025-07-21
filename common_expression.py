import re
from typing import List


class CommonExpression:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "operation": (
                    [
                        "KeywordInString",
                        "KeywordAllInString",
                        "==",
                        "!=",
                        ">",
                        "<",
                        ">=",
                        "<=",
                    ],
                ),
                "input_a": (
                    "ANY",
                    {"multiline": False, "default": "", "dynamicPrompts": True},
                ),
                "input_b": (
                    "ANY",
                    {"multiline": False, "default": "", "dynamicPrompts": True},
                ),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "evaluate"
    CATEGORY = "utils/logic"

    def evaluate(self, operation, input_a, input_b):
        result = False
        input_a = str(input_a)
        input_b = str(input_b)

        try:
            if operation == "KeywordInString":
                keywords = [k.strip() for k in input_b.split(",") if k.strip()]
                result = any(kw in input_a for kw in keywords)

            elif operation == "KeywordAllInString":
                keywords = [k.strip() for k in input_b.split(",") if k.strip()]
                result = all(kw in input_a for kw in keywords)

            elif operation == "==":
                result = input_a == input_b

            elif operation == "!=":
                result = input_a != input_b

            elif operation == ">":
                try:
                    result = float(input_a) > float(input_b)
                except:
                    result = len(input_a) > len(input_b)

            elif operation == "<":
                try:
                    result = float(input_a) < float(input_b)
                except:
                    result = len(input_a) < len(input_b)

            elif operation == ">=":
                try:
                    result = float(input_a) >= float(input_b)
                except:
                    result = len(input_a) >= len(input_b)

            elif operation == "<=":
                try:
                    result = float(input_a) <= float(input_b)
                except:
                    result = len(input_a) <= len(input_b)

        except Exception as e:
            print(f"表达式计算错误: {str(e)}")
            result = False

        return (result,)
