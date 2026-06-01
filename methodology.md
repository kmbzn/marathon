---
title: III. Methodology
layout: default
nav_order: 4
---

# III. Methodology
{: .no_toc }

<details open markdown="block">
  <summary>목차</summary>
{: .text-delta }
- TOC
{:toc}
</details>

---

## 1. Data Preprocessing
- **결측치 처리** — 중도 포기자(DNF) 및 결측 구간 처리
- **데이터 변환** — 문자열 시간(`HH:MM:SS`)을 수치형(Seconds)으로 전환
- **인코딩** — 성별·국적 등 범주형 변수 One-Hot Encoding

## 2. Feature Engineering
후반부 기록 예측 정확도를 높이기 위해 수학적 지표를 추가합니다.

- **Fatigue Index (피로 지수)** — 30K 이후 페이스와 초반 10K 페이스의 변화율
- **Pacing Variance** — 구간별 페이스의 분산(일관성)

## 3. Model Training & Evaluation
성능 지표는 **RMSE**(Root Mean Squared Error)와 **R² Score**를 사용합니다.

사용 알고리즘:

- Ridge / Lasso Regression
- Random Forest Regressor
- XGBoost / LightGBM Regressor

> 🚧 각 모델의 하이퍼파라미터·학습 설정은 코드와 함께 정리해 추가하세요.
