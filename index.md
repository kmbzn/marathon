---
title: Home
layout: default
nav_order: 1
description: 프로젝트 개요 및 목차
---

# 마라톤 완주 시간 예측
{: .fs-8 }

인구통계학적 특성과 페이스 패턴을 반영한 머신러닝 기반 완주 시간 예측  
AI+X: Deep Learning (2026 Spring)
{: .fs-5 .fw-300 }

<div style="max-width:720px;margin:1.5rem auto;">
  <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
    <iframe
      src="https://www.youtube.com/embed/EL9nypUBUn0"
      title="마라톤 완주 시간 예측 프로젝트 발표"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      style="position:absolute;top:0;left:0;width:100%;height:100%;">
    </iframe>
  </div>
  <img src="https://images.unsplash.com/photo-1596727362302-b8d891c42ab8?q=80&w=1085&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" style="width:100%;margin-top:1rem;display:block;" alt="">
</div>

---

## Overview

마라톤은 인간의 한계에 도전하는 스포츠로, 철저한 페이스 조절이 완주 성공 여부를 결정합니다. 본 프로젝트는 Kaggle의 **Boston Marathon Dataset**을 바탕으로, 러너의 개인 프로필과 구간별 데이터가 최종 완주 시간에 미치는 영향을 분석합니다. 특히 **Hitting the Wall**(30km 이후 급격한 페이스 저하) 현상을 정량적으로 분석하고 머신러닝 모델로 완주 시간을 예측하고자 합니다.

---

## Results

| 단계 | 설명 | 결과 페이지 | 노트북 |
|------|------|-------------|--------|
| 1. EDA | 성별·나이 분포, 상관관계 시각화 | [보기]({{ site.baseurl }}{% link pages/01_eda_results.md %}) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/01_eda_visualization.ipynb) |
| 2. 전처리 & 피처 엔지니어링 | Fatigue Index, Pacing Variance 산출 | [보기]({{ site.baseurl }}{% link pages/02_preprocessing_results.md %}) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/02_preprocessing_and_feature_engineering.ipynb) |
| 3. 모델 학습 & 평가 | RMSE/R² 비교, 피처 중요도 분석 | [보기]({{ site.baseurl }}{% link pages/03_modeling_results.md %}) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/03_modeling_and_evaluation.ipynb) |
| 4. 인사이트 & 결론 | Hitting the Wall 분석, 페이스 전략 제안 | [보기]({{ site.baseurl }}{% link pages/04_insights.md %}) | — |

---

## Table of Contents

1. [**Proposal**]({{ site.baseurl }}{% link proposal.md %}) — 동기와 목표
2. [**Datasets**]({{ site.baseurl }}{% link dataset.md %}) — 보스턴 마라톤 데이터셋
3. [**Methodology**]({{ site.baseurl }}{% link methodology.md %}) — 전처리 · 피처 · 모델
4. [**Evaluation & Analysis**]({{ site.baseurl }}{% link evaluation.md %}) — 결과 · 그래프 · 지표
5. [**Related Work**]({{ site.baseurl }}{% link related-work.md %}) — 참고 자료 · 도구
6. [**Conclusion**]({{ site.baseurl }}{% link conclusion.md %}) — 논의 · 역할분담 · 발표 영상

---

## Team Members

| 이름 | 소속 | 이메일 |
| --- | --- | --- |
| **양종빈** | Hanyang Univ. CSE | goldon102@gmail.com |
| **성시훈** | Hanyang Univ. CSE | sihun0415@gmail.com |
| **김병준** | Hanyang Univ. CSE | kmbzn24@gmail.com |
| **임성현** | Hanyang Univ. CSE | beo00325@gmail.com |

---

## Key Findings

- 전체 러너의 **47.9%**가 후반부에 10% 이상 페이스 저하를 경험 (Hitting the Wall)
- **30K 기록**이 완주 시간 예측 기여도의 **96.6%** 차지 (Random Forest Feature Importance)
- 10K 기록만으로도 완주 시간을 **±4분 오차**로 예측 가능 (R² = 0.990)
- Ridge Regression RMSE **1.61분**, R² **0.9984** 달성 (Full Model 최고 성능)