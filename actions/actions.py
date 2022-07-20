# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, AllSlotsReset
import random
import re

demo_data_list = [
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 890,
            "price": "1484.00",
            "product_id": 571029,
            "product_name": "SL-防蓝光抗疲劳显年轻远近两用高档眼镜",
            "logo_url": "https://oss.giikin.cn/uploads/8d7cf1f242a764f73c68d98cdf1bec8b.jpg",
            "areaId": 100,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮-菲律宾",
            "sale_id": 1001895321,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 100,
            "options": {"chinese": [{"name": "颜色", "values": "红色，紫色，黑色，茶色"},
                                    {"name": "规格", "values": "100度，150度，200度，250度，300度，350度，400度"}],
                        "trans": [{"trans_name": "Color", "trans_values": "red，purple，Black，Sand tea"},
                                  {"trans_name": "Specification",
                                   "trans_values": "+100°(Under 45)，+150°(45-50Years old)，+200°(50-55Years old)，+250°(55-60Years old)，+300°(60-65Years old)，+350°(65-70Years old)，+400°(Above 70 years old)"}]},
            "rules": "【Buy 1 free 1】2 for ₱890，【Buy 2 free 2】4 for ₱1090",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895321"
        },
        "duration": 83.03189277648926,
        "memory": "989.77 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 1299,
            "price": "2319.00",
            "product_id": 1001701,
            "product_name": "X22061501Jc-防晒冰丝袖套",
            "logo_url": "https://oss.giikin.cn/uploads/8727e81a5e3704fcf58fe69f8872d697.jpg",
            "areaId": 184,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "雪豹运营中心",
            "sale_id": 1001885321,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 184,
            "options": {
                "chinese": [
                    {
                        "name": "尺码",
                        "values": "均码"
                    },
                    {
                        "name": "颜色",
                        "values": "【玉桂狗】，向日葵，太空熊，库洛米"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Free size"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "Cinnamoroll Dog，Sunflower，Space Bear，Kuromi"
                    }
                ]
            },
            "rules": "Buy 2 pairs free 2 pairs 1299，Buy 4 pairs free 4 pairs 1799 (only 225 per pair)",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001885321"
        },
        "duration": 34.50417518615723,
        "memory": "989.37 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 85,
            "price": "170.00",
            "product_id": 578293,
            "product_name": "X21110501Fc-纯色袜",
            "logo_url": "https://oss.giikin.cn/uploads/54335ae2d7d0409dc212b2cb92e06f6f.jpg",
            "areaId": 14,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮家族-马来西亚",
            "sale_id": 1001885221,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 14,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "男黑，男白，女黑，女白"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Male black，Male white，Female black， Female white"
                    }
                ]
            },
            "rules": "6 pairs RM125，3 pairs RM85",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001885221"
        },
        "duration": 83.15396308898926,
        "memory": "988.44 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 37900,
            "price": "75800.00",
            "product_id": 587603,
            "product_name": "X21122102Bc-电动蒜泥神器捣蒜器",
            "logo_url": "https://oss.giikin.cn/uploads/a1a996ff3e3806b5726fb4c6e0ca039f.jpg",
            "areaId": 99,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "精灵家族-韩国",
            "sale_id": 1001885211,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 99,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "大动力白色-100ml，大动力粉色-100ml，大动力蓝色-100ml，普通黑色-100ml"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "색상",
                        "trans_values": "화이트，핑크，블루，블랙"
                    }
                ]
            },
            "rules": "1 개 ₩37,900，2 개 ₩43,900，3 개 ₩48,900",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001885211"
        },
        "duration": 43.2438850402832,
        "memory": "988.55 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 699,
            "price": "998.00",
            "product_id": 535511,
            "product_name": "蕾丝中腰镂空内裤",
            "logo_url": "https://oss.giikin.cn/uploads/e2cdc909a8d70413e20bb25b9fc4e4f2.jpg",
            "areaId": 13,
            "currency": "泰铢",
            "currencyId": 16,
            "lang_id": 8,
            "language": "泰语",
            "area": "火凤凰家族-泰国",
            "sale_id": 1001785211,
            "currencyCode": "THB",
            "symbol": "฿",
            "lang_code": "TH",
            "currency_id": 16,
            "area_id": 13,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "紫色，黑色，粉色，银灰，肤色，酒红，深蓝，浅咖色"
                    },
                    {
                        "name": "尺码",
                        "values": "M，L，XL，XXL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "สี",
                        "trans_values": "สีม่วง，ดำ，สีชมพู，สีเทาเงิน，ผิวหนัง，ไวน์แดง，น้ำเงิน，สีน้ำตาลอ่อน"
                    },
                    {
                        "trans_name": "ขนาด",
                        "trans_values": "M，L，XL，2XL"
                    }
                ]
            },
            "rules": "3 ตัว ฿699，6 ตัว ฿899，9 ตัว ฿1099",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001785211"
        },
        "duration": 51.89204216003418,
        "memory": "989.52 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 799,
            "price": "999.00",
            "product_id": 198607,
            "product_name": "指甲剪修16件套",
            "logo_url": "https://oss.giikin.cn/ueditor/20210126/5be9c3884c72caa24d7f165dcd81ba18.jpg",
            "areaId": 57,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "雪豹家族-运营5组",
            "sale_id": 1001785311,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 57,
            "options": {
                "chinese": [
                    {
                        "name": "尺码",
                        "values": "灰色，蓝色，深棕色，咖啡色拉链包 20件套，7022D咖啡色（升级版），7022D蓝色（升级版）"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Gray，Blue，Dark brown，20，Coffee"
                    }
                ]
            },
            "rules": "1 piece₱ 799，2 pieces₱ 1199",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001785311"
        },
        "duration": 45.33886909484863,
        "memory": "988.57 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 5280,
            "price": "10560.00",
            "product_id": 605107,
            "product_name": "JS-满钻水桶包",
            "logo_url": "https://oss.giikin.cn/uploads/218c51cd48f3c4f54d771eec4c598843.jpg",
            "areaId": 98,
            "currency": "日币",
            "currencyId": 9,
            "lang_id": 3,
            "language": "日语",
            "area": "金狮-日本",
            "sale_id": 1001781311,
            "currencyCode": "JPY",
            "symbol": "￥",
            "lang_code": "JP",
            "currency_id": 9,
            "area_id": 98,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "银色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "カラー",
                        "trans_values": "シルバー"
                    }
                ]
            },
            "rules": "2点目半額 期間限定",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781311"
        },
        "duration": 65.88006019592285,
        "memory": "988.26 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 1299,
            "price": "1999.00",
            "product_id": 603655,
            "product_name": "JS-垂感显瘦优雅休闲裤",
            "logo_url": "https://oss.giikin.cn/uploads/3e047e00ba90a03e64894f78aa033cec.png",
            "areaId": 115,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "红杉-菲律宾",
            "sale_id": 1001781211,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 115,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "白色，卡其色，红色，绿色，黑色"
                    },
                    {
                        "name": "尺码",
                        "values": "XXL，XXXL，4XL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "White，Khaki，Red，Green，Black"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "2XL(40-55kg)，3XL(55-65kg)，4XL(65-80kg)"
                    }
                ]
            },
            "rules": "1 piece ₱1299，2 pieces ₱1699",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781211"
        },
        "duration": 63.983917236328125,
        "memory": "989.33 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 31900,
            "price": "63800.00",
            "product_id": 122332,
            "product_name": "男士时尚短袖衫",
            "logo_url": "https://oss.giikin.cn/uploads/237145d8f3517d695471c02229a5760c.jpg",
            "areaId": 187,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "火凤凰-韩国",
            "sale_id": 1001781210,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 187,
            "options": {
                "chinese": [
                    {
                        "name": "顏色",
                        "values": "白色，黑色，灰色，紅色，雅蘭色，果綠色，草绿色，深藍色，粉色，黄色，藏青"
                    },
                    {
                        "name": "男士尺碼",
                        "values": "S，M，L，XL，2XL，3XL，4XL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "컬러",
                        "trans_values": "화이트，블랙，그레이，레드，블루，그린，초록색，다크 블루，핑크，옐로우，네이비"
                    },
                    {
                        "trans_name": "사이즈",
                        "trans_values": "S（45-50kg），M（50-60kg），L（60-70kg），XL（70-80kg），2XL（80-90kg），3XL（90-95kg），4XL（95-100kg）"
                    }
                ]
            },
            "rules": "1 벌 ₩31,900，2 벌 ₩41,900，4 벌 ₩59,900",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781210"
        },
        "duration": 43.745994567871094,
        "memory": "989.62 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 1899,
            "price": "3599.00",
            "product_id": 1000024,
            "product_name": "X22052601Ja-阔腿裤含腰带连体衣",
            "logo_url": "www.bing.com",
            "areaId": 184,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "雪豹运营中心",
            "sale_id": 1001781110,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 184,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黑色，酒红色，军绿色，深蓝色"
                    },
                    {
                        "name": "尺码",
                        "values": "S，M，L，XL，XXL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "black，wine，army green，dark blue"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "S，M，L，XL，2XL"
                    }
                ]
            },
            "rules": "1 piece 1899，2 pieces 2799",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781110"
        },
        "duration": 70.3129768371582,
        "memory": "989.21 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 950,
            "price": "1849.00",
            "product_id": 604165,
            "product_name": "X2022050903Gc-懒人省力铺床床垫抬高器",
            "logo_url": "www.bing.com",
            "areaId": 34,
            "currency": "台币",
            "currencyId": 13,
            "lang_id": 2,
            "language": "繁体中文",
            "area": "飞马家族-泰国",
            "sale_id": 1001781810,
            "currencyCode": "NTD",
            "symbol": "NT$",
            "lang_code": "TW",
            "currency_id": 13,
            "area_id": 34,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "两个装"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "顏色",
                        "trans_values": "兩個裝"
                    }
                ]
            },
            "rules": "一套2個950，加400再得2個",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781810"
        },
        "duration": 69.12803649902344,
        "memory": "988.27 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 42900,
            "price": "85800.00",
            "product_id": 518511,
            "product_name": "X20122105S-U型礼服隐形内衣",
            "logo_url": "https://oss.giikin.cn/uploads/0514f46388068e6801f7471cf8acd125.jpg",
            "areaId": 21,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "金牛家族-韩国",
            "sale_id": 1001781890,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 21,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "白色，黑色，藕肤色"
                    },
                    {
                        "name": "尺码",
                        "values": "S(适合32/70ABC），M(适合34/75ABC），L(适合36/80ABC），XL(适合38/85ABC），XXL(适合40/90ABC），xxxl"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "색상",
                        "trans_values": "화이트，블랙，베이지"
                    },
                    {
                        "trans_name": "사이즈",
                        "trans_values": "S，M，L，XL，2XL，3XL"
                    }
                ]
            },
            "rules": "₩42,900/2장，₩49,900/3장，₩55,900/4장",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001781890"
        },
        "duration": 100.01897811889648,
        "memory": "989.48 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 99,
            "price": "990.00",
            "product_id": 605318,
            "product_name": "HFH-德国多功能俯卧撑训练板",
            "logo_url": "https://oss.giikin.cn/uploads/53124eed20f8e8bee868adb72b64f23b.jpg",
            "areaId": 130,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "火凤凰-英语",
            "sale_id": 1001788890,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 130,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "22种+收纳包【不包胶手柄】"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Multifunctional push-up board"
                    }
                ]
            },
            "rules": "RM99 for 1 set，RM139 for 2 sets",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001788890"
        },
        "duration": 79.95891571044922,
        "memory": "988.45 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 249,
            "price": "830.00",
            "product_id": 606052,
            "product_name": "JS-高端手作质感大容量妈妈手提包",
            "logo_url": "https://oss.giikin.cn/uploads/2b4a93062d423ccd01f17b5acfa69fa4.png",
            "areaId": 16,
            "currency": "阿联酋迪拉姆",
            "currencyId": 1,
            "lang_id": 9,
            "language": "阿语",
            "area": "金狮家族-阿联酋",
            "sale_id": 1001788880,
            "currencyCode": "AED",
            "symbol": "درهم",
            "lang_code": "AR",
            "currency_id": 1,
            "area_id": 16,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "酒红色，绿色，黑色，黄棕色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "لون",
                        "trans_values": "أحمر داكن，اخضر，اسود，بني أصفر"
                    }
                ]
            },
            "rules": "AED 249 x 1，AED 199.5 x 2",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001788880"
        },
        "duration": 37.693023681640625,
        "memory": "988.54 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 4480,
            "price": "8960.00",
            "product_id": 559411,
            "product_name": "男士短袖POLO衫",
            "logo_url": "https://oss.giikin.cn/uploads/1c501b1b5cba87714ab31f58fb0ed27b.jpg",
            "areaId": 98,
            "currency": "日币",
            "currencyId": 9,
            "lang_id": 3,
            "language": "日语",
            "area": "金狮-日本",
            "sale_id": 1001788888,
            "currencyCode": "JPY",
            "symbol": "￥",
            "lang_code": "JP",
            "currency_id": 9,
            "area_id": 98,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "白色，红色，黄色，灰色，黑色，宝兰"
                    },
                    {
                        "name": "尺码",
                        "values": "M，L，XL，XXL，XXXL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "カラー",
                        "trans_values": "ホワイト，レッド，イエロー，グレー，ブラック，ネイビー"
                    },
                    {
                        "trans_name": "サイズ",
                        "trans_values": "M(50-60kg)，L(60-70kg)，XL(70-75kg)，2XL(75-85kg)，3XL(85-90kg)"
                    }
                ]
            },
            "rules": "当店独売り！1枚で4,480円，2枚で5,480円，3枚で6,480円",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001788888"
        },
        "duration": 47.05190658569336,
        "memory": "989.42 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 39900,
            "price": "66500.00",
            "product_id": 604538,
            "product_name": "JS-二合一刮刷专为边角窄缝清洁刷",
            "logo_url": "https://oss.giikin.cn/uploads/79275a097964360c970a768fc8c82845.jpg",
            "areaId": 187,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "火凤凰-韩国",
            "sale_id": 1001888888,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 187,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "橙色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "색상",
                        "trans_values": "오랜지"
                    }
                ]
            },
            "rules": "한 개 39900，두 개 45900，세 개 49900",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001888888"
        },
        "duration": 46.672821044921875,
        "memory": "988.44 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 279,
            "price": "930.00",
            "product_id": 576389,
            "product_name": "JS-男式机车胸包",
            "logo_url": "https://oss.giikin.cn/uploads/2b7330614e72999687f137e23e3de0a5.jpg",
            "areaId": 117,
            "currency": "沙特币",
            "currencyId": 14,
            "lang_id": 9,
            "language": "阿语",
            "area": "金狮-中东市场",
            "sale_id": 1001895221,
            "currencyCode": "SAR",
            "symbol": "ريال",
            "lang_code": "AR",
            "currency_id": 14,
            "area_id": 117,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黑色，黑棕"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "لون",
                        "trans_values": "اسود，اسود و بني"
                    }
                ]
            },
            "rules": "SAR 279 x 1，SAR 148 x 2",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895221"
        },
        "duration": 37.850141525268555,
        "memory": "988.37 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 65,
            "price": "119.00",
            "product_id": 139684,
            "product_name": "竹節高升手鐲",
            "logo_url": "https://oss.giikin.cn/ueditor/20180921/b25faed56e18bbf90077a556835cac33.jpg",
            "areaId": 22,
            "currency": "新加坡",
            "currencyId": 15,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮家族-新加坡",
            "sale_id": 1001895222,
            "currencyCode": "SGD",
            "symbol": "S$",
            "lang_code": "EN",
            "currency_id": 15,
            "area_id": 22,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "竹节镯子"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Bamboo Bracelet"
                    }
                ]
            },
            "rules": "1 for S$65，2 for S$75",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895222"
        },
        "duration": 33.766984939575195,
        "memory": "988.35 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 35,
            "price": "175.00",
            "product_id": 1001493,
            "product_name": "HFH-高品质方领吊带连衣裙",
            "logo_url": "https://oss.giikin.cn/uploads/738a34f59aedcf3f7b10893977bd5386.jpg",
            "areaId": 22,
            "currency": "新加坡",
            "currencyId": 15,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮家族-新加坡",
            "sale_id": 1001895223,
            "currencyCode": "SGD",
            "symbol": "S$",
            "lang_code": "EN",
            "currency_id": 15,
            "area_id": 22,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黑色，蓝色，香槟，桃红"
                    },
                    {
                        "name": "尺码",
                        "values": "4XL，S，M，L，XL，2XL，3XL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Black，Blue，Champagne，Red"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "4XL(72-80kg)，S(40-47kg)，M(47-52kg)，L(52-57kg)，XL(57-62kg)，2XL(62-67kg)，3XL(67-72kg)"
                    }
                ]
            },
            "rules": "Only S$35，Buy 1 Free 1  S$45，3 for S$55",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895223"
        },
        "duration": 31.248092651367188,
        "memory": "989.48 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 44900,
            "price": "449000.00",
            "product_id": 600734,
            "product_name": "JS-大容量宽肩带复古女包",
            "logo_url": "https://oss.giikin.cn/uploads/23c6cd033df85014cbda6eefb02d718e.jpg",
            "areaId": 137,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "神龙-韩国",
            "sale_id": 1001895226,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 137,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黄色，褐色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "색상",
                        "trans_values": "옐로우，브라운"
                    }
                ]
            },
            "rules": "+₩14,900원 하나 더!",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895226"
        },
        "duration": 32.20200538635254,
        "memory": "988.32 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 29,
            "price": "145.00",
            "product_id": 583882,
            "product_name": "神经诱导素鱼饵料",
            "logo_url": "https://oss.giikin.cn/uploads/81f3fd95dff7ef9d0d2356f06e324450.jpg",
            "areaId": 159,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "客服中心-新马菲",
            "sale_id": 1001895228,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 159,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "100ml"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "100ml"
                    }
                ]
            },
            "rules": "5 piece for RM29，10 piece for RM49",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895228"
        },
        "duration": 35.813093185424805,
        "memory": "988.34 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 99,
            "price": "179.00",
            "product_id": 1001137,
            "product_name": "X22060905Ac-强磁彩钻消肿耳钉",
            "logo_url": "https://oss.giikin.cn/uploads/f8673c39a30b538c904a6a92b3c6fa7d.jpg",
            "areaId": 55,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "雪豹家族-运营3组",
            "sale_id": 1001895229,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 55,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "磁铁宝蓝钻，磁铁透明白钻，磁铁香槟钻，磁铁黑色钻"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Magnet sapphire blue rhinestone ，Magnet transparent white rhinestone ，Magnet champagne rhinestone ，Magnet black rhinestone "
                    }
                ]
            },
            "rules": "Limited time 2 pairs 99，Great value 4 pairs 139",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895229"
        },
        "duration": 40.85993766784668,
        "memory": "988.65 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 269,
            "price": "2990.00",
            "product_id": 534911,
            "product_name": "X21041201X-便捷式手持挂烫机",
            "logo_url": "https://oss.giikin.cn/ueditor/1688/20210104/ENdLyRz8p0Gb8IGy6O0B888i0dnDFfYl.jpeg",
            "areaId": 117,
            "currency": "沙特币",
            "currencyId": 14,
            "lang_id": 9,
            "language": "阿语",
            "area": "金狮-中东市场",
            "sale_id": 1001895220,
            "currencyCode": "SAR",
            "symbol": "ريال",
            "lang_code": "AR",
            "currency_id": 14,
            "area_id": 117,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "墨绿色"
                    },
                    {
                        "name": "尺码",
                        "values": "欧规-220v"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "اللون ",
                        "trans_values": "أخضر داكن"
                    },
                    {
                        "trans_name": "المقاس",
                        "trans_values": "المعيار الاوروبي"
                    }
                ]
            },
            "rules": "احصل على 1 قطعة بسعر 269 ريال，احصل على 2 قطعة بسعر 360 ريال",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895220"
        },
        "duration": 33.02001953125,
        "memory": "989.45 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 3999,
            "price": "7998.00",
            "product_id": 583247,
            "product_name": "HS-防砸防刺穿工作鞋",
            "logo_url": "https://oss.giikin.cn/uploads/19a3412cadb2bcf2b80b7bbb3598d7b3.jpg",
            "areaId": 1,
            "currency": "日币",
            "currencyId": 9,
            "lang_id": 3,
            "language": "日语",
            "area": "精灵家族-日本",
            "sale_id": 1001895233,
            "currencyCode": "JPY",
            "symbol": "￥",
            "lang_code": "JP",
            "currency_id": 9,
            "area_id": 1,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黄色，绿色，橘黄，黄色加绒，橙色加绒，绿色加绒"
                    },
                    {
                        "name": "规格",
                        "values": "39，40，41，42，43，44"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "カラー",
                        "trans_values": "イエロー，グリーン，オレンジ，裏起毛イエロー，裏起毛オレンジ，裏起毛グリーン"
                    },
                    {
                        "trans_name": "サイズ",
                        "trans_values": "24.5，25，25.5，26，26.5，27"
                    }
                ]
            },
            "rules": "2足目半額",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895233"
        },
        "duration": 56.118011474609375,
        "memory": "989.35 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 1299,
            "price": "6495.00",
            "product_id": 548302,
            "product_name": "X21060801EC-按扣五爪扣钳子纽扣套装",
            "logo_url": "https://oss.giikin.cn/uploads/ccbb18757850fb1e42fa7bfa09af62cf.jpg",
            "areaId": 56,
            "currency": "菲律宾",
            "currencyId": 20,
            "lang_id": 4,
            "language": "英语",
            "area": "雪豹家族-运营4组",
            "sale_id": 1001895234,
            "currencyCode": "PHP",
            "symbol": "₱",
            "lang_code": "EN",
            "currency_id": 20,
            "area_id": 56,
            "options": {
                "chinese": [
                    {
                        "name": "尺码",
                        "values": "盒装100套五爪扣（空心10色各5套+实心10色各5套）+工具+说明书飞机盒"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Specifications",
                        "trans_values": "Boxed 100 sets of 5-claw buttons (Hollow: 5 sets for each of 10 colors + Solid: 5 sets for each of 10 colors) + tools + manual airplane box"
                    }
                ]
            },
            "rules": "1 set ₱1299，2 sets ₱1799",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895234"
        },
        "duration": 31.405925750732422,
        "memory": "988.67 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 21900,
            "price": "32600.00",
            "product_id": 221373,
            "product_name": "包头女鞋",
            "logo_url": "https://oss.giikin.cn/ueditor/20200910/f67dff93609a5533d6575f9d08728b3b.jpg",
            "areaId": 194,
            "currency": "匈牙利福林",
            "currencyId": 36,
            "lang_id": 18,
            "language": "匈牙利语",
            "area": "神龙-匈牙利",
            "sale_id": 1001895235,
            "currencyCode": "HUF",
            "symbol": "Ft",
            "lang_code": "HU",
            "currency_id": 36,
            "area_id": 194,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "绿色，蓝色，棕色，红棕，Foot stick"
                    },
                    {
                        "name": "尺码",
                        "values": "35，36，37，38，39，40，41，42，43"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Színe",
                        "trans_values": "Zöld，Kék，Barna，Vörös barna， Foot stick"
                    },
                    {
                        "trans_name": "Méretet",
                        "trans_values": "35，36，37，38，39，40，41，42，43"
                    }
                ]
            },
            "rules": "1 darab 21 900 Ft，2 darab 31 900 Ft",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895235"
        },
        "duration": 49.527883529663086,
        "memory": "989.48 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 99,
            "price": "198.00",
            "product_id": 584583,
            "product_name": "大容量手提折叠防水收纳包",
            "logo_url": "https://oss.giikin.cn/uploads/7be9710dc38f29ef429a98604c934f0b.jpg",
            "areaId": 130,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "火凤凰-英语",
            "sale_id": 1001895236,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 130,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "001#黑色，001#粉色，001#藏蓝色，001#浅蓝色，001#紫色，001#绿色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Black，Pink，Tibetan blue，Light blue，Purple，Green"
                    }
                ]
            },
            "rules": "RM99 for 1 piece，RM149 for 2 pieces",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895236"
        },
        "duration": 33.73908996582031,
        "memory": "988.55 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 42000,
            "price": "70000.00",
            "product_id": 592734,
            "product_name": "sl-冰丝休闲裤男",
            "logo_url": "https://oss.giikin.cn/uploads/a35f041ff653c430297f9084379d96ca.jpg",
            "areaId": 137,
            "currency": "韩元",
            "currencyId": 10,
            "lang_id": 5,
            "language": "韩语",
            "area": "神龙-韩国",
            "sale_id": 1001895238,
            "currencyCode": "KRW",
            "symbol": "₩",
            "lang_code": "KR",
            "currency_id": 10,
            "area_id": 137,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "浅灰色，深灰色，黑色，绿色"
                    },
                    {
                        "name": "尺码",
                        "values": "4XL，5XL，M，L，XL，XXL，XXXL"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "색상",
                        "trans_values": "라이트 그레이，다크 그레이，블랙，그린"
                    },
                    {
                        "trans_name": "사이즈",
                        "trans_values": "4XL，5XL，M，L，XL，2XL，3XL"
                    }
                ]
            },
            "rules": "₩42,000/2벌 ，₩49,000/3벌 ，₩55,000/4벌 ",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895238"
        },
        "duration": 38.37299346923828,
        "memory": "989.4 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 899,
            "price": "1899.00",
            "product_id": 1001649,
            "product_name": " 美容美體健身腿部頸椎按摩狼牙棒",
            "logo_url": "www.bing.com",
            "areaId": 17,
            "currency": "台币",
            "currencyId": 13,
            "lang_id": 2,
            "language": "繁体中文",
            "area": "神龙家族-港澳台",
            "sale_id": 1001895250,
            "currencyCode": "NTD",
            "symbol": "NT$",
            "lang_code": "TW",
            "currency_id": 13,
            "area_id": 17,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "粉色，蓝色，紫色"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "顏色",
                        "trans_values": "粉色，藍色，紫色"
                    }
                ]
            },
            "rules": "【今日限定】$899買一送一，【超夯活動】$1099三入，【狂殺特賣】$1299四入",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895250"
        },
        "duration": 33.71000289916992,
        "memory": "988.37 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 269,
            "price": "899.00",
            "product_id": 597452,
            "product_name": "JS-牛皮舒适镂空妈妈粗跟鞋",
            "logo_url": "https://oss.giikin.cn/uploads/c2a7c6f22e8cb8d39b14b201053393b6.jpg",
            "areaId": 117,
            "currency": "沙特币",
            "currencyId": 14,
            "lang_id": 9,
            "language": "阿语",
            "area": "金狮-中东市场",
            "sale_id": 1001895256,
            "currencyCode": "SAR",
            "symbol": "ريال",
            "lang_code": "AR",
            "currency_id": 14,
            "area_id": 117,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "灰色，棕色"
                    },
                    {
                        "name": "尺码",
                        "values": "36，37，38，39，40，35"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "لون",
                        "trans_values": "رمادي，بني"
                    },
                    {
                        "trans_name": "مقاس",
                        "trans_values": "36，37，38，39，40，35"
                    }
                ]
            },
            "rules": "SAR 269 x 1，SAR 199.5 x 2",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895256"
        },
        "duration": 38.44785690307617,
        "memory": "989.36 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 119,
            "price": "238.00",
            "product_id": 1000590,
            "product_name": "HFH-冰丝华夫格休闲套装",
            "logo_url": "https://oss.giikin.cn/uploads/b15d17de9c3365a0fa75712a382db8d9.jpg",
            "areaId": 94,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "火凤凰-马来西亚",
            "sale_id": 1001895259,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 94,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "黑色，杏色，灰杏色，彩蓝色，藏青色，白色，橘色，灰色"
                    },
                    {
                        "name": "尺码",
                        "values": "XL，2XL，3XL，4XL，5XL，M，L"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "black，apricot，Grey Apricot，blue，navy，white，orange，gray"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "XL(65-75kg)，2XL(75-85kg)，3XL(85-95kg)，4XL(95-105kg)，5XL(105-115kg)，M(45-55kg)，L(55-65kg)"
                    }
                ]
            },
            "rules": "1 Set for RM119，2 Sets for RM169",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895259"
        },
        "duration": 42.62709617614746,
        "memory": "989.56 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 29,
            "price": "48.00",
            "product_id": 571029,
            "product_name": "SL-防蓝光抗疲劳显年轻远近两用高档眼镜",
            "logo_url": "https://oss.giikin.cn/uploads/61b516533f2f09522c906a6e7a0fb22d.jpg",
            "areaId": 22,
            "currency": "新加坡",
            "currencyId": 15,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮家族-新加坡",
            "sale_id": 1001895266,
            "currencyCode": "SGD",
            "symbol": "S$",
            "lang_code": "EN",
            "currency_id": 15,
            "area_id": 22,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "红色，紫色，黑色，茶色"
                    },
                    {
                        "name": "规格",
                        "values": "100度，150度，200度，250度，300度，350度，400度"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "red，purple，Black，Sand tea"
                    },
                    {
                        "trans_name": "Specification",
                        "trans_values": "+100°(Under 45)，+150°(45-50Years old)，+200°(50-55Years old)，+250°(55-60Years old)，+300°(60-65Years old)，+350°(65-70Years old)，+400°(Above 70 years old)"
                    }
                ]
            },
            "rules": "【Buy 1 free 1】2 for S$29，【Buy 2 free 2】4 for S$39",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895266"
        },
        "duration": 35.42590141296387,
        "memory": "989.65 kb"
    },
    {
        "code": 0,
        "comment": "",
        "data": {
            "special_price": 79,
            "price": "395.00",
            "product_id": 1001857,
            "product_name": "JS天然莫代尔睡裙",
            "logo_url": "https://oss.giikin.cn/uploads/7de886a5a467df42caa04a5b2c6195bd.jpg",
            "areaId": 14,
            "currency": "马来西亚",
            "currencyId": 12,
            "lang_id": 4,
            "language": "英语",
            "area": "金狮家族-马来西亚",
            "sale_id": 1001895288,
            "currencyCode": "MYR",
            "symbol": "RM",
            "lang_code": "EN",
            "currency_id": 12,
            "area_id": 14,
            "options": {
                "chinese": [
                    {
                        "name": "颜色",
                        "values": "粉色，黄色，黑色，橘色，灰色，墨绿色，玫红色，蓝色"
                    },
                    {
                        "name": "尺码",
                        "values": "S，M，L，XL，XXL，XXXL，4xl"
                    }
                ],
                "trans": [
                    {
                        "trans_name": "Color",
                        "trans_values": "Pink，Yellow，Black，Orange，Gray，Dark green，Rose red，Blue"
                    },
                    {
                        "trans_name": "Size",
                        "trans_values": "S，M，L（50-100kg），XL（100-150kg），2XL，3XL，4XL"
                    }
                ]
            },
            "rules": "Only RM79，Buy 1 Free 1 RM109，3 for RM129",
            "currencyList": [],
            "isMultiCurrency": 0
        },
        "service": "inner.sale",
        "action": "getSaleInfo",
        "request": {
            "service": "inner.sale",
            "action": "getSaleInfo",
            "t": "1656312415",
            "token": "d3b9d87e7873363321022493025a5cfa52284c32",
            "appKey": "intent",
            "sale_id": "1001895288"
        },
        "duration": 36.64112091064453,
        "memory": "989.5 kb"
    }
]

