# 1팀 DATA로 - 추천시스템 기반 영화 스트리밍 사이트(PICK&FLIX)

---------------------------------------

# 프로젝트 계획서

## 1. 프로젝트 개요
- **프로젝트명**: 빅데이터 & 클라우드 IT 교육과정 최종 프로젝트
- **프로젝트 주제**: 추천시스템 기반 영화 스트리밍 사이트(PICK & FLIX)
- **목표**: 영화 시청 경험 극대화 및 사용자 만족도 향상
- **기간**: 2024년 6월 - 2025년 1월

## 2. 프로젝트 일정
- **프로젝트 기획**: 2024년 8월 19일 - 8월 21일
- **프로토타입 개발**: 2024년 10월 24일 - 10월 30일
- **최종 프로젝트 개발 및 테스트**: 2024년 11월 07일 - 12월 30일

## 3. 팀 구성
<table style="width:100%; text-align:center; table-layout:fixed;">
  <colgroup>
    <col style="width:20%;">
    <col style="width:20%;">
    <col style="width:20%;">
    <col style="width:20%;">
    <col style="width:20%;">
  </colgroup>
  <thead>
    <tr>
      <th>곽현철</th>
      <th>김승훈</th>
      <th>서정임</th>
      <th>양현우</th>
      <th>조진형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>데이터 수집 및 분석<br>DB 모델링 및 기획</td>
      <td>개발 기획 및 총괄 책임<br>데이터분석</td>
      <td>Front & Back 개발<br>DB 모델링 및 구축</td>
      <td>Front & Back 개발<br>DB 모델링</td>
      <td>AWS 인프라 구축<br>데이터분석</td>
    </tr>
  </tbody>
</table>
<br>



</div>
<div style="text-align: left;">
    <h2 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 4. 🛠️ Tech Stacks </h2>
    <br>
    <div style="margin: 10px 0; text-align: left; font-weight: 700; font-size:20px; color: #282d33;">
        <p><strong>주 개발 언어</strong><br>
            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" style="border-radius: 5px;"></p>
        <p><strong>데이터베이스</strong><br>
            <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white" style="border-radius: 5px;"></p>
        <p><strong>웹 구현</strong><br>
            <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white" style="border-radius: 5px;">
            <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white" style="border-radius: 5px;">
            <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white" style="border-radius: 5px;">
            <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white" style="border-radius: 5px;"></p>
        <p><strong>클라우드 환경</strong><br>
            <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white" style="border-radius: 5px;"></p>
    </div>
</div>

<br><br>
## 5. 📑 Documents

<details>
<summary>요구사항 정의서</summary>

#### 사용자 기능

| 기능               | 세부 설명                                                                                     |
|--------------------|----------------------------------------------------------------------------------------------|
| 회원가입 및 로그인,<br> 선호장르 선택 | - 회원가입 시 이메일, 비밀번호, 이름, 생년월일, 성별, 시도 입력<br>- 로그인 및 비밀번호 재설정 기능 제공<br>- 최초 로그인 시 선호 장르 선택 |
| 영화 검색 및 추천  | - 영화 제목 검색을 통해 영화 정보 확인<br>- 개인화된 AI 추천 기능<br>- 평점 TOP 10 영화 리스트 제공<br>- 현재 시청 중인 영화 보기<br>- 비슷한 시청 기록을 가진 사용자의 추천 영화 제공<br>- 곧 계약이 종료되는 영화 알림<br>- 전체 영화 리스트 제공 |
| 영화 재생 및 기록  | - 영화를 스트리밍하여 시청 가능<br>- 시청 완료 후 시청률 및 평점 기록 가능                            |
| 위시리스트 관리    | - 관심 있는 영화를 위시리스트에 추가/제거 가능<br>- 위시리스트에서 영화 세부 정보로 바로 접근 가능        |
| 장르 검색          | - 관심 있는 장르 선택 후 해당 장르별 영화 검색 가능<br>- 검색된 영화 클릭 시 영화 세부 정보로 바로 접근 가능 |
| 프로필 관리        | - 사용자 자신의 프로필 확인 및 수정 기능 제공                                                    |
<br>

