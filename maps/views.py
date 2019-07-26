from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls import url
from django.http import JsonResponse
import urllib.request, json, pprint
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Common, Detail
from .serializers import CommonSerializer, DetailSerializer, SearchByAreaSerializer, SearchBySigunguSerializer, SearchByCategorySerializer, SearchByContentIdSerializer

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


# api db 저장 및 update
def detailcommon(request):
    # ServiceKey = "tG2pbhauvACu6IO20lRl4NIY5qDcRrFnl21s57G6XgwovyquyiFquhZgoE%2FBmG930wyBEyxx4pNZEyxzt8%2Brvg%3D%3D"
    # ServiceKey = "5Z64FYjCYoIRrToMriTzGi%2BbzlzcHOFJKdG9NFgR77i52r%2BCCi6XbU9gpq15l8fEGojdilIdq0iyzQvIpe3BlQ%3D%3D"
    ServiceKey = "GK%2BXkUwSbqiqfXfrJ2VPSperv70MFPcgz0%2Fo1NqOV%2FGlNX4AdA5wzyWdvTHPpaXtFSMSjrR1AhRE%2FEaCW37V9g%3D%3D"
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey="
    option = "&contentTypeId=&defaultYN=Y&overviewYN=Y&addrinfoYN=Y&areacodeYN=Y&sigungucodeYN=Y&numOfRows=25344&pageNo=1&MobileOS=AND&MobileApp=travel5&_type=json"
    url_ = url + ServiceKey + option

    request_ = urllib.request.Request(url_)
    response = urllib.request.urlopen(request_)
    rescode = response.getcode()
    print(rescode)


    if (rescode == 200):
        column_list = ['contentId', 'category', 'tel', 'addr1', 'addr2', 'area', 'sigungu', 'title',  'overview', 'zipCode', 'homepage', 'mapx', 'mapy']
        items_list = ['contentid','contenttypeid', 'tel', 'addr1', 'addr2', 'areacode', 'sigungucode', 'title', 'overview', 'zipcode', 'homepage', 'mapx', 'mapy']
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        items = dict['response']['body']['items']['item'] 

        for item in items :
            result_value = []
            result_column=[]
            for i in items_list:
                if i in item.keys() :
                    result_value.append(item[i])
                    result_column.append(column_list[items_list.index(i)])
                else:
                    if items_list.index(i) in [0, 1, 5, 6, 11, 12]:
                        result_value.append(0)
                    else:
                        result_value.append('없음')
                    result_column.append(column_list[items_list.index(i)])
            
            common = Common(contentId=int(result_value[0]), category=int(result_value[1]), tel=result_value[2], 
                            addr1=result_value[3], addr2=result_value[4], area=int(result_value[5]),
                            sigungu=int(result_value[6]), title=result_value[7], overview=result_value[8],
                            zipCode=result_value[9], homepage=result_value[10], 
                            mapx=float(result_value[11]), mapy=float(result_value[12]))
            
            # image 저장
            # detail_key = "5Z64FYjCYoIRrToMriTzGi%2BbzlzcHOFJKdG9NFgR77i52r%2BCCi6XbU9gpq15l8fEGojdilIdq0iyzQvIpe3BlQ%3D%3D"
            detail_key = "GK%2BXkUwSbqiqfXfrJ2VPSperv70MFPcgz0%2Fo1NqOV%2FGlNX4AdA5wzyWdvTHPpaXtFSMSjrR1AhRE%2FEaCW37V9g%3D%3D"
            # detail_key = "tG2pbhauvACu6IO20lRl4NIY5qDcRrFnl21s57G6XgwovyquyiFquhZgoE%2FBmG930wyBEyxx4pNZEyxzt8%2Brvg%3D%3D"
            image_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailImage?ServiceKey={detail_key}&contentId={int(result_value[0])}&imageYN=Y&MobileOS=ETC&MobileApp=AppTest&_type=json"
            temp_url = urllib.request.urlopen(image_url)
            # print(image_url)
            f = temp_url.read()
            content = json.loads(f.decode('utf-8'))
            # pprint.pprint(content)
            image_items = content['response']['body']['items']
            # pprint.pprint(image_items)
            image_list = []
            if image_items == '' :
                image_list.append("null")
            else:
                for item in image_items['item'] :
                    if type({'key':'1'}) == type(item):
                        image_list.append(item['originimgurl'])
                    else:
                        # print(image_items['item']['originimgurl'])
                        image_list.append(image_items['item']['originimgurl'])
            common.image = image_list
            
            # overview
            detailinfo_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?ServiceKey={detail_key}&contentId={int(result_value[0])}&defaultYN=Y&overviewYN=Y&MobileOS=ETC&MobileApp=AppTest&_type=json"
            temp_url = urllib.request.urlopen(detailinfo_url)
            f = temp_url.read()
            content = json.loads(f.decode('utf-8'))
            # pprint.pprint(content)
            detail_items = content['response']['body']['items']['item']
            # pprint.pprint(detail_items)
            if 'homepage' in detail_items.keys():
                homepy = detail_items['homepage']
                common.homepage = homepy
            if 'overview' in detail_items.keys():
                infotext = detail_items['overview']
                common.overview = infotext
            common.save()                                                                                                           
            
            print('----------------------------------')
            # detail 저장
            detailintro_url = f"http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailIntro?ServiceKey={detail_key}&contentId={int(result_value[0])}&contentTypeId={int(result_value[1])}&MobileOS=ETC&MobileApp=AppTest&_type=json&numOfRows="
            temp_url = urllib.request.urlopen(detailintro_url)
            f = temp_url.read()
            content = json.loads(f.decode('utf-8'))
            detail_items = content['response']['body']['items']['item']
            # pprint.pprint(detail_items)
            detail = Detail()
            detail_pk = int(result_value[0])
            category = int(result_value[1])
            detail.detailId = Common.objects.get(contentId=detail_pk)
            detail.save()

            # 관광지
            if category == 12 :
                detail_set = {
                    'chkbabycarriage': 'chkBaby',
                    'chkpet': 'chkPet',
                    'expagerange': 'ageLimit',
                    'restdate': 'restDate',
                    'usetime': 'useTime',
                }

                for item in detail_items.keys():
                    if item in detail_set.keys():
                        detail = Detail.objects.get(detailId=detail_pk)
                        print(item, detail_set[item])
                    # if v in detail_items.keys():
                    #     detail = Detail.objects.get(detailId=detail_pk)
                    #     key = k
                    #     value = v
                    #     detail(key = detail_items[value])
                    #     print(key,value, detail_items[value], detail.key)
                    #     detail.save()


            # 행사/공연/축제
            if category == 15 :
                detail_set = {
                    'ageLimit' : 'agelimit',
                    'startTime' : 'eventstartdate',
                    'endTime' : 'eventenddate',
                    'subevent' : 'subevent'
                }

                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()


            # 문화시설
            if category == 14 :
                detail_set = {
                    'chkBaby' : 'chkbabycarriageculture',
                    'chkPet' : 'chkpetculture',
                    'discountInfo' : 'discountinfo',
                    'pay' : 'usefee'
                }

                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()


            # 레포츠
            if category == 28 :
                detail_set = {
                    'chkBaby' : 'chkbabycarriageleports',
                    'chkPet' : 'chkpetleports',
                    'ageLimit' : 'agelimit',
                    'openPeriod' : 'openperiod',
                    'pay' : 'usefeeleports'
                }

                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()

            # 숙박
            if category == 32 :
                detail_set = {
                    'chkinTime' : 'checkintime',
                    'chkoutTime' : 'checkouttime',
                    'chkCook' : 'chkcooking',
                    'subevent' : 'subfacility',
                    'refund' : 'refundrequlation'
                }

                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()
                
            # 쇼핑
            if category == 38 :
                detail_set = {
                    'chkBaby' : 'chkbabycarriageshopping',
                    'chkPet' : 'chkpetshopping',
                    'openPeriod' : 'chkcooking',
                    'subevent' : 'opendateshopping',
                    'openTime' : 'opentime'
                }
                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()
            
            
            # 음식점
            if category == 39 :
                detail_set = {
                    'discountInfo' : 'discountinfofood',
                    'chkBaby' : 'kidsfacility',
                    'chkPack' : 'packing',
                    'chkSmoking' : 'smoking',
                    'openTime' : 'opentimefood'
                }

                for k, v in detail_set.items():
                    if v in detail_items.keys():
                        key = k
                        value = v
                        detail.key = detail_items[value]
                print(detail)
                detail.save()

            detail.common = common
            detail.save()
    else:
        print("잠시 후에 다시 도전!")
    return render(request, 'maps/')