goodsstore = [
    # goods   price   rules  size -  color - gcode
    {'电视机-1': [100, '买一送一', 11, '红色', 'aaaaa111']},
    {'电视机-2': [200, '买二送一', 22, '黑色', 'bbbbb222']},
    {'工作鞋': [300, '买三送一', 33, '黄色', 'ccccc333']},
    {'洗发精': [400, '买四送一', 44, '褐色', 'dddddd444']},
    {'运动袜': [500, '买五送一', 55, '蓝色', 'eeeee555']},
    {'收纳包': [600, '买六送一', 66, '绿色', 'fffff666']},
    {'汽车-1': [700, '买七送一', 77, '灰色', 'ggggg777']},
    {'汽车-2': [800, '买八送一', 88, '蓝色', 'hhhhh888']},
    {'汽车-3': [900, '买九送一', 99, '白色', 'iiiiii999']},
]

orderlist = [
    # tell - goods -    status -   color - size - code - count - name
    {'545115564': ['鞋子', '商品准备打包', '红色', 6, 'GT1111', 10, 'zs']},
    {'151651515': ['衣服-1', '商品准备打包', '红色', 9, 'GT2222', 10, 'ls']},
    {'152325622': ['衣服-2', '商品正在派送', '黑色', 8, 'GT3333', 11, 'ww']},
    {'322323244': ['帽子', '商品正在派送', '黄色', 7, 'GT4444', 22, 'op']},
    {'156215563': ['手机', '商品准备打包', '绿色', 9, 'GT5555', 33, 'gg']},
    {'897454123': ['裙子', '商品正在退货', '粉红', 10, 'GT6666', 44, 'mm']},
    {'666688888': ['音樂盒', '商品正在退货', '白色', 11, 'GT7777', 55, 'dd']}
]


