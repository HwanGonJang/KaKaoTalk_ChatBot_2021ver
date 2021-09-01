from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create your views here.

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('/home/ubuntu/kakao/mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://campbase-cfe26-default-rtdb.firebaseio.com/'
})

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']


    dir = db.reference('Establishment/Carpentry')
    CNum = dir.get()['null']
    dir = db.reference('Establishment/Lobby')
    LNum = dir.get()['null']
    dir = db.reference('Establishment/Seminar')
    SNum = dir.get()['null']
    dir = db.reference('PrintData')
    PNum = dir.get()['Count']


    leftSpace = "=====잔여공간=====\n목공실: %d석\n로비: %d석\n세미나실: %d석\n3D 프린터: %d대" % (CNum, LNum, SNum, PNum)



    if return_str == '홈으로':
                return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': ""
                    }
                }],
                'quickReplies': [{
                    'label':'Camp51.9 정보',            #캠프 정보는 카카오톡 기능으로
                    'action': 'message',
                    'messageText': 'Camp51.9 정보'
                },
                {
                    'label': '예약하기',
                    'action': 'message',
                    'messageText': '예약하기'
                 },
                 {
                    'label': '행사 정보',               #카톡 기능
                    'action': 'message',
                    'messageText': '행사 정보'
                },
                {
                    'label': '개발 정보',               #카톡 기능
                    'action': 'message',
                    'messageText': '개발 정보'
                }
                ]
            }
        })

    elif return_str == '예약하기':
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '아래 정보를 선택해주세요.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '학생 및 교직원',
                        'action': 'message',
                        'messageText': '학생 및 교직원'
                    },
                    {
                        'label': '외부인',
                        'action': 'message',
                        'messageText': '외부인'
                    },
                    {
                        'label': '잔여 공간',
                        'action': 'message',
                        'messageText': '잔여 공간'
                    }
                ]
                }
            })
    elif return_str == '학생 및 교직원':
        infoNum = 0
        return JsonResponse(
        {
            "version": "2.0",
            "template": {
                "outputs": [
                {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": "로비",
                        "description": "로비(30석)을 예약합니다.",
                        "thumbnail": {
                            "imageUrl": "https://user-images.githubusercontent.com/33739448/108666856-77d5d000-751b-11eb-9283-77123258c2ac.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "로비 예약하기",
                            "messageText": "로비"
                            }
                        ]
                        },
                        {
                        "title": "목공실",
                        "description": "목공실(15석)을 예약합니다.",
                        "thumbnail": {
                            "imageUrl": "https://user-images.githubusercontent.com/33739448/108666860-7906fd00-751b-11eb-8c65-3bc8388f99d3.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "목공실 예약하기",
                            "messageText": "목공실"
                            }
                        ]
                        },
                        {
                        "title": "세미나실",
                        "description": "세미나실(12석)을 예약합니다.",
                        "thumbnail": {
                            "imageUrl": "https://user-images.githubusercontent.com/33739448/108666859-786e6680-751b-11eb-97d9-8b95423e6f14.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "세미나실 예약하기",
                            "messageText": "세미나실"
                            }
                        ]
                        },
                        {
                        "title": "3D 프린터",
                        "description": "3D프린터(8대)를 예약합니다.",
                        "thumbnail": {
                            "imageUrl": "https://user-images.githubusercontent.com/33739448/108666857-77d5d000-751b-11eb-97f1-72e2a87971ba.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "3D프린터 예약하기",
                            "messageText": "3D 프린터"
                            }
                        ]
                        },
                        {
                        "title": "레이저커터",
                        "description": "레이저커터를 예약합니다.",
                        "thumbnail": {
                            "imageUrl": "https://user-images.githubusercontent.com/33739448/108666854-76a4a300-751b-11eb-9457-27360f7a13e4.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "레이저커터 예약하기",
                            "messageText": "레이저커터"
                            }
                        ]
                        }
                    ]
                    }
                }
                ]
            }
            })

    elif return_str == '외부인':
        infoNum = 1
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '예약하실 공간 혹은 장비를 선택해주세요.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '3D 프린터(요금)',
                        'action': 'message',
                        'messageText': '3D 프린터(요금)'
                    },
                    {
                        'label': '레이저커터',
                        'action': 'message',
                        'messageText': '레이저커터'
                    },
                    {
                        'label': '공간예약',
                        'action': 'message',
                        'messageText': '공간예약'
                    }
                    ]
                }
            })

    elif return_str == '목공실':
        dir = db.reference('Establishment/Carpentry')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']

        if tmpNum > 0:
            dir.update({'null': tmpNum-1})
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약성공=======\n\n목공실이 예약되었습니다.\n예약코드: carn\n\n방문 등록 후에 이용해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })
        else:
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약공간부족=======\n\n예약에 실패했습니다.\n\n직접 방문한 후 >이용등록을 해주세요.'
                            }
                                                    }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

    elif return_str == '로비':
        dir = db.reference('Establishment/Lobby')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']

        if tmpNum > 0:
            dir.update({'null': tmpNum-1})
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약성공=======\n\n로비가 예약되었습니다.\n예약코드: lbrn\n\n방문 등록 후에 이용해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })
        else:
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약공간부족=======\n\n예약에 실패했습니다.\n\n직접 방문한 후 >이용등록을 해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

    elif return_str == '세미나실':
        dir = db.reference('Establishment/Seminar')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']

        if tmpNum > 0:
            dir.update({'null': tmpNum-1})
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약성공=======\n\n세미나실이 예약되었습니다.\n예약코드: smrn\n\n방문 등록 후에 이용해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })
        else:
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약공간부족=======\n\n예약에 실패했습니다.\n\n직접 방문한 후 >이용등록을 해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

    elif return_str == '컴퓨터실':
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '컴퓨터실은 현재 이용불가합니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == '3D 프린터':
        dir = db.reference('Establishment/Lobby')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']

        if tmpNum > 0:
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약성공=======\n\n3D프린터가 예약되었습니다.\n예약코드: dprn\n\n방문 등록 후에 이용해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

    elif return_str == '레이저커터':
        dir = db.reference('LaserData')
        tmpNum = dir.get()['Count']
        dir.update({'Count': tmpNum+1})
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '=======예약성공=======\n\n레이저커터가 예약되었습니다.\n예약코드: lcrn\n\n방문 등록 후에 이용해주세요.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

        

    elif return_str == '공간예약':
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '공간예약은 전화로 문의해주세요.\n전화번호:070-4675-3131'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == '잔여 공간':
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': leftSpace
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == '레이저커터(요금)':
        dir = db.reference('LaserData')
        tmpNum = dir.get()['Count']
        dir.update({'Count': tmpNum+1})

        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '=======예약성공=======\n\n레이저커터가 예약되었습니다.\n\n방문 등록 후에 이용해주세요.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == '3D 프린터(요금)':
        dir = db.reference('PrintData')
        print(dir.get()['Count'])
        tmpNum = dir.get()['Count']

        if tmpNum > 0:
            dir.update({'Count': tmpNum-1})

            for num in range(1, 9):
                if num == 1:
                    dir = db.reference('UserData/printNum : 1')
                    state = dir.get()['tmp']
                elif num == 2:
                    dir = db.reference('UserData/printNum : 2')
                    state = dir.get()['tmp']
                elif num == 3:
                    dir = db.reference('UserData/printNum : 3')
                    state = dir.get()['tmp']
                elif num == 4:
                    dir = db.reference('UserData/printNum : 4')
                    state = dir.get()['tmp']
                elif num == 5:
                    dir = db.reference('UserData/printNum : 5')
                    state = dir.get()['tmp']
                elif num == 6:
                    dir = db.reference('UserData/printNum : 6')
                    state = dir.get()['tmp']
                elif num == 7:
                    dir = db.reference('UserData/printNum : 7')
                    state = dir.get()['tmp']
                elif num == 8:
                    dir = db.reference('UserData/printNum : 8')
                    state = dir.get()['tmp']

                if state == "Waiting":
                    dir.update({'tmp': "Reservation"})
                    break

            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약성공=======\n\n3D프린터가 예약되었습니다.\n3D프린터는 2시간 후 자동 예약취소됩니다.\n\n방문 등록 후에 이용해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

        else:
            return JsonResponse(
            {
                'version': '2.0',
                'template': {
                    'outputs': [
                        {
                            'simpleText': {
                                'text': '=======예약공간부족=======\n\n예약에 실패했습니다.\n\n직접 방문한 후 >이용등록을 해주세요.'
                            }
                        }
                    ],
                    'quickReplies': [
                        {
                            'label': '홈으로',
                            'action': 'message',
                            'messageText': '홈으로'
                        }
                        ]
                    }
                })

    elif return_str == 'lbrn':
        dir = db.reference('Establishment/Lobby')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']
        dir.update({'null': tmpNum+1})
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '====예약이 취소되었습니다==\n\n최소 내역: 로비\n\n예약이 정상적으로 취소되었습니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == 'carn':
        dir = db.reference('Establishment/Carpentry')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']
        dir.update({'null': tmpNum+1})
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '====예약이 취소되었습니다==\n\n최소 내역: 목공실\n\n예약이 정상적으로 취소되었습니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == 'smrn':
        dir = db.reference('Establishment/Seminar')
        dir = db.reference('Establishment/Seminar')
        print(dir.get()['null'])
        tmpNum = dir.get()['null']
        dir.update({'null': tmpNum+1})
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '====예약이 취소되었습니다==\n\n최소 내역: 세미나실\n\n예약이 정상적으로 취소되었습니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })
    elif return_str == 'dprn':
        dir = db.reference('PrintData')
        tmpNum = dir.get()['Count']
        dir.update({'Count': tmpNum+1})

        for num in range(1, 9):
            if num == 1:
                dir = db.reference('UserData/printNum : 1')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 2')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 3')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 4')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 5')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 6')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 7')
                state = dir.get()['tmp']
            elif num == 1:
                dir = db.reference('UserData/printNum : 8')
                state = dir.get()['tmp']

            if state == "Reservation":
                dir.update({'tmp': "Waiting"})
                break

        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '====예약이 취소되었습니다==\n\n최소 내역: 3D 프린터\n\n예약이 정상적으로 취소되었습니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })

    elif return_str == 'lcrn':
        dir = db.reference('LaserData')
        tmpNum = dir.get()['Count']
        dir.update({'Count': tmpNum-1})
        return JsonResponse(
        {
            'version': '2.0',
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '====예약이 취소되었습니다==\n\n최소 내역: 레이저커터\n\n예약이 정상적으로 취소되었습니다.'
                        }
                    }
                ],
                'quickReplies': [
                    {
                        'label': '홈으로',
                        'action': 'message',
                        'messageText': '홈으로'
                    }
                    ]
                }
            })
