from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
def keyboard(request):
    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['소개','학교','천안볼거리','학사정보']
        }
    )
@csrf_exempt    
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    if cafeteria_name == '소개':
        return JsonResponse({
                'message': {
                    'text':' 안녕 날 소개할께!!',
                    'text':'나는 광회봇이고, 내 꿈은 IT왕이 되는거야!!\n 언젠간 멋진 동료들을 이끌고 나도 항해를 할거야!',
                    'photo': {
                        'url':'http://mblogthumb2.phinf.naver.net/20110612_265/qorwjs_0_1307855937077j3a4i_JPEG/3%C3%B5%B8%B8.jpg?type=w2',
                        'width':640,
                        'height':480
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['소개','학교','천안볼거리','학사정보']
                }
            })
    elif cafeteria_name == '학교':
        return JsonResponse({
            'message': {
                'text': '나는 단국대학교를 졸업했어',
                'photo': {
                    'url': 'https://upload.wikimedia.org/wikipedia/ko/0/06/Dankook_emblem.png',
                    'width': 640,
                    'height': 480

                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보']
            }
        })
    elif cafeteria_name == '천안볼거리':
        return JsonResponse({
            'message': {
                'text': '봄여행'+spring('http://www.cheonan.go.kr/tour/sub02_01_01.do')
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보']
            }
        })
    elif cafeteria_name == '학사정보':
        return JsonResponse({
            'message': {
                'text':  '2018학년도 축제 관련 수업진행 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656946\n'\
 +'2018학년도 축제 관련 수업진행 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656910\n'\
 +' 2018학년도 계절(하계)학기 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656619\n'\
 +' [국제]2018년 하반기 중남미 지역기구 파견인턴 선발 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=657084\n'\
 +' [국제]2019년도 일본정부(문부과학성)초청 국비 연구유학생 모집 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=657061\n'\
 +' [국제] 경기도-광동성 대학생 국제교류캠프 참가자 모집 홍보\n'
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656981\n'\
 +' [국제] 2019 불가리아 정부초청 장학생 선발 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656978\n'\
 +' [국제] 콜롬비아 정부의 스페인어 연수 프로그램 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656934\n'\
 +' [국제] 2018년도 국비유학생 선발 공고\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656931\n'\
 +' [국제] 2018년도 기술기능인 국비연수생 선발 공고\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656914\n'\
 +' 2018학년도 하계 국제영어(ICE) 수강 신청 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656913\n'\
 +' [국제] 국제계절학기 Academic Program 실시 안내(정정)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656895\n'\
 +' 2018 하계 단국영어몰입프로그램(i EDU) 신청 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656864\n'\
 +' [국제]천안캠퍼스 국제학생회(GTN) 15기 모집 안내(추가 모집)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656844\n'\
 +' [국제] 집중외국어회화과정 Global Village 실시 안내 (강의계획서 추가)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656728\n'\
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보']
            }
        })        
    
def crawling():
    url = 'https://portal.dankook.ac.kr/web/portal/-7'
    html = urlopen(url)
    source = html.read()
    html.close()
    soup = BeautifulSoup(source, 'html5lib')
    table = soup.find(id="p_p_id_Bbs_WAR_bbsportlet_")
    text = table.find_all(class_="subject")

    for x in text:
        title = x.get_text()
        print(title, end=' \n')
        link = x.a.get('href')
        print(link)
    return crawling
            
def spring(url):
    r=requests.get(url)#소스를 가져온다
    c=r.content#소스에서 내용물을 가져온다
    soup = BeautifulSoup(c,'html.parser')#가져온 소스를 보기좋게~~해준다.
    all=soup.find('div', class_='thema_list')#필요한부분의 전체를 다 끌고온다. 주의 할것은 class는 class_로 해줘야한다.
    column = all.find_all('div',{'class':'row'})
    result = ''
    for i,items in enumerate(column):
        title=items.find('strong').text
        summary=items.find('p').text
        link = items.a.get('href')
        result += str(i+1)+". "+title + "\n" + summary+"\n" +'<자세한정보>\n'+'http://www.cheonan.go.kr'+link+"\n"
    return result        
       


            
    
            
    
        






















        
            
    
        





