class CleanSlot(Action):
    """
    检查用户来自商品落地页：此时可以从商品库中完成关键信息的填充
    检查用户直接进入 line，此时需要更多的实体识别工作
    """

    def name(self) -> Text:
        return "action_clean_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]


class SetGoodsPageInfoToSlot(Action):
    """
    检查用户来自商品落地页：此时可以从商品库中完成关键信息的填充
    检查用户直接进入 line，此时需要更多的实体识别工作
    """

    def name(self) -> Text:
        return "action_check_where_user_come_from"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        random_float = random.random()
        if random_float > 10:  # input line directly
            # if random_float <= 0.99:  # from  goods page
            # fixme 商品库中商品信息的解析，这里需要一个来自商品详情页的指示信息
            all_goods_info = random.choice(demo_data_list)
            sgoods_slot = all_goods_info['data']['product_name']
            ssize_slot = str(all_goods_info['data']['options'])
            price = all_goods_info['data']['price']
            rules = all_goods_info['data']['rules']
            sprice_slot = price + '。更多價格優惠活動：' + rules + "。"
            # print('goods_information_product_name: ', goods_information_product_name)
            return [
                SlotSet('sprice_slot', sprice_slot),
                SlotSet('sgoods_slot', sgoods_slot),
                SlotSet('ssize_slot', ssize_slot)
            ]
        else:
            # name = next(tracker.get_latest_entity_values('name'), None)
            # print("name: ", name)
            # phone = next(tracker.get_latest_entity_values('phone'), None)
            # print("phone: ", phone)
            goods = next(tracker.get_latest_entity_values('goods'), None)
            print("goods: ", goods)
            gcode = next(tracker.get_latest_entity_values('gcode'), None)
            print("gcode: ", gcode)
            logo = next(tracker.get_latest_entity_values('logo'), None)
            print("logo: ", logo)
            attr = next(tracker.get_latest_entity_values('attr'), None)
            print("attr: ", attr)
            color = next(tracker.get_latest_entity_values('color'), None)
            print("color: ", color)
            count_ = next(tracker.get_latest_entity_values('count'), None)
            print("count: ", count_)
            price = next(tracker.get_latest_entity_values('price'), None)
            print("price: ", price)
            city = next(tracker.get_latest_entity_values('city'), None)
            print("city: ", city)
            part = next(tracker.get_latest_entity_values('part'), None)
            print("part: ", part)
            street = next(tracker.get_latest_entity_values('street'), None)
            print("street: ", street)
            print('*' * 10)
            if goods:  # 直接进入line发送了商品需求信息
                return [
                    # SlotSet('goods_slot', goods),
                    SlotSet('logo_slot', logo),
                    SlotSet('gcode_slot', gcode),
                    SlotSet('attr_slot', attr),
                    SlotSet('color_slot', color),
                    SlotSet('count_slot', count_)
                ]
            else:  # Nothing
                return [SlotSet('nothing_slot', True)]


