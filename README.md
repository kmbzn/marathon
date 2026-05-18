# Project Overview

![](https://images.unsplash.com/photo-1596727362302-b8d891c42ab8?q=80&w=1085&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

마라톤은 인간의 한계에 도전하는 스포츠로, 철저한 페이스 조절(Pacing Strategy)과 환경적 요인(Environmental Factors)이 완주 성공의 여부를 결정합니다. 본 프로젝트는 Kaggle에 공개된 보스턴 마라톤 데이터셋을 바탕으로, 러너의 개인 프로필과 구간별 데이터가 최종 완주 시간(Official Finish Time)에 미치는 영향을 심층 분석합니다.

This project leverages demographic, environmental, and in-race behavioral data to build robust predictive models. We focus not only on regression accuracy but also on explaining the phenomenon of **"Hitting the Wall" (30km 지점 이후의 급격한 페이스 저하)** through advanced data visualization and feature engineering.

---

## Team Members

본 프로젝트는 한양대학교 컴퓨터소프트웨어학부 학생들로 구성된 팀에 의해 공동 관리 및 개발됩니다.

| 이름 | 소속
| --- | ---
| **양종빈** | Hanyang Univ. CSE |
| **성시훈** | Hanyang Univ. CSE |
| **김병준** | Hanyang Univ. CSE |
| **임성현** | Hanyang Univ. CSE |

---

## Key Objectives

1. **Exploratory Data Analysis**
  * 나이(Age)와 성별(Gender)에 따른 마라톤 페이스 유지 능력의 상관관계 도출
  * 기온(Temperature) 및 날씨 변화가 러너들의 후반부 기록 저하에 미치는 영향 시각화
2. **Feature Engineering)**
  * 구간별 페이스 데이터를 활용하여 러너의 페이스 일관성을 나타내는 'Fatigue Index(피로도 지수)' 및 'Pacing Variance' 산출
3. **Predictive Modeling**
  * 선형 회귀(Linear Regression)부터 트리 기반 앙상블 모델(Random Forest, XGBoost, LightGBM)까지 다양한 회귀 알고리즘 비교 평가
4. **Actionable Insights Generation**
  * 분석 결과를 바탕으로 아마추어 러너 및 코칭 스태프가 참조할 수 있는 데이터 기반의 최적 페이스 전략 제안

---

## 📊 Dataset Description

본 프로젝트는 Kaggle의 **Boston Marathon Dataset**을 기반으로 합니다. 데이터셋은 다음과 같은 핵심 변수(Features)들을 포함하고 있습니다.

### 1. Demographic Data

* `Age`: 러너의 만 나이 (Numeric)
* `M/F`: 러너의 성별 (Categorical)
* `Country` / `State`: 러너의 국적 및 거주 지역

### 2. In-Race Split Times

* 5K, 10K, 15K, 20K, Half, 25K, 30K, 35K, 40K 지점의 통과 시간 및 페이스 기록

### 3. Environmental Data

* `Temperature`: 대회 당일의 평균 기온 (°C)
* `Weather`: 기후 조건 (맑음, 흐림, 우천 등)

### 4. Target Variable

* `Official Time`: 최종 마라톤 완주 시간 (HH:MM:SS 형식을 초 단위 변환하여 사용)

---

## 🛠 Methodology & Pipeline

### 1. Data Preprocessing

* **Missing Value Imputation:** 중도 포기자(DNF) 및 결측치 처리
* **Data Transformation:** 문자열로 되어 있는 시간 데이터(`HH:MM:SS`)를 수치형(Seconds) 데이터로 전환
* **Encoding:** 성별 및 국적 등 범주형 변수의 One-Hot Encoding 적용

### 2. Feature Engineering

후반부 기록 예측의 정확도를 높이기 위해 수학적 지표를 변수로 추가합니다.

* **Fatigue Index (피로 지수):** 30K 이후 페이스와 초반 10K 페이스의 변화율을 측정합니다.

### 3. Model Training & Evaluation

예측 모델의 성능 평가는 수치형 데이터의 오차를 판단하는 대표적인 지표인 RMSE (Root Mean Squared Error)와 결정계수인 **$R^2$ Score**를 기준으로 합니다.

* **사용 알고리즘:**
* Ridge / Lasso Regression
* Random Forest Regressor
* XGBoost / LightGBM Regressor

---

## 📁 Project Structure

```text
├── data/                  # Raw and processed dataset files
├── notebooks/             # Jupyter Notebooks for EDA and prototyping
│   ├── 01_eda_visualization.ipynb
│   └── 02_model_training.ipynb
├── src/                   # Source code for production
│   ├── __init__.py
│   ├── preprocessing.py   # Data cleaning and engineering
│   └── models.py          # Model architecture and evaluation
├── README.md              # Project documentation
└── requirements.txt       # Dependency list

```

---

## 🚀 How to Run

### Prerequisites

본 프로젝트를 local 환경에서 실행하려면 `Python 3.8` 이상의 버전이 필요합니다.

### Installation & Execution

1. 리포지토리를 clone합니다.
```bash
git clone https://github.com/kmbzn/marathon.git)
cd marathon
```
2. 필요한 라이브러리 및 의존성 파일을 설치합니다.
```bash
pip install -r requirements.txt
```
3. (optional) 전처리 및 모델 학습 스크립트를 실행하거나 `notebooks/` 디렉토리의 jupyter notebook을 실행할 수 있습니다.
```bash
jupyter notebook notebooks/01_eda_visualization.ipynb
```

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details. 본 프로젝트의 코드와 분석 결과는 MIT 라이선스 하에 자유로운 복사, 수정, 배포 및 상업적 이용이 가능합니다.
