# 카카오톡 챗봇 with Python, Apache

## 개요
https://github.com/HwanGonJang/ydp_alarm_with_kakaoApi

 위 깃허브에 있는 것 처럼 저의 첫번째 대형 프로젝트는 2018년 고등학교 2학년에 막무가내로 시작한 학교 알림 서비스 카카오톡 챗봇이었습니다. 친구 한 명과 함께 완전히 노베이스 상태에서 약 4개월간 쉬는시간, 방과후 틈틈히 개발했었던 기억이 납니다. 겨우 거점학교에서 파이썬 하나만 배웠던 당시 카카오톡 챗봇을 위해 서버를 공부하고 파이썬 코드를 짜며 정말 많은 시도와 실패를 했던 기억이 납니다.  당시만 해도 카카오톡 챗봇이라는 카카오톡 기능은 많이 알려지지 않았기에 정보도 적고 개발이 힘들었습니다. 하지만 그만큼 특별한 프로젝트였습니다. 서버 개념을 몰라서 단순히 리눅스 기반인 라즈베리파이에서 개발을 해보기도 하고 윈도우 cmd 창에 그냥 폴더를 생성해서 개발하기도 했었습니다. 

 그래서 문득 이런 생각이 들었습니다. 이후 약 4년이 지나고 대학교에 들어오며 정말 많은 경험과 개발 그리고 공부를 해왔는데 다시 한 번 만들어 보는 것은 어떨까? 제 첫번째 프로젝트를 복습하는 것은 제 실력을 인지하는 것 뿐 아니로 또 많은 공부가 될 것 같아 바로 개발에 착수 했습니다.  



## 개발과정

 저는 영등포고등학교 메이커스페이스 Camp51.9의 매니저로 일하고 있기에 2018년 영등포고등학교 알리미 챗봇에 이어서 이번에는 메이커스페이스의 챗봇 서비스를 제작할 것입니다. 공간정보, 행사정보, 공간예약 등 다양한 캠프 이용 서비스를 제공하는 것이 목적입니다. 이미 HTML 프로젝트로 만든 웹 어플리케이션이 파이어베이스를 연동하고 있어서 이번에는 파이썬 코드로 같은 파이어베이스를 연동하고 여러가지 정보를 가져올 수 있도록 하겠습니다.



### 1. 권한 신청

 우선 카카오톡에서 플러스친구를 개설해줍니다. 카카오톡 플러스 친구를 검색하고 사이트에 들어가면 플러스친구를 쉽게 만들 수 있습니다. 그리고 카카오톡 오픈빌더의 허가를 받아야합니다. 이 부분이 2018년과는 다른 부분입니다. 2018년에는 챗봇 서비스가 많이 알려지지 않아서 플러스친구를 개설한 이후에 구글에서 찾을 수 있는 챗봇 관련 명령어, 함수 문서를 보고 하나부터 열까지 파이썬으로 제작해야 했습니다. 하지만 이제는 오픈빌더를 통해서 코드구현 없이도 챗봇을 쉽게 개발할 수 있습니다. 2018년 당시에는 서버, 코드 등 모두 개발자가 만든 후 플러스 친구에 단순히 API만 연결 할 수 있었지만 지금은 많이 편리해져 굳이 서버를 만들거나 하지 않아도 제공되는 기능으로만 챗봇을 만들 수 있습니다. 하지만 저는 실시간으로 정보가 바뀌기 때문에 파이썬으로 코드를 작성하고 따로 서버를 구성할 것입니다. 오픈빌더 허가에는 저는 휴일이 겹쳐있어서 8일정도 걸렸습니다.
 <img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_2.png?raw=true'>

### 2. AWS 우분투 서버 설정

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_1.png?raw=true'>

 오픈빌더가 허가 되면 챗봇 개발 화면으로 들어갈 수 있습니다. 미리 만들어 놓은 플러스친구 계정을 여기에 연결해줍니다. 연결한 후 개발을 시작하기 위해 서버 개설을 합니다. 이 부분은 고2 때와 마찬가지로 아마존에서 제공하는 1년 무료 ec2 서비스를 이용합니다. AWS에 회원가입후 아마존의 우분투 무료 서버를 개설하고 private key를 다운 받습니다. 이 key는 자신의 서버를 이용하기 위한 비밀번호와 같은 역할을 해줍니다. 또, 윈도우에서는 우분투 서버를 이용하기 위해 putty라는 프로그램을 설치해야합니다. putty를 통해 윈도우에서도 우분투 서버 프로그래밍을 할 수 있습니다. putty에 ec2 서버 주소와 키를 입력하고 실행하면 우분투 서버로 접속이 가능합니다. ID는 기본으로 ubuntu를 입력하면됩니다.

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_4.png?raw=true'>

 로그인하면 처음 디렉토리인 홈 디렉토리 부터 시작이 가능합니다. 

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_3.png?raw=true'>

### 3. 프로젝트 생성 및 Django, Apache 설치

 이제 챗봇 개발을 위해서 Django와 Apache를 설치해주어야 합니다.

