# 띵스플로우 백엔드 개발자 기업 과제

## 요구사항 구현 내용
1. 사용자의 게시글 업로드
    - title, body column 생성
    - max_length를 20과 200으로 설정
    - Postgresql 14를 사용했는데 기본적으로 emoji 저장 가능

2. 사용자 게시글에 비밀번호 설정
    - password column 생성
    - 암호화된 형태로 저장
    - 비밀번호는 6자 이상, 숫자 1개 이상 포함되어야 가능

3. 게시글 페이지네이션
    - 1페이지에 20개 단위 제공되도록 구현

4. 외부 API를 활용하여 날씨정보 저장
    - django signal을 이용하여 Post가 생성된 후 PostWeather가 생성되도록 구현
---

## 그 밖에 구현 사항
- unittest
- Swagger
---
<img width="1007" alt="스크린샷 2022-09-07 오후 4 45 22" src="https://user-images.githubusercontent.com/60789129/188820191-efd00304-5a8e-4a4b-9551-6147966b234f.png">
