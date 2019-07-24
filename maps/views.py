from django.shortcuts import render
from django.conf.urls import url
import urllib.request
import json
import pprint
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import DetailInformSerializer
# from .models import DetailInform


# Create your views here.

def main(request):
    ServiceKey = "tG2pbhauvACu6IO20lRl4NIY5qDcRrFnl21s57G6XgwovyquyiFquhZgoE%2FBmG930wyBEyxx4pNZEyxzt8%2Brvg%3D%3D"
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/"
    key = "?ServiceKey=" + ServiceKey
    get = "areaCode"
    option = "&numOfRows=17&pageNo=1&MobileOS=AND&MobileApp=travel5&_type=json"
    url_ = url + get + key + option

    request_ = urllib.request.Request(url_)
    response = urllib.request.urlopen(request_)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        value = dict['response']['body']['items']['item']
        context = {'value': value }
        return render(request, 'maps/MainPage.html', context)
    else:
        print("Error Code:" + rescode)
        return render(request, 'maps/MainPage.html')

def korea(request):
    return render(request, 'maps/korea.html')

def getInform(items, key_lists, lists):
    inform = {}
    value_lists = []
    # 값 없는거 빼기
    for i in items:
        if i in lists :
            value_lists.append((lists.index(i),i))
            print(i)
    value_lists.sort()
    # print(value_lists)
    for i in range(len(value_lists)) :
        inform.update({key_lists[value_lists[i][0]]:items[value_lists[i][1]]})
    return inform

# detail page
def detailpage(request, content_id):
    content_type_code = {'관광지' : 12, '문화시설':14, '행사/공연/축제' : 15, 
                        '레포츠':28, '숙박':32, '쇼핑':38, '음식점':39}
    servicekey = "GK%2BXkUwSbqiqfXfrJ2VPSperv70MFPcgz0%2Fo1NqOV%2FGlNX4AdA5wzyWdvTHPpaXtFSMSjrR1AhRE%2FEaCW37V9g%3D%3D"
    # print(content_id, servicekey)

    # 공통 정보 조회 (간단한 정보만)
    pre_url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?ServiceKey="
    common_url = pre_url + servicekey + "&contentId=" + str(content_id) + "&defaultYN=Y&MobileOS=ETC&MobileApp=AppTest&_type=json"
    print(common_url)

    # image를 위한 contentTypeId 가져오기
    temp_url = urllib.request.urlopen(common_url)
    f = temp_url.read()
    content = json.loads(f.decode('utf-8'))
    content_type_id = content['response']['body']['items']['item']['contenttypeid']
    title = content['response']['body']['items']['item']['title']
    print(content_type_id, title)

    # image 가져오기
    image_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailImage?ServiceKey={servicekey}&contentId={content_id}&contentTypeId={content_type_id}&MobileOS=ETC&MobileApp=AppTest&_type=json"
    # print(image_url)
    temp_url = urllib.request.urlopen(image_url)
    f = temp_url.read()
    content = json.loads(f.decode('utf-8'))
    # pprint.pprint(content)
    image_items = content['response']['body']['items']['item']
    image_list = []
    for i in image_items :
        image_list.append(i['originimgurl'])
    print(image_list)

    # 숙박/여행/그 이외 정보 추가
    detailinfo_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailInfo?ServiceKey={servicekey}&contentId={content_id}&contentTypeId={content_type_id}&MobileOS=ETC&MobileApp=AppTest&_type=json"
    temp_url = urllib.request.urlopen(detailinfo_url)
    f = temp_url.read()
    content = json.loads(f.decode('utf-8'))
    pprint.pprint(content)
    detail_items = content['response']['body']['items']['item']
    pprint.pprint(detail_items[0]['infotext'])
    infotext = detail_items[0]['infotext']
    print('---------------------------------')

    # 소개 정보 가져오기
    detailintro_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailIntro?ServiceKey={servicekey}&contentId={content_id}&contentTypeId={content_type_id}&MobileOS=ETC&MobileApp=AppTest&_type=json"
    # print(detailinfo_url)
    temp_url = urllib.request.urlopen(detailintro_url)
    f = temp_url.read()
    content = json.loads(f.decode('utf-8'))
    pprint.pprint(content)
    items = content['response']['body']['items']['item']
    # pprint.pprint(items)

    # 행사/공연/축제
    if content_type_id == 15 :
        key_lists = ['관람 가능 연령', '이용 요금', '장소', '행사 시작일', '행사 종료일', '행사 홈페이지']
        lists = ['agelimit', 'usetimefestival','eventplace', 'eventstartdate', 'eventenddate', 'eventhomepage']
        inform = getInform(items, key_lists, lists)

    # 관광지
    if content_type_id == 12 :
        key_lists = ['체험안내', '이용시기', '이용시간', '주차시설', '문의 및 안내']
        lists = ['expguide', 'useseason','usetime', 'parking', 'infocenter']
        inform = getInform(items, key_lists, lists)

    # 문화시설
    if content_type_id == 14 :
        key_lists = ['이용시간',' 이용요금', '관람시간', '쉬는날', '주차시설', '할인정보', '문의 및 안내']
        lists = ['usetimeculture', 'usefee', 'spendtime', 'restdateculture', 
                'parkingculture','discountinfo', 'infocenterculture']
        inform = getInform(items, key_lists, lists)

    # 여행코스
    if content_type_id == 25 :
        key_lists = ['코스 총거리', '코스 일정', '코스 총 소요시간', '코스 테마', '문의 및 안내']
        lists = ['distance', 'schedule', 'taketime','theme','infocentertourcourse']
        inform = getInform(items, key_lists, lists)

    # 레포츠
    if content_type_id == 28 :
        key_lists = ['체험 가능연령', '개장기간', '이용시간', '입장료', '쉬는날', '예약안내', '문의 및 안내']
        lists = ['expagerangeleports', 'openperiod', 'usetimeleports', 'usefeeleports','restdateleports', 'reservation', 'infocenterleports']
        inform = getInform(items, key_lists, lists)

    # 숙박
    if content_type_id == 32 :
        key_lists = ['입실 시간', '퇴실 시간', '주차 시설', '예약안내', '예약안내 홈페이지', '문의 및 안내']
        lists = ['checkintime', 'checkouttime', 'parkinglodging','reservationlodging', 'reservationurl', 'infocenterlodging']
        inform = getInform(items, key_lists, lists)

    # 쇼핑
    if content_type_id == 38 :
        key_lists = ['개장일', '영업시간','쉬는날', '매장안내', '주차 시설', '문의 및 안내']
        lists = ['opendateshopping', 'opentime', 'restdateshopping', 'shopguide', 'parkingshopping', 'infocentershopping']
        inform = getInform(items, key_lists, lists)
    
    # 음식점
    if content_type_id == 39 :
        key_lists = ['대표메뉴', '영업시간', '포장 가능', '예약안내', '어린이 놀이방 여부', '금연/흡연 여부', '주차 시설','문의 및 안내']
        lists = ['firstmenu', 'opentimefood', 'packing', 'reservationfood', 'kidsfacility','smoking', 'parkingfood','infocenterfood']
        inform = getInform(items, key_lists, lists)
    print(inform)
        
    detail = DetailInform()
    detail.title = title
    detail.image_lists = image_list
    detail.content = infotext
    detail.save()
    
    context = {'imageList':image_list, 'inform':inform, 'title':title, 'infotext':infotext}
    return render(request, 'maps/DetailPage.html', context)

def map(request):
    return render(request, 'maps/map.html')