# serializer
def commonserializers(request):
    commons = Common.objects.all()
    serializer = CommonSerializer(commons, many=True)
    return JsonResponse(serializer.data, safe=False)



# main page
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

# main_map
def korea(request):
    return render(request, 'maps/korea.html')

    

def map(request):
    return render(request, 'maps/map.html')

@api_view(['GET'])
def commonserializers(request):
    '''
    공통정보 출력
    '''
    commons = Common.objects.all()
    serializer = CommonSerializer(commons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchbyareaserializers(request, area):
    '''
    지역코드로 정보 가져오기
    '''
    commons = Common.objects.filter(area=area)
    serializer = SearchByAreaSerializer(commons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchbysigunguserializers(request, area, sigungu):
    '''
    지역코드, 시군구 코드로 정보 가져오기
    '''
    commons = Common.objects.filter(area=area, sigungu=sigungu)
    serializer = SearchBySigunguSerializer(commons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchbycategoryserializers(request, category):
    '''
    카테고리로 정보 가져오기
    '''
    commons = Common.objects.filter(category=category)
    serializer = SearchByCategorySerializer(commons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchbycontentidserializers(request, contentid):
    '''
    contentid로 정보 가져오기
    '''
    commons = Common.objects.filter(contentid=contentid)
    serializer = SearchByContentIdSerializer(commons, many=True)
    return Response(serializer.data)
