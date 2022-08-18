from turtle import position
from. import models
import recruit

def get_company_info(register_company_id):
    company_info = models.Company.objects.get(company_id = register_company_id)
    print(company_info)
    return company_info

def get_recruit_info(modify_recruit_id):
    recruit_info = models.Recruit.objects.get(recruit_id = modify_recruit_id)
    print(recruit_info)
    return recruit_info


def register_recruit(request_body):
    try:
        print("start_register_recruit")
        recruit = models.Recruit
        company_info = get_company_info(request_body["company_id"])
        print(company_info)
        recruit.objects.create(
            company_id = company_info,
            position = request_body["position"],
            compensation = int(request_body["compensation"]),
            content = request_body["content"],
            tech = request_body["tech"],
            nation = company_info.nation, 
            region = company_info.region,
            volunteer = 0
        )
    except Exception as e:
        print(e)
    finally:
        print("finish_register_recruit")

def modify_recruit(request_body):
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
    try:
        print("start_delete_recruit")
        recruit_info = models.Recruit.objects.get(recruit_id = request_body["recruit_id"])
        recruit_info.delete()
    except Exception as e:
        print(e)
    finally:
        print("finish_delete_recruit")

def get_recruit_list():
    try:
        print("start_get_recruit_list")
        recruit_list = list(models.Recruit.objects.values("recruit_id","nation","region","position","compensation","tech"))
        return recruit_list
    except Exception as e:
        print(e)
    finally:
        print("finish_get_recruit_list")

def get_recruit_detail(search_recruit_id):
    try:
        print("start_get_recruit_detail")
        recruit_dict = models.Recruit.objects.filter(recruit_id = search_recruit_id).values("recruit_id","nation","region","position","compensation","tech","content","company_id").first()
        return recruit_dict
    except Exception as e:
        print(e)
    finally:
        print("finish_get_recruit_detail")

def get_other_recruit_list(recruit_dict):
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