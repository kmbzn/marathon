# Project Overview

## 인구통계학적 특성과 페이스 패턴을 반영한 머신러닝 기반 마라톤 완주 시간 예측

![](https://images.unsplash.com/photo-1596727362302-b8d891c42ab8?q=80&w=1085&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

마라톤은 인간의 한계에 도전하는 스포츠로, 철저한 페이스 조절이 완주 성공의 여부를 결정합니다. 본 Project는 Kaggle에 공개된 보스턴 마라톤 데이터셋을 바탕으로, 러너의 개인 프로필과 구간별 데이터가 최종 완주 시간(Official Finish Time)에 미치는 영향을 심층 분석합니다.

나이, 성별, 구간별 페이스, **히팅 더 월(Hitting the Wall)** 현상을 정량적으로 분석하고, 여러 머신러닝 모델로 완주 시간을 예측합니다.

> **Hitting the Wall**: 30km 지점 이후 발생하는 급격한 페이스 저하 현상. 전체 러너의 47.9%가 경험.

---

## 분석 결과 보기

| 단계 | 설명 | 결과 페이지 | 노트북 |
|------|------|-------------|--------|
| 1. 탐색적 분석 (EDA) | 성별·나이 분포, 상관관계 시각화 | [결과 보기](pages/01_eda_results.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/01_eda_visualization.ipynb) |
| 2. 전처리 & 피처 엔지니어링 | Fatigue Index, Pacing Variance 산출 | [결과 보기](pages/02_preprocessing_results.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/02_preprocessing_and_feature_engineering.ipynb) |
| 3. 모델 학습 & 평가 | RMSE/R² 비교, 피처 중요도 분석 | [결과 보기](pages/03_modeling_results.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/03_modeling_and_evaluation.ipynb) |
| 4. 인사이트 & 결론 | 히팅 더 월 분석, 페이스 전략 제안 | [결과 보기](pages/04_insights.md) | — |

---

## Key Findings

- **30K 기록이 완주 시간의 96.6%를 결정** (Random Forest Feature Importance)
- **전체 러너의 47.9%**가 후반부에 10% 이상 페이스 저하를 경험
- 10K 기록만으로도 완주 시간을 **±4분 오차**로 예측 가능 (R² = 0.990)
- Ridge Regression으로 RMSE **1.62분**, R² **0.9983** 달성

---

## Team Members

본 Project는 한양대학교 컴퓨터소프트웨어학부 학생들로 구성된 팀에 의해 공동 관리 및 개발됩니다.

| 이름 | 소속 |
| --- | --- |
| **양종빈** | Hanyang Univ. CSE |
| **성시훈** | Hanyang Univ. CSE |
| **김병준** | Hanyang Univ. CSE |
| **임성현** | Hanyang Univ. CSE |

---

## Key Objectives

1. **Exploratory Data Analysis**
   - 나이(`Age`)와 성별(`M/F`)에 따른 마라톤 페이스 유지 능력의 상관관계 도출
   - 구간별 페이스 변화를 통한 히팅 더 월 현상 정량화
2. **Feature Engineering**
   - 구간별 페이스 데이터를 활용한 `Fatigue Index(피로도 지수)` 및 `Pacing Variance` 산출
3. **Predictive Modeling**
   - Ridge / Lasso Regression부터 Random Forest, XGBoost, LightGBM까지 비교 평가
4. **Actionable Insights**
   - 아마추어 러너를 위한 데이터 기반 최적 페이스 전략 제안

---

## 📁 Project Structure

```text
├── data/
│   ├── marathon_results_2015.csv      # Boston Marathon 2015 원본 데이터
│   ├── marathon_results_2016.csv      # Boston Marathon 2016 데이터
│   └── marathon_results_2017.csv      # Boston Marathon 2017 데이터
├── notebooks/
│   ├── 01_eda_visualization.ipynb     # 탐색적 데이터 분석
│   ├── 02_preprocessing_and_feature_engineering.ipynb
│   └── 03_modeling_and_evaluation.ipynb
├── pages/                             # 분석 결과 요약 페이지
│   ├── 01_eda_results.md
│   ├── 02_preprocessing_results.md
│   ├── 03_modeling_results.md
│   └── 04_insights.md
├── src/
│   ├── __init__.py
│   ├── preprocessing.py               # 데이터 정제·피처 엔지니어링 함수
│   └── models.py                      # 모델 학습·평가 함수
├── requirements.txt
└── README.md
```

---

## Dataset Description

본 Project는 Kaggle의 **Boston Marathon Dataset (2015–2017)** 을 기반으로 합니다.

| 카테고리 | 컬럼 | 설명 |
|----------|------|------|
| 인구통계 | `Age`, `M/F`, `Country` | 나이, 성별, 국적 |
| 구간 기록 | `5K` ~ `40K` | 5K 간격 누적 통과 시간 (HH:MM:SS) |
| 타겟 변수 | `Official Time` | 최종 완주 시간 → 초 단위로 변환 |

> **참가자 (2015)**: 26,598명 | **유효 데이터**: 26,357명 | **나이 범위**: 18–82세

---

## 🚀 How to Run

```bash
git clone https://github.com/kmbzn/marathon.git
cd marathon
pip install -r requirements.txt
jupyter notebook notebooks/01_eda_visualization.ipynb
```

또는 상단 표의 Colab 배지를 클릭해 바로 실행할 수 있습니다.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
