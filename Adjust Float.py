class AdjustFloat:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_float": ("FLOAT", {
                    "default": 0.0,  # 默认值
                    "min": -1000.0,  # 最小值
                    "max": 1000.0,   # 最大值
                    "step": 0.01     # 步长
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)  # 返回类型为浮点数
    FUNCTION = "adjust_float"
    CATEGORY = "Math Operations"

    def adjust_float(self, input_float):
        integer_part = int(input_float)  # 获取整数部分
        decimal_part = input_float - integer_part  # 获取小数部分
        decimal_first_digit = int(decimal_part * 10)  # 获取小数点后的第一位数字
        
        if decimal_first_digit >= 5:
            return (float(integer_part + 1),)  # 如果小数部分为5或更大，整数部分加1
        else:
            return (float(integer_part),)  # 否则返回整数部分

# 注册节点类
NODE_CLASS_MAPPINGS = {
    "AdjustFloat": AdjustFloat
}

# 显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "AdjustFloat": "Adjust Float"
}
