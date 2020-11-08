import json


def get_question(field, keyword_list, context):
    if field == "budget_amount":
        question = "预算金额"
    elif field == "bid_amount":
        question = "中标金额"
    elif field == "party_a_name":
        question = "采购人"
    elif field == "party_a_contact":
        question = "采购联系人"
    elif field == "party_a_contact_number":
        question = "采购联系电话"
    elif field == "agency_name":
        question = "代理机构"
    elif field == "agency_contact":
        question = "代理机构联系人"
    elif field == "agency_contact_number":
        question = "代理机构联系电话"
    elif field == "party_b_name":
        question = "中标人"
    else:
        question = ""
    for keyword in keyword_list:
        if keyword in context:
            question = keyword
            break
    return question


def generate_example(input_text):
    context = input_text
    qas = []

    # 预算金额
    temp_field = "budget_amount"
    temp_list = ['预算金额', '采购金额', '招标控制价', '投资额', '总预算', '采购预算价',
                 '采购资金', '最高限价', '控制价', '拦标价', '建安造价', '工程预算']
    temp_question = get_question(temp_field, temp_list, context)
    qas.append({"question": temp_question, "id": temp_field})

    # 中标金额
    temp_field = "bid_amount"
    temp_list = ['中标金额', '成交金额', '预中标价格', '合同金额', '合同总金额', '中标价格',
                 '成交价格', '采购合同金额', '签约合同价', '成交价', '成交价合计', '成交价款',
                 '成交商家报价', '中标商家报价', '中选金额']
    temp_question = get_question(temp_field, temp_list, context)
    qas.append({"question": temp_question, "id": temp_field})

    # 甲方名称
    temp_field = "party_a_name"
    temp_list = ['采购单位', '招标单位', '建设单位', '采购单位名称', '招标人名称', '招标人单位名称',
                 '采购人', '招标人', '发包人', '采购人名称']
    temp_question = get_question(temp_field, temp_list, context)
    qas.append({"question": temp_question, "id": temp_field})

    # 甲方联系人
    temp_field = "party_a_contact"
    temp_list = ['采购', '招标']
    temp_question = get_question(temp_field, temp_list, context) + "联系人"
    qas.append({"question": temp_question, "id": temp_field})

    # 甲方联系电话
    temp_field = "party_a_contact_number"
    temp_list = ['采购', '招标']
    temp_question = get_question(temp_field, temp_list, context) + "联系电话"
    qas.append({"question": temp_question, "id": temp_field})

    # 代理机构名称
    temp_field = "agency_name"
    qas.append({"question": "代理机构", "id": temp_field})

    # 代理机构联系人
    temp_field = "agency_contact"
    qas.append({"question": "代理机构联系人", "id": temp_field})

    # 代理机构联系电话
    temp_field = "agency_contact_number"
    qas.append({"question": "代理机构联系电话", "id": temp_field})

    # 乙方名称
    temp_field = "party_b_name"
    temp_list = ['乙方', '供应商', '中标单位', '中标公司', '成交单位',
                 '成交公司', '承包单位', '承包公司', '中标人', '成交人', '承包人']
    temp_question = get_question(temp_field, temp_list, context)
    qas.append({"question": temp_question, "id": temp_field})

    return {
        "qas": qas,
        "context": context
    }


if __name__ == '__main__':
    text = "START项目名称和编号 西南财经大学智慧教室多媒体智能扩音设备采购项目(WZ201929) 采购人 西南财经大学" \
           " 地址及联系方式 成都市温江区柳台大道555号028-87092439 评审小组 纪建国、钱彤、李科、胡芳、赵亮 中标商家名称 " \
           "成都市创航科技有限公司 中标商家地址 成都市武侯区人民南路四段一号 中标商家报价 461800元 主要标的名称 智能扩音设备一：" \
           "艾力特OS-704FC-A80台 智能扩音设备二：艾力特SPK-3E196台 智能扩音设备三：艾力特MS-D05080台；END"
    data = generate_example(text)
    print(json.dumps(data, ensure_ascii=False, indent=4))