class OutOfScopeHowUse(Action):
    def name(self) -> Text:
        return "action_howuse_outofscope"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # goods = next(tracker.get_latest_entity_values('goods'), None)

        # 如果 None，说明用户没有提供任何信息就在寻求商品的使用方式；
        sgoods = tracker.get_slot('sgoods_slot')
        goods = tracker.get_slot('goods_slot')
        if sgoods is not None:
            # fixme 需要把固定话术的答复配置在这里
            dispatcher.utter_message(text=f"我想您是需要了解商品：{sgoods}的具體特性 / 使用方法 / 質量保證。\n"
                                          f"1. 如果您是需要了解商品的使用方法，我們會為您的商品附送商品使用說明，您可以閱讀該文檔了解商品的使用方法。\n"
                                          f"2. 如果您是需要了解產品的性質，某些特定商品的使用因人而異，但是我可以為您保證我們的商品均具備完整的質量檢測證明。\n"
                                          f"同時我們為您提供了完善的售後服務，在您收到商品之後您有7天鑒賞期以供您決定該商品是否適合您。\n"
                                          f"所以您可以放心購買，期待您收到心儀的商品的那一天。")
            return []
        if goods is not None:
            dispatcher.utter_message(text=f"我想您是需要了解商品：{goods}的具體特性 / 使用方法 / 質量保證。\n"
                                          f"1. 如果您是需要了解商品的使用方法，我們會為您的商品附送商品使用說明，您可以閱讀該文檔了解商品的使用方法。\n"
                                          f"2. 如果您是需要了解產品的性質，某些特定商品的使用因人而異，但是我可以為您保證我們的商品均具備完整的質量檢測證明。\n"
                                          f"同時我們為您提供了完善的售後服務，在您收到商品之後您有7天鑒賞期以供您決定該商品是否適合您。\n"
                                          f"所以您可以放心購買，期待您收到心儀的商品的那一天。")
            return []
        else:
            dispatcher.utter_message(response="utter_welcome_nothing")
            return []


