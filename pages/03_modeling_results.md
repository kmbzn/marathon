---
title: "모델 학습 & 평가 결과"
layout: default
nav_order: 3
parent: "IV. Evaluation & Analysis"
---

# 모델 학습 및 평가 결과

> **분석 노트북**: [`03_modeling_and_evaluation.ipynb`](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/03_modeling_and_evaluation.ipynb)

---

## Experimental Setup

두 가지 예측 시나리오를 비교합니다.

| 시나리오 | 사용 피처 | 실용적 의미 |
|----------|-----------|-------------|
| **Full Model** | 30K 기록까지 + 인구통계 + Fatigue Index | 레이스 후반 기록 예측 |
| **Early Model** | 10K 기록까지 + 나이/성별 + Fatigue Index | 레이스 초반 완주 시간 예측 |

- Train/Test Split: 80% / 20% (random_state=42)
- Train: 21,061명 / Test: 5,266명
- 평가 지표: RMSE (낮을수록 좋음), R² (높을수록 좋음)

---

## Full Model Results

| 모델 | RMSE | R² |
|------|------|-----|
| **Ridge Regression** | **1.61분 (97초)** | **0.9984** |
| Lasso Regression | 1.61분 (97초) | 0.9984 |
| Random Forest | 1.99분 (119초) | 0.9975 |
| XGBoost | 2.86분 (172초) | 0.9948 |
| LightGBM | 2.78분 (167초) | 0.9951 |

**해석**: 30K 기록까지 알고 있을 때 완주 시간을 평균 **±1.6분** 오차로 예측합니다. 30K 누적 기록이 최종 기록과 거의 선형적으로 연결되기 때문에 Ridge 같은 선형 모델이 가장 우수한 성능을 보입니다.

---

## Early Model Results (up to 10K)

| 모델 | RMSE | R² |
|------|------|-----|
| Ridge (Early) | 5.37분 (322초) | 0.9821 |
| **Random Forest (Early)** | **4.00분 (240초)** | **0.9901** |
| XGBoost (Early) | 4.32분 (259초) | 0.9884 |
| LightGBM (Early) | 4.35분 (261초) | 0.9882 |

**해석**: 레이스 초반 10K 기록만으로도 완주 시간을 평균 **±4분** 오차로 예측합니다. Early Prediction에서는 비선형 모델(RF)이 선형 모델을 앞서며, 초반 페이스와 최종 기록 사이의 복잡한 패턴을 더 잘 포착합니다.

---

## Model Performance Log

```
=== Full Model ===
Ridge               RMSE = 1.61 min (97s)    R² = 0.9984
Lasso               RMSE = 1.61 min (97s)    R² = 0.9984
Random Forest       RMSE = 1.99 min (119s)   R² = 0.9975
XGBoost             RMSE = 2.86 min (172s)   R² = 0.9948
LightGBM            RMSE = 2.78 min (167s)   R² = 0.9951

=== Early Prediction (10K 기준) ===
Ridge (Early)       RMSE = 5.37 min (322s)   R² = 0.9821
RF (Early)          RMSE = 4.00 min (240s)   R² = 0.9901
XGBoost (Early)     RMSE = 4.32 min (259s)   R² = 0.9884
LightGBM (Early)    RMSE = 4.35 min (261s)   R² = 0.9882
```

---

## Random Forest Feature Importance

| 순위 | 피처 | 중요도 |
|------|------|--------|
| 1 | `30K_s` (30K 누적 기록) | **0.9656** |
| 2 | `Fatigue_Index` | 0.0178 |
| 3 | `Pacing_Variance` | 0.0128 |
| 4 | `25K_s` | 0.0009 |
| 5 | `Half_s` | 0.0007 |
| 6–11 | 나머지 구간 기록, Age, Gender | < 0.001 |

**주요 발견**: 30K 구간 기록이 전체 예측력의 96.6%를 차지합니다. 30K까지 어떤 속도로 달렸는지가 최종 기록을 거의 결정한다는 의미입니다. Fatigue Index(피로도 지수)가 두 번째 중요 변수로, 페이스 관리의 중요성을 뒷받침합니다.

---

## Prediction Accuracy Analysis

Ridge Full Model의 Residual 분포는 평균 0 근처에서 대칭적인 정규분포를 보이며, 이는 모델이 체계적인 편향 없이 잘 작동하고 있음을 나타냅니다.

```
잔차 분포:
  - 95% 구간: ±3분 이내
  - 5분 이상 오차: 전체의 약 2%
```