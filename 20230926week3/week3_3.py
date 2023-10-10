#3 正则表达式验证身份证号是否合法(from gpt)
import re


def validate_id_card(id_card):
    # 定义身份证号的正则表达式
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}(\d|X|x)$'

    # 使用正则表达式匹配身份证号
    match = re.match(pattern, id_card)

    # 如果匹配成功，则返回True，否则返回False
    if match:
        return True
    else:
        return False