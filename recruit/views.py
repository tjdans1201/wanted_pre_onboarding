from django.http import JsonResponse
from. import crud
import json

def register(request):
    # 채용공고 등록
    try:
        result = {"result":"success"}
        request_body = json.loads(request.body)
        crud.register_recruit(request_body)
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)

def modify(request):
    # 채용공고 수정
    try:
        result = {"result":"success"}
        request_body = json.loads(request.body)
        crud.modify_recruit(request_body)
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)

def delete(request):
    # 채용공고 삭제
    try:
        result = {"result":"success"}
        request_body = json.loads(request.body)
        crud.delete_recruit(request_body)
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)

def search(request):
    # 채용공고 취득
    try:
        result = {}
        if "search" in request.GET:
        # 검색 키워드가 있는 경우
            keyword = request.GET["search"]
            recruit_list = crud.get_recruit_list(keyword)
        else:
        # 검색 키워드가 없는 경우
            recruit_list = crud.get_recruit_list()
        result["recruit_list"] = recruit_list
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)

def search_recruit_detail(request):
    # 채용공고 상세 취득
    try:
        result = {}
        request_body = json.loads(request.body)
        recruit_dict = crud.get_recruit_detail(request_body["recruit_id"])
        # 해당 기업이 등록한 채용공고 리스트 취득
        other_recruit_list = crud.get_other_recruit_list(recruit_dict)
        recruit_dict["other_recruit_id"] = other_recruit_list
        recruit_dict.pop("company_id")
        result["recruit_detail"] = recruit_dict
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)

def apply(request):
    # 채용공고 지원
    try:
        result = {"result":"success"}
        request_body = json.loads(request.body)
        # 지원 내역 확인(1회만 지원 가능)
        applied_recruiting = crud.get_applied_recruiting(request_body["member_id"])
        # 지원 내역 없는 경우 지원
        if applied_recruiting == None:
            crud.apply_recruit(request_body)
        else:
            result["result"] = "already applied"
    except Exception as e:
        result = {"error":e}
    finally:
        return JsonResponse(result)