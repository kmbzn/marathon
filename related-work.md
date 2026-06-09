---
title: V. Related Work
layout: default
nav_order: 6
---

# V. Related Work

---

## 1. Tools & Libraries

| 도구 / 라이브러리 | 버전 | 용도 |
|:---|:---|:---|
| **Python** | 3.8+ | 전체 분석 환경 |
| **pandas** | 2.x | 데이터 로드, 정제, 변환 |
| **NumPy** | 1.x | 수치 연산, 배열 처리 |
| **scikit-learn** | 1.x | Ridge/Lasso 회귀, 전처리, 평가 지표 |
| **XGBoost** | 1.7+ | 그래디언트 부스팅 회귀 |
| **LightGBM** | 3.x | 리프 단위 성장 그래디언트 부스팅 |
| **Matplotlib** | 3.x | 기본 시각화, 그래프 출력 |
| **Seaborn** | 0.x | 통계적 시각화, 히트맵, 분포 플롯 |
| **Jupyter Notebook** | — | EDA 및 프로토타이핑 환경 |

### Installation

```bash
pip install -r requirements.txt
```
requirements.txt
pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
xgboost>=1.7
lightgbm>=3.3
matplotlib>=3.7
seaborn>=0.12
jupyter

---

## 2. Datasets

| 이름 | 출처 | 설명 |
|:---|:---|:---|
| **Boston Marathon Results (2015–2017)** | [Kaggle — rojour/boston-results](https://www.kaggle.com/datasets/rojour/boston-results) | 본 프로젝트의 핵심 데이터셋. 연도별 완주 기록·구간 시간·인구통계 포함 |
| **Boston Marathon Qualifiers Dataset** | [Kaggle — runningwithrock](https://www.kaggle.com/datasets/runningwithrock/boston-marathon-qualifiers-dataset) | BQ(보스턴 자격 기록) 기준 데이터. 참가 자격 분석 참고용 |

---

## 3. Related Work

### 3-1. Hitting the Wall — Pace Collapse Analysis

**[1] Smyth, B. (2021). How recreational marathon runners hit the wall: A large-scale data analysis of late-race pacing collapse in the marathon.**
*PLOS ONE*, 16(5), e0251513.
[https://doi.org/10.1371/journal.pone.0251513](https://doi.org/10.1371/journal.pone.0251513)

> 400만 건 이상의 마라톤 기록을 분석하여 Hitting the Wall(HTW)을 페이스 기반으로 정의하고, 발생 비율·성별·연령·능력 수준에 따른 차이를 대규모로 분석한 연구. **전체 러너의 약 34%가 HTW를 경험**하며, 남성(28%)이 여성(17%)보다 유의미하게 높은 발생률을 보임. 본 프로젝트의 Fatigue Index 설계 및 30K 기준 구간 설정의 이론적 근거로 활용.

---

**[2] Berndsen, J., Lawlor, A., & Smyth, B. (2020). Exploring the wall in marathon running.**
*Journal of Sports Analytics*, 6(3), 173–186.
[https://doi.org/10.3233/JSA-200354](https://doi.org/10.3233/JSA-200354)

> K-Means 클러스터링을 활용해 마라톤 페이싱 프로필을 HTW 발생 그룹과 미발생 그룹으로 분류하고, Onset·Pace Collapse·Slowdown·Distance 4개 랜드마크 지표로 Wall을 정의한 연구. 본 프로젝트의 Pacing Variance 및 구간별 페이스 특징 추출 방법론에 직접적인 영향을 줌.

---

### 3-2. Finish Time Prediction Models

**[3] Atterfors, J. & Lamm, J. (2023). Machine Learning of Pacing Patterns for Half Marathon.**
*Springer Lecture Notes in Computer Science*.
[https://doi.org/10.1007/978-3-031-31772-9_14](https://doi.org/10.1007/978-3-031-31772-9_14)

> 예테보리 하프 마라톤 42만 건 데이터(2010–2019)를 기반으로 완주 시간 예측과 HTW 위험 러너 식별 두 가지 과제에 머신러닝을 적용한 연구. **HTW 위험 러너의 70% 이상을 사전에 식별**하는 모델을 제안. 본 프로젝트의 분류 가능성 확장 방향 참고.

---

**[4] Journal of Technical Education Science (2025). Predicting Marathon Finishing Times Using Ensemble Learning: An Empirical Study on Boston Marathon Data.**
[https://jte.edu.vn/index.php/jte/article/view/1924](https://jte.edu.vn/index.php/jte/article/view/1924)

> 본 프로젝트와 동일한 Boston Marathon 2015–2017 데이터셋을 사용하여 KNN, ANN, LSTM, 앙상블 모델을 비교한 연구. Linear Regression + Random Forest + MLPRegressor ensemble이 **RMSE 11.06분, R² 0.928**로 최고 성능을 달성. 본 프로젝트의 모델 성능 Baseline으로 활용.

---

**[5] Smyth, B. et al. (2021). Recommendations for marathon runners: on the application of recommender systems and machine learning.**
*User Modeling and User-Adapted Interaction*, 32, 787–837.
[https://doi.org/10.1007/s11257-021-09299-3](https://doi.org/10.1007/s11257-021-09299-3)

> Strava·RunKeeper 훈련 데이터를 활용해 개인화 완주 시간 예측 및 페이스 플랜 추천 시스템을 구축한 연구. Case-Based Reasoning(CBR)과 다양한 회귀 알고리즘을 비교하며, 훈련 이력이 예측 정확도에 미치는 영향을 분석. 본 프로젝트의 향후 확장 방향(추천 시스템) 참고.

---

**[6] Smyth, B. & Cunningham, P. (2019). Pace my race: recommendations for marathon running.**
*ACM RecSys 2019*.
[https://doi.org/10.1145/3298689.3346991](https://doi.org/10.1145/3298689.3346991)

> 7,931건의 마라톤 데이터를 기반으로 레이스 중 실시간 완주 시간 예측 및 페이스 조정 추천 시스템을 제안한 연구. 기존 예측 방식 대비 유의미한 정확도 향상을 달성. 구간 기록이 누적될수록 예측 정확도가 높아지는 특성을 분석.

---

### 3-3. Weather Conditions & Marathon Performance

**[7] Ely, M. R. et al. (2007). Impact of weather on marathon-running performance.**
*Medicine & Science in Sports & Exercise*, 39(3), 487–493.

> 기온·습도·일사량·풍속 등 복합 기상 조건이 마라톤 완주 시간에 미치는 영향을 분석한 연구. **기온 상승에 따른 기록 저하는 비선형 패턴**을 보이며, 특히 빠른 러너일수록 기온 영향에 더 민감하게 반응함. 본 프로젝트의 기온 변수 설계 및 해석의 이론적 배경.

---

### 3-4. Missing Data Handling (2013 Boston Marathon)

**[8] Hammerling, D. et al. (2014). Completing the Results of the 2013 Boston Marathon.**
*PLOS ONE*, 9(4), e93800.
[https://doi.org/10.1371/journal.pone.0093800](https://doi.org/10.1371/journal.pone.0093800)

> 폭탄 테러로 중단된 2013년 보스턴 마라톤에서 약 6,000명의 DNF 러너 완주 시간을 KNN 기반 Matrix Completion으로 추정한 연구. 본 프로젝트의 DNF 결측치 처리 방법론 및 구간 시간 데이터의 통계적 활용 방식 참고.

---

## 4. Reference Documents

| 제목 | 링크 | 설명 |
|:---|:---|:---|
| XGBoost 공식 문서 | [xgboost.readthedocs.io](https://xgboost.readthedocs.io) | 하이퍼파라미터 설정 및 early stopping 레퍼런스 |
| LightGBM 공식 문서 | [lightgbm.readthedocs.io](https://lightgbm.readthedocs.io) | Leaf-wise 성장 원리 및 파라미터 가이드 |
| scikit-learn User Guide | [scikit-learn.org/stable/user_guide](https://scikit-learn.org/stable/user_guide.html) | Ridge/Lasso, 전처리, 평가 지표 레퍼런스 |
| Kaggle — Boston Marathon EDA | [rpubs.com/susan_li/boston-marathon](https://rpubs.com/susan_li/boston-marathon) | 2016년 보스턴 마라톤 데이터 탐색적 분석 예시 |
| Predicting Boston Marathon Finish Times (RPubs) | [rpubs.com/timlynch/STOR320FinalProject](https://rpubs.com/timlynch/STOR320FinalProject) | 동일 데이터셋 기반 회귀 분석 레퍼런스 |
