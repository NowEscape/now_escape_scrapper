# 지금, 방탈출
:lock: 예약 가능한 방탈출을 찾으려 모든 방탈출 매장 홈페이지를 방문하는 방탈출러 <br/>
:unlock: 이젠 지금, 방탈출 어플을 이용하여 예약 가능한 방탈출을 쉽고 빠르게 찾을 수 있어요!

<br/>
<div align="center">
  <img src="https://user-images.githubusercontent.com/49519059/221346839-59c489f5-b370-464c-86d0-4d786b9229cf.png" width="20%">
  <img src="https://user-images.githubusercontent.com/49519059/221346843-871ccf36-2957-439c-bc33-4f5aabb9771d.png" width="20%">
	<img src="https://user-images.githubusercontent.com/49519059/221346844-713e42fd-684b-4ae3-9879-1d7555467304.png" width="20%">
	<img src="https://user-images.githubusercontent.com/49519059/221346845-35046fe9-0f4b-4f3e-ba45-9c10dcb8ba19.png" width="20%">
</div>
<br/>

## 설치 방법
Android : https://play.google.com/store/apps/details?id=com.now_escape.now_escape&pli=1 <br/>
ios : https://apps.apple.com/kr/app/%EC%A7%80%EA%B8%88-%EB%B0%A9%ED%83%88%EC%B6%9C/id6445975673

<br/>

## 업데이트 내역
- 0.1.0 : Android, ios 출시
	
<br/>

## project 설명
- 방탈출 테마들에 대해 일정 주기마다 예약가능한 시간대를 스크래핑하여 db에 저장



## 사용한 주요 라이브러리
- bs4 : selenium으로 모두 처리하기에는 성능이 너무 안 좋고, scrapy 프레임워크를 도입하기에는 이미 어느 정도 스크래핑이 진행된 상황이라 새로운 프로젝트를 만들기에는 부담스러웠음. 그래서 라이브러리인 bs4 도입
- selenium : 스크래핑하기 위해 사용한 라이브러리. bs4, scrapy 대신, 동적인 처리가 필요할 때 selenium을 사용함.
- APschduler : 일정시간마다 작업을 수행하기 위해 사용한 라이브러리. crontab, celery 대신, 가볍지만 관리가 편리한 방법을 사용하기 위해 APschduler를 사용함. 
