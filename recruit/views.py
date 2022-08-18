from django.http import HttpResponse, JsonResponse
from. import crud
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    # 채용공고 등록
    request_body = json.loads(request.body)
    crud.register_recruit(request_body)
    return JsonResponse(request_body)

def modify(request):
    # 채용공고 수정
    request_body = json.loads(request.body)
    crud.modify_recruit(request_body)
    return JsonResponse(request_body)

def delete(request):
    # 채용공고 삭제
    request_body = json.loads(request.body)
    crud.delete_recruit(request_body)
    return JsonResponse(request_body)

def search(request, keyword:None):
    # 채용공고 취득
    if keyword is not None:
        pass
    recruit_list = crud.get_recruit_list()
    return HttpResponse(recruit_list)

def search_recruit_detail(request):
    # 채용공고 상세 취득
    request_body = json.loads(request.body)
    recruit_dict = crud.get_recruit_detail(request_body["recruit_id"])
    other_recruit_list = crud.get_other_recruit_list(recruit_dict)
    recruit_dict["other_recruit_id"] = other_recruit_list
    recruit_dict.pop("company_id")
    return JsonResponse(recruit_dict)