#### 관리자 기능

| 기능               | 세부 설명                                                                                     |
|--------------------|----------------------------------------------------------------------------------------------|
| 영화 신규 등록     | - 영화의 코드, 제목, 출시년도, 감독, 장르, 줄거리, 런타임, 시청 등급, 추가일, 계약 종료일, 포스터, 영상정보 추가 가능 |
| 영화 관리          | - 영화 정보를 수정 및 공개 여부 확인 가능<br>- 영화를 검색하여 원하는 영화를 빠르게 찾을 수 있는 기능     |
| 계약 관리          | - 계약 종료일이 임박한 영화 리스트 확인 및 관리                                                   |

[요구사항정의서.pdf](https://github.com/whynotsw-camp/wh01-3rd-4team-DATA-/blob/main/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%EC%A0%95%EC%9D%98%EC%84%9C.pdf)

</details>
<details>
<summary>WBS</summary>

[WBS.pdf](https://github.com/whynotsw-camp/wh01-3rd-4team-DATA-/blob/main/WBS.pdf)

</details>

<details>
<summary>모델 정의서, 성능평가방식</summary>

모델 정의서 문서 내 일부 내용 발췌하였습니다.

#### 모델 개요
| 항목           | 내용                                                                                     |
|----------------|------------------------------------------------------------------------------------------|
| **모델 이름**  | Contents-based Filtering 추천 알고리즘                                                     |
| **목적**       | 사용자 시청 영화의 장르 및 키워드 데이터를 기반으로 유사 영화 추천 리스트 생성                 |
<br>

#### 모델 설명

| 항목               | 내용                                                                                 |
|--------------------|--------------------------------------------------------------------------------------|
| **알고리즘 유형**  | CountVectorizer 또는 TfidfVectorizer + 코사인 유사도 기반 추천                           |
| **모델 구조**      | 영화 메타데이터를 벡터화하여 영화 간 유사도 계산<br>사용자 선호 벡터를 생성하고 유사 영화 추출 |
<br>

#### 실험 및 결과

| 항목               | 내용                                                                                 |
|--------------------|--------------------------------------------------------------------------------------|
| **데이터셋**       | 20개년 한국 박스오피스 Top 50 (총 963개 영화 데이터)                                    |
| **평가 방법**      | Precision@K: 상위 K개 추천 항목 중 실제로 유용한 항목의 비율 (클릭 또는 재생 여부 기준)        |
| **업데이트 요소**  | - 콘텐츠 증가 시 계산 리소스가 증가할 수 있음<br>- 선호하지 않는 영화를 예측해 계산 과정에서 제외 가능<br>- 하이브리드 방식(내용 기반 + 협업 필터링) 적용 가능 |

[모델정의서, 성능평가방식.pdf](https://github.com/whynotsw-camp/wh01-3rd-4team-DATA-/blob/main/%EB%AA%A8%EB%8D%B8%EC%A0%95%EC%9D%98%EC%84%9C%2C%EC%84%B1%EB%8A%A5%ED%8F%89%EA%B0%80%EB%B0%A9%EC%8B%9D.pdf)

</details>


<details>
<summary>최종 보고서(발표 PPT)</summary>

[추천 시스템 기반 영화 스트리밍 사이트(PICK&FLIX).pptx](https://github.com/whynotsw-camp/wh01-3rd-4team-DATA-/blob/main/DATA%EB%A1%9C_%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EA%B8%B0%EB%B0%98%20%EC%98%81%ED%99%94%20%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D%20%EC%82%AC%EC%9D%B4%ED%8A%B8(PICK%26FLIX)_1230.pptx)

</details>
