from .common_expression import CommonExpression
from .any_to_string import AnyToString

NODE_CLASS_MAPPINGS = {
    "common_expression": CommonExpression,
    "any_to_string": AnyToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "common_expression": "通用表达式判断",
    "any_to_string": "任意类型转字符串",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