* 장고: 파이썬으로 작성된 오픈 소스 웹 프레임워크
* 아파치: 오픈 소스 크로스 플랫폼 HTTP 웹 서버 프레임 워크

 다음 명령으로 장고를 설치하고 프로젝트를 만들어줍니다.

~~~python
pip install django
#프로젝트 이름
django-admin startproject camp_chatbot
#실행할 앱 이름
python3 manage.py startapp camp_app
~~~

 장고는 단순히 웹 앱을 만들기 위한 프레임워크 이므로 이 웹을 배포할 서버가 필요합니다. 이 역할을 아파치가 해줄 것입니다. 프로젝트를 생성한 후에 다음 명령으로 아파치를 설치해줍니다.

~~~python
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
~~~

 장고와 아파치를 설치한 후에는 cd로 프로젝트 폴더로 이동하여 settings.py, wsgi.py 파일을 수정해줍니다. settings.py에서는 만들어준 앱을 추가하는 작업, wsgi.py는 외부로 장고를 가져올 수 있도록하는 작업입니다.

 모든 작업이 끝나면 아파치를 재시작해 변경 사항을 업데이트해줍니다.

 ~~~python
 sudo apachectl -k restart
 ~~~


### 4. 챗봇에서 실행할 파이썬 코드 작성
 챗봇이 참조하는 코드는 생성한 앱 폴더 안에 있는 views.py 입니다. 코드의 길이가 900줄이 넘기 때문에 몇몇 부분만 보겠습니다.

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_6.png?raw=true'>

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_5.png?raw=true'>



 ~~~python
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Create your views here.

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('/home/ubuntu/kakao/mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://campbase-cfe26-default-rtdb.firebaseio.com/'
})

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })
 ~~~

 views.py의 첫 부분입니다. 사용할 장고와 파이어베이스 라이브러리를 import 해줍니다. 파이썬에서 파이어베이스를 이용하기 위해서 파이어베이스의 url을 설정해주고 카카오톡 챗봇에서 받는 json을 text 타입으로 지정해줍니다. 




 ~~~python
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
 ~~~

 위 코드는 챗봇의 잔여공간 요청시에 불러오는 메시지 함수입니다. 파이썬에서 파이어베이스는 db.reference와 dir.get 을 활용해 다루는데 여기서는 메이커스페이스 시설의 잔여좌석 정보를 가져와 leftSpace 변수에 문자열로 저장합니다.



 ~~~python
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
                	#캠프 정보는 카카오톡 기능으로
                    'label':'Camp51.9 정보',            
                    'action': 'message',
                    'messageText': 'Camp51.9 정보'
                },
                {
                    'label': '예약하기',
                    'action': 'message',
                    'messageText': '예약하기'
                 },
                 {
                    'label': '행사 정보',               
                    'action': 'message',
                    'messageText': '행사 정보'
                },
                {
                    'label': '개발 정보',               
                    'action': 'message',
                    'messageText': '개발 정보'
                }
                ]
            }
        })
 ~~~

 카카오톡 챗봇의 응답은 기본적으로 if문으로 실행됩니다. 위 코드는 카카오톡에서 '홈으로' 라는 라벨을 눌렀을때의 결과입니다. 홈으로 버튼을 누르면 다시 Camp51.9 정보, 예약하기, 행사 정보, 개발 정보 라벨로 이어집니다. 그리고 나머지 코드 또한 이러한 구조가 반복됩니다. 이외에도 이미지, url 등 여러가지 기능이 있습니다.




### 카카오 오픈빌더 설정
 처음에 이제 카카오톡 챗봇을 오픈빌더만으로 구축할 수 있다고 했습니다. 오픈빌더에서는 시나리오 추가를 통해서 여러가지 경우의 수에 대한 응답을 설정할 수 있고 응답으로 이미지, 링크, 또다른 버튼, 구매 등 다양한 기능을 추가할 수 있습니다. 저는 이곳에서 기본적인 인사를 작성하고 버튼을 배치했습니다. 그 후 스킬 탭에서 스킬 배포를 해주면 기능 구성은 완료입니다.

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_7.png?raw=true'>

 마지막으로 배포 탭에서 모든 설정에 대한 배포를 해주면 카카오톡 챗봇 구축 성공입니다.

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_8.png?raw=true'>

## 마무리
 이렇게 카카오톡 챗봇을 3년이 지난 후 다시 만들게 되었습니다. 처음 만들떄에는 구글을 따라하면서 이해도 못하고 개발했던 기억이 나는데 다시 개발해보니 그때 했던 작업이 어떤 작업인지 이해가 되고 뿌듯합니다. 이것으로 카카오톡 챗봇 글을 마무리합니다. 감사합니다.

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_10.jpg?raw=true' width='500' height='1000'>

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_11.jpg?raw=true' width='500' height='1000'>

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_12.jpg?raw=true' width='500' height='1000'>

<img src='https://github.com/HwanGonJang/HwanGonJang.github.io/blob/master/Pictures/k_13.png?raw=true'>