class FindGoodsWithGoodsSlotToGetPrice(Action):
    def name(self) -> Text:
        # 这个操作也可以当作是根据 goods name 去商品库找到更多相关商品详情的过程
        return "action_find_goods_in_database_to_get_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        goods = tracker.get_slot('goods_slot')
        relate_goods_list = []
        for i in goodsstore:
            if goods in list(i.keys())[0]:
                relate_goods_list.append(i)
        if len(relate_goods_list) != 0:
            dispatcher.utter_message(text=f'通過您提供的{goods}關鍵字信息,我幫您查詢到如下商品信息：\n'
                                          f'{relate_goods_list}\n'
                                          f'如果您喜歡这款商品，您可以告知我姓名電話地址數量規格，我可以幫您下單喔可以為您優先出貨呢。')
            return []
        else:
            dispatcher.utter_message(text=f'很抱歉，通過您提供的{goods}關鍵字信息,我沒有幫助您查詢到任何相關的產品信息。')
            return []


# ==============================================  Cancel Order  OK

class RequestCancelOrder(Action):
    def name(self) -> Text:
        return "action_find_orders_and_survey"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[
        Dict[Text, Any]]:
        phone = tracker.get_slot("phone_slot")
        print(phone)

        # fixme 数据库操作 - 查询用户相关订单
        # connection = sqlite3.connect(path_to_db)
        # cursor = connection.cursor()
        # cursor.execute("SELECT * FROM orders WHERE tellnumber=?", tell_entity)
        # orderlist = cursor.fetchall()
        user_orders = []
        for each_order in orderlist:
            if phone in list(each_order.keys())[0]:
                user_orders.append(each_order)
        print(user_orders, '*' * 10, len(user_orders))
        # fixme 需要明确订单的数量；做订单筛选然后返回
        if len(user_orders) != 0:
            # dispatcher.utter_message(response='utter_give_user_order_info', order_list=user_orders)
            return [SlotSet('order_list', user_orders), SlotSet('there_is_order_slot', True)]
        else:
            return [SlotSet('there_is_order_slot', False)]


