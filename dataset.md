---
title: II. Datasets
layout: default
nav_order: 3
---

# II. Datasets
{: .no_toc }

<details open markdown="block">
  <summary>목차</summary>
{: .text-delta }
- TOC
{:toc}
</details>

---

본 프로젝트는 Kaggle의 **Boston Marathon Dataset**을 기반으로 합니다. 주요 변수(Features)는 다음과 같습니다.

## 1. Demographic Data
- `Age` — 러너의 만 나이 (Numeric)
- `M/F` — 성별 (Categorical)
- `Country` / `State` — 국적 및 거주 지역

## 2. In-Race Split Times
- 5K, 10K, 15K, 20K, Half, 25K, 30K, 35K, 40K 지점의 통과 시간 및 페이스 기록

## 3. Environmental Data
- `Temperature` — 대회 당일 평균 기온 (°C)
- `Weather` — 기후 조건 (맑음, 흐림, 우천 등)

## 4. Target Variable
- `Official Time` — 최종 완주 시간 (HH:MM:SS → 초 단위로 변환하여 사용)

> 🚧 데이터 출처 링크와 샘플 행(표)을 6/9 전까지 추가하세요.
