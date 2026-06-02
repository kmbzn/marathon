---
title: Home
layout: default
nav_order: 1
description: 프로젝트 개요 및 목차
---

# 마라톤 완주 시간 예측
{: .fs-8 }

인구통계학적 특성과 대기 온도를 반영한 머신러닝 기반 완주 시간 예측  
한양대학교 컴퓨터소프트웨어학부 · AI+X: Deep Learning (2026 Spring)
{: .fs-5 .fw-300 }

---

## 목차 (Table of Contents)

1. [**Proposal**]({% link proposal.md %}) — 동기와 목표
2. [**Datasets**]({% link dataset.md %}) — 보스턴 마라톤 데이터셋
3. [**Methodology**]({% link methodology.md %}) — 전처리 · 피처 · 모델
4. [**Evaluation & Analysis**]({% link evaluation.md %}) — 결과 · 그래프 · 지표
5. [**Related Work**]({% link related-work.md %}) — 참고 자료 · 도구
6. [**Conclusion**]({% link conclusion.md %}) — 논의 · 역할분담 · 발표 영상

---

## Overview

마라톤은 인간의 한계에 도전하는 스포츠로, 철저한 페이스 조절(Pacing Strategy)과 환경적 요인(Environmental Factors)이 완주 성공 여부를 결정합니다. 본 프로젝트는 Kaggle에 공개된 **보스턴 마라톤 데이터셋**을 바탕으로, 러너의 개인 프로필과 구간별 데이터가 최종 완주 시간(Official Finish Time)에 미치는 영향을 심층 분석합니다.

나이, 성별, 구간별 페이스, 기온 등의 변수를 활용해 완주 시간을 예측하고 결과를 시각화합니다. 특히 **"Hitting the Wall"(30km 지점 이후의 급격한 페이스 저하)** 현상을 피처 엔지니어링과 데이터 시각화로 설명하는 데 초점을 둡니다.