class MakeSureCancelOrder(Action):
    def name(self) -> Text:
        return "action_submit_survey_cancel_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[
        Dict[Text, Any]]:
        users_order = tracker.get_slot('order_list')
        phone = tracker.get_slot('phone_slot')
        order_status = users_order[0].get(phone)[1]
        if order_status == '商品正在派送':
            return [SlotSet('there_is_order_slot_can_cancel', False)]
        else:
            return [SlotSet('there_is_order_slot_can_cancel', True)]


class MakeSureCancelOrderFinal(Action):
    def name(self) -> Text:
        return "action_submit_survey_cancel_form_final"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[
        Dict[Text, Any]]:
        # intent = tracker.latest_message['intent'].get('name')
        open_sure_cancel_feedback = tracker.get_slot('open_sure_cancel_feedback')
        # print(open_sure_cancel_feedback)
        if open_sure_cancel_feedback == '确需取消' or open_sure_cancel_feedback == '確需取消':
            # fixme 数据库操作 - 更新用户订单信息，设置为取消状态
            dispatcher.utter_message(response='utter_achieve_cancel')
            return []
        if open_sure_cancel_feedback == '暂不取消' or open_sure_cancel_feedback == '暫不取消':
            dispatcher.utter_message(response='utter_stop_cancel')
            return []


