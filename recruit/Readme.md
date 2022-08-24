1) 채용공고 등록

url: http://host:port/recruit/register

input_parameter : ex) {"company_id":1, "position": "백엔드 시니어 개발자", "compensation":2000000,"content":"원티드랩에서 백엔드 시니어 개발자를 채용합니다. 자격요건은..","tech":"java"}

response:
    ex)
        성공 : {result:success}
        실패 : {error:error 내용}

2) 채용공고 수정

url: http://host:port/recruit/modify

input_parameter : ex) {"recruit_id":1,"position": "백엔드드 시니어 개발자", "compensation":2000000,"content":"원티드랩에서 백엔드 시니어 개발자를 채용합니다. 자격요건은..","tech":"python" }

response:
    ex)
        성공 : {result:success}
        실패 : {error:error 내용}

3) 채용공고 삭제

url: http://host:port/recruit/delete

input_parameter : ex) {recruit_id:1}

response:
    ex)
        성공 : {result:success}
        실패 : {error:error 내용}

4) 채용공고 목록

검색 키워드가 없는 경우
url: http://host:port/recruit/search

검색 키워드가 있는 경우(쿼리 파라미터 추가)
url: http://host:port/recruit/search?search=keyword

response:
    ex) 
        성공 : {recruit_list:[
            {
                "recruit_id": 1,
                "company_name": "wanted",
                "nation": "korea",
                "region": "seoul",
                "position": "백엔드 시니어 개발자",
                "compensation": 2000000,
                "tech": "java"
            },
            {
                "recruit_id": 2,
                "company_name": "wanted",
                "nation": "korea",
                "region": "seoul",
                "position": "백엔드 주니어 개발자",
                "compensation": 2000000,
                "tech": "java"
            }]}
        실패 : {error:error 내용}

5) 채용 상세 페이지(해당 회사가 올린 다른 채용공고가 추가적으로 포함)

url: http://host:port/recruit/search_recruit_detail

input_parameter : ex) {recruit_id:1}

response:
    ex)
        성공 : { "recruit_detail": 
        {
            "recruit_id": 1,
            "nation": "korea",
            "region": "seoul",
            "position": "백엔드드 시니어 개발자",
            "compensation": 2000000,
            "tech": "java",
            "content": "원티드랩에서 백엔드 시니어 개발자를 채용합니다. 자격요건은..",
            "other_recruit_id": [
                2,
                3
            ]
            }
        }
        실패 : {error:error 내용}

6) 채용공고 지원

url: http://host:port/recruit/apply

input_parameter : ex) {member_id:1, recruit_id:1}

response:
    ex)
        성공 : 정상등록 -> {result:success}, 지원 내역 있는 경우 -> {result:already applied}
        실패 : {error:error 내용}