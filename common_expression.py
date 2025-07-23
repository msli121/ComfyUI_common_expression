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
                        "and",
                        "or",
                        "chinese_chars_count_ge",
                        "chinese_chars_count_le",
                    ],
                ),
                "input_a": (
                    "STRING",
                    {"multiline": False, "default": "", "dynamicPrompts": True},
                ),
                "input_b": (
                    "STRING",
                    {"multiline": False, "default": "", "dynamicPrompts": False},
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

            elif operation == "and":
                input_a = input_a.lower()
                if input_a in ['true', '1', 't', 'y', 'yes']:
                    input_a_bool = True
                else:
                    input_a_bool = False
                if input_b in ['true', '1', 't', 'y', 'yes']:
                    input_b_bool = True
                else:
                    input_b_bool = False
                result = input_a_bool and input_b_bool

            elif operation == "or":
                if input_a in ['true', '1', 't', 'y', 'yes']:
                    input_a_bool = True
                else:
                    input_a_bool = False
                if input_b in ['true', '1', 't', 'y', 'yes']:
                    input_b_bool = True
                else:
                    input_b_bool = False
                result = input_a_bool or input_b_bool

            elif operation == "chinese_chars_count_ge":
                chinese_char_count = int(input_b)
                input_a = str(input_a)
                # 统计input_a中中文字符个数
                chinese_chars = [char for char in input_a if '\u4e00' <= char <= '\u9fa5']
                result = len(chinese_chars) >= chinese_char_count

            elif operation == "chinese_chars_count_le":
                chinese_char_count = int(input_b)
                input_a = str(input_a)
                # 统计input_a中中文字符个数
                chinese_chars = [char for char in input_a if '\u4e00' <= char <= '\u9fa5']
                result = len(chinese_chars) <= chinese_char_count

        except Exception as e:
            print(f"表达式计算错误: {str(e)}")
            result = False

        return (result,)