# ===================================================== Check Order OK

class RequestCheckOrderStatus(Action):
    def name(self) -> Text:
        return "action_check_orders_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = tracker.get_slot('phone_slot')
        print(phone)
        user_orders = []
        for each_order in orderlist:
            if phone in list(each_order.keys())[0]:
                user_orders.append(each_order)
        if len(user_orders) != 0:
            return [SlotSet('order_list', user_orders), SlotSet('have_order_need_change', True)]
        else:
            return [SlotSet('have_order_need_change', False)]


class GetOrderCheckAnswer(Action):
    def name(self) -> Text:
        return "action_get_check_order_answer_from_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # check_answer = tracker.latest_message['intent'].get('name')
        check_answer = tracker.get_slot('open_order_check_answer_feedback')
        print(check_answer)
        if check_answer == "確認無誤" or check_answer == '确认无误':
            return [SlotSet('condition_do_not_need_change_order', True)]
        if check_answer == '訂單修正' or check_answer == '订单修正':
            return [SlotSet('condition_do_not_need_change_order', False)]


class SetNewOrderName(Action):
    def name(self) -> Text:
        return "action_get_new_order_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_order_name = tracker.get_slot('open_new_order_name_feedback')
        if new_order_name is not None:
            dispatcher.utter_message(text=f'感謝，我已經記錄了您新訂單的姓名：{new_order_name}。')
            # return [SlotSet('new_order_name', new_order_name)]
            return []
        else:
            dispatcher.utter_message(text=f'您輸入的新訂單信息的姓名信息好像有誤！')
            return []


