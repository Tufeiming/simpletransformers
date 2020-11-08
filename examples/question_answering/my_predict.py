# -*- coding: UTF-8 -*-
import json
import torch
from simpletransformers.question_answering import QuestionAnsweringModel
from generate_data import generate_example


def predict(model, context):
    to_predict = [
        generate_example(context)
    ]

    result = model.predict(to_predict)
    final_result = {}
    for i in range(len(result[0])):
        if result[0][i]["answer"][0] == "empty":
            final_result[result[0][i]["id"]] = ""
        else:
            final_result[result[0][i]["id"]] = result[0][i]["answer"][0]
    return final_result


def main():
    # 创建模型
    train_args = {
        "do_lower_case": True,
        "encoding": "utf-8",
        "learning_rate": 3e-5,
        "max_seq_length": 512,
        "doc_stride": 128,
        "max_query_length": 10,
        "n_best_size": 5,
        "max_answer_length": 60
    }
    use_cuda = torch.cuda.is_available()
    print(use_cuda)
    model = QuestionAnsweringModel("bert", "model", use_cuda=use_cuda, args=train_args)

    # 例子
    context = "START4283 中标信息详情 [朝阳]分局处突车防护装备更新成交公告更正公告 2020-10-3013：03：16 一、项目基本情况 原公告的采购项目编号：CYCG_20_1846 原公告的采购项目名称：分局处突车防护装备更新 首次公告日期：2020-10-2916：42地址：http：//www.ccgp-beijing.gov.cn/xxgg/qjzfcggg/qjzbjggg/t20201029_1287683.html 二、更正信息 更正事项：采购结果 更正内容： 1、主要标的信息中防弹防刺服数量1更正为195 2、补充公告附件 更正日期：2020-10-3011：00 三、其他补充事宜 / 四、凡对本次公告内容提出询问，请按以下方式联系。 1.采购人信息 名称：北京市公安局朝阳分局机关 地址：北京市朝阳区道家园1号 联系方式：吕德华,85953808 2.采购代理机构信息 名称：北京合信恒盛咨询有限公司 地　址：北京市朝阳区幺家店路常营公园内办公区办公用房 联系方式：李冬，65766188-8013 3.项目联系方式 项目联系人：李冬 电　话：　　65766188-8013 更多内容请 下载保标APP 2015- 2019 woyaobid.com.AllRightsReserved世舶科技（武汉）有限公司版权所有 $(document).ready(function(){vardate=newDate；varnewyear=date.getFullYear()；$(\"#new_year\").html(newyear)；$(\"table\").each(function(){$(this).wrap(\"<divclass='margin-tong'></div>\")；})；})；；END"
    result = predict(model, context)
    print(json.dumps(result, ensure_ascii=False, indent=4))

    # 输出如下
    # {
    #     "budget_amount": "",
    #     "bid_amount": "",
    #     "party_a_name": "北京市公安局朝阳分局机关",
    #     "party_a_contact": "吕德华",
    #     "party_a_contact_number": ",85953808",
    #     "agency_name": "北京合信恒盛咨询有限公司",
    #     "agency_contact": "李冬",
    #     "agency_contact_number": "65766188-8013",
    #     "party_b_name": ""
    # }


if __name__ == '__main__':
    main()
