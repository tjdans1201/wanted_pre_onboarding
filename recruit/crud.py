from. import models
from django.db.models import Q

def get_company_info(register_company_id):
    # 기업정보 취득
    company_info = models.Company.objects.get(company_id = register_company_id)
    return company_info

def get_recruit_info(modify_recruit_id):
    # 채용공고 정보 취득
    recruit_info = models.Recruit.objects.get(recruit_id = modify_recruit_id)
    return recruit_info

def get_user_info(modify_member_id):
    # 이용자 정보 취득
    user_info = models.Member.objects.get(member_id = modify_member_id)
    return user_info


def register_recruit(request_body):
    # 채용공고 등록
    try:
        print("start_register_recruit")
        recruit = models.Recruit
        company_info = get_company_info(request_body["company_id"])
        print(company_info)
        recruit.objects.create(
            company_id = company_info,
            company_name = company_info.company_name,
            position = request_body["position"],
            compensation = int(request_body["compensation"]),
            content = request_body["content"],
            tech = request_body["tech"],
            nation = company_info.nation, 
            region = company_info.region,
        )
    except Exception as e:
        print(e)
    finally:
        print("finish_register_recruit")

def modify_recruit(request_body):
    # 채용공고 수정
    try:
        print("start_modify_recruit")
        recruit_info = get_recruit_info(request_body["recruit_id"])
        print(recruit_info)
        recruit_info.position = request_body["position"]
        recruit_info.compensation = request_body["compensation"]
        recruit_info.content = request_body["content"]
        recruit_info.tech = request_body["tech"]
        recruit_info.save()
    except Exception as e:
        print(e)
    finally:
        print("finish_modify_recruit")

def delete_recruit(request_body):
    # 채용공고 삭제
    try:
        print("start_delete_recruit")
        recruit_info = models.Recruit.objects.get(recruit_id = request_body["recruit_id"])
        recruit_info.delete()
    except Exception as e:
        print(e)
    finally:
        print("finish_delete_recruit")

def get_recruit_list(keyword=None):
    # 채용공고 목록 조회
    try:
        print("start_get_recruit_list")
        if keyword:
            # 회사명, 사용기술에서 해당 키워드 검색
            recruit_list = list(models.Recruit.objects.filter(Q(company_name__contains=keyword) | Q(tech__contains=keyword)).values("recruit_id","company_name","nation","region","position","compensation","tech"))
        else:
            recruit_list = list(models.Recruit.objects.values("recruit_id","company_name","nation","region","position","compensation","tech"))
        return recruit_list
    except Exception as e:
        print(e)
    finally:
        print("finish_get_recruit_list")

def get_recruit_detail(search_recruit_id):
    # 채용공고 상세 조회
    try:
        print("start_get_recruit_detail")
        recruit_dict = models.Recruit.objects.filter(recruit_id = search_recruit_id).values("recruit_id","nation","region","position","compensation","tech","content","company_id").first()
        return recruit_dict
    except Exception as e:
        print(e)
    finally:
        print("finish_get_recruit_detail")

def get_other_recruit_list(recruit_dict):
    # 해당 회사에 다른 채용공고 ID조회
    try:
        print("start_get_other_recruit_list")
        recruit_id_list = list(models.Recruit.objects.filter(company_id = recruit_dict["company_id"]).exclude(recruit_id =  recruit_dict["recruit_id"]).values("recruit_id"))
        if len(recruit_id_list) > 0:
            recruit_id_list = [i["recruit_id"] for i in recruit_id_list]
        return recruit_id_list
    except Exception as e:
        print(e)
    finally:
        print("finish_get_other_recruit_list")

def get_applied_recruiting(search_member_id):
    # 해당 이용자의 지원 내역 취득
    try:
        print("start_get_applied_recruiting")
        applied_recruiting = models.AppliedHistory.objects.filter(member_id = search_member_id).values("recruit_id").first()
        return applied_recruiting
    except Exception as e:
        print(e)
    finally:
        print("finish_get_applied_recruiting")

def apply_recruit(request_body):
    # 채용공고 지원
    try:
        print("start_apply_recruit")
        applid_history = models.AppliedHistory
        applid_history.objects.create(
            recruit_id = request_body["recruit_id"],
            member_id = request_body["member_id"],
        )
    except Exception as e:
        print(e)
    finally:
        print("finish_apply_recruit")