class SetNewOrderPhone(Action):
    def name(self) -> Text:
        return "action_get_new_order_phone"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_order_phone = tracker.get_slot('open_new_order_phone_feedback')
        if new_order_phone is not None:
            dispatcher.utter_message(text=f'感謝，我已經記錄了您新訂單的電話：{new_order_phone}。')
            # return [SlotSet('new_order_phone', new_order_phone)]
            return []
        else:
            dispatcher.utter_message(text=f'您輸入的新訂單信息的電話信息好像有誤！')
            return []


class SetNewOrderAddress(Action):
    def name(self) -> Text:
        return "action_get_new_order_address"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_order_address = tracker.get_slot('open_new_order_address_feedback')
        if new_order_address is not None:
            dispatcher.utter_message(text=f'感謝，我已經記錄了您新訂單的地址：{new_order_address}。')
            # return [SlotSet('new_order_address', new_order_address)]
            return []
        else:
            dispatcher.utter_message(text=f'您輸入的新訂單信息的地址信息好像有誤！')
            return []


class ChangeOrderInDatabase(Action):
    def name(self) -> Text:
        return "action_achieve_change_order_in_database"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # intent = tracker.latest_message['intent'].get('name')
        new_order_name = tracker.get_slot('open_new_order_name_feedback')
        new_order_phone = tracker.get_slot('open_new_order_phone_feedback')
        new_order_address = tracker.get_slot('open_new_order_address_feedback')
        # fixme 执行数据库中的订单修改操作
        dispatcher.utter_message(response='utter_achieve_change_order_in_database')
        return []


# = ====== 查询订单物流状态

class RequestOutOrderStatus(Action):
    def name(self) -> Text:
        return "action_get_express_out_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tell_entity = tracker.get_slot('phone_slot')
        # tell_entity = tracker.get_slot('receive_uer_phone_out')
        # patt = re.compile('\d+')
        # tell_entity = patt.findall(tell_entity)[0]
        print(tell_entity)
        user_orders = []
        for each_order in orderlist:
            if tell_entity in list(each_order.keys())[0]:
                user_orders.append(each_order)
        if len(user_orders) != 0:
            order_status = user_orders[0][tell_entity][1]
            if order_status == '商品正在派送':
                dispatcher.utter_message(response='utter_give_user_order_sending')
                return []
            else:
                dispatcher.utter_message(response='utter_give_user_order_other')
                return []
        else:
            dispatcher.utter_message(response='utter_no_orders')
            return []


class RequestBackOrderStatus(Action):
    def name(self) -> Text:
        return "action_get_express_back_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tell_entity = tracker.get_slot('phone_slot')
        # tell_entity = tracker.get_slot('receive_uer_phone_out')
        # patt = re.compile('\d+')
        # tell_entity = patt.findall(tell_entity)[0]
        print(tell_entity)
        user_orders = []
        for each_order in orderlist:
            if tell_entity in list(each_order.keys())[0]:
                user_orders.append(each_order)
        if len(user_orders) != 0:
            order_status = user_orders[0][tell_entity][1]
            if order_status == '商品正在退货':
                dispatcher.utter_message(response='utter_give_user_order_backing')
                return []
            else:
                dispatcher.utter_message(response='utter_give_user_no_order_backing')
                return []
        else:
            dispatcher.utter_message(response='utter_no_orders')
            return []
