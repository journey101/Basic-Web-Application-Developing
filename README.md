# ds-sc3-project
section3-project

※ 프로젝트 설명
  : 본 프로젝트는 코드스테이츠 데이터사이언스(1기) 과정의 섹션3(데이터엔지니어링-웹애플리케이션) 4주차에 진행한 과제입니다. 

1. 서비스 기획의도
  : twitter 유저들의 텍스트 데이터를 머신러닝 예측모델(RandomForest)을 활용해 분석, 특정 키워드별로 적합한 브랜드명을 예측해주는 서비스를 의도하였습니다. 

2. 서비스 기능요약
  : Twitter api 에서 user data(username, tweet text)를 받아올 수 있고, 
    분석을 원하는 브랜드or특정유저의 이름(username)을 넣으면 해당 유저의 트윗 게시글 내용이 DB에 축적하고,
    머신러닝 예측모델(Random Forest)로 특정 키워드에 대하여 가장 적합한 브랜드or특정유저 이름의 예측값을 보여주는 기본적인 웹 애플리케이션 개발에 필요한 CRUD(Create(생성), Read(읽기), Update(갱신), Delete(삭제))를 훈련하기 위한 프로젝드입니다. 
