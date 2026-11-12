<div align="center">

## 박효진 | Hyojin Park

**데이터를 분석하고, 필요한 시스템을 구현하는 데이터 분석가입니다.**

M.S. Statistics, @HUFS

B.S. Statistics, @HUFS

</div>

---

### 🚀 Summary

- **통계 연구 및 모델링** — 이산형 생존자료를 위한 새 생존모형을 제안하고 시뮬레이션·실데이터로 검증
- **실무 데이터 분석** — 다기관 EMR·청구자료 기반 비교효과·생존분석, 치료제 시장 점유율·신규 처방·치료 경로 분석
- **통계적 해석과 결과 전달** — 생존분석·성향점수·메타분석 결과를 연구진이 이해할 수 있는 표·그래프·보고서로 정리
- **AI 활용 및 시스템 구현** — AI 코딩 도구로 개인 금융 대시보드, 데이터 분석 도구, 업무 자동화 프로그램을 기획·구현

### 🔎 Profile

**👩‍💻 Experience**

- `2025.07 ~ 재직 중` **에비드넷** 데이터사이언스팀 — 다기관 RWD/RWE 분석, 치료제 시장·마케팅 리서치, 코호트 구축·통계분석
- `2024.10 ~ 2025.06` **분당서울대학교병원** 외부 분석연구원 — 전국 단위 청구자료 기반 CML 치료 성과·생존·의료비 분석

**🎓 Education**

- `2024.09 ~ 2026.02` **한국외국어대학교 통계학 석사** (학·석사 연계)
- `2021.03 ~ 2024.08` **한국외국어대학교 통계학 학사** (학·석사 연계)

### 📝 Tech Stack

![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![SAS](https://img.shields.io/badge/SAS-0766D1?style=flat-square)
![R Shiny](https://img.shields.io/badge/R%20Shiny-1A162D?style=flat-square&logo=rstudioide&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

![Claude](https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=claude&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-000000?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white)

- **Data** — OMOP-CDM · EMR · Claims Data · Cohort Definition · Data QC
- **Methods** — Survival Analysis · Cox Regression · PSM / PS Weighting · Meta-analysis
- **Market Research** — Market Share · Treatment Pathway Analysis
- **AI & Automation** — Claude Code · Codex · Ollama (Local LLM) · n8n

### 🤖 AI & Automation

> 반복적인 작업을 줄이거나 기존 서비스로 해결하기 어려운 문제를 발견했을 때, 필요한 도구를 직접 만들어 사용해 왔습니다.

- **Workflow Automation** — n8n·iPhone 단축어로 콘텐츠 수집 → AI 요약 → Notion 기록 자동화
- **분석 도구 개발** — R Shiny 기반 데이터 탐색·QC 도구, 통계 산출물 점검 프로그램
- **데이터 서비스 개발** — 개인 금융 대시보드와 소비 예측 시스템, 로컬 PDF 도구
- **AI 코딩·Local LLM** — Claude Code·Codex로 기능 구현·개선, Ollama로 로컬 요약·분류 워크플로

### 🛠️ What I Build

> 분석에 반복해서 쓰는 로직은 R 패키지로, 불편한 일은 작은 앱으로 만듭니다. (저장소는 비공개)

**🧪 R Analysis Toolkit** — 테스트와 예제를 갖춘 R 패키지 9종

| Package | 하는 일 |
|:---|:---|
| `r-km-curve` | Kaplan-Meier·누적 사건 곡선, risk table, log-rank |
| `r-baseline-table1` | 군별 기저 특성표(Table 1), PSM 전후 비교 |
| `r-table1-excel` | Table 1을 서식 있는 Excel로 내보내기 |
| `r-cohort-flow` | 대상자 선정 인원 검증과 흐름도 |
| `r-grace-period` | 처방 기록으로 치료 에피소드 만들기 |
| `r-persistence` | 치료 지속성 판정 |
| `r-discontinuation` | 치료 중단일·전환·중도절단 정리 |
| `r-sankey-diagram` | 용량·치료 상태 전이 Sankey 다이어그램 |
| `r-paired-change` | 전후 짝지은 측정값 변화 요약·검정 |

**🏥 RWD 업무 도구**
- `cdm-dq` — 병원 간 OMOP CDM 데이터 품질 비교
- `drb-checker` — 데이터 반출 심의 전 Excel·Word의 식별 위험 값 사전 점검
- `work-studio` — 업무 기록·주간업무·반출 점검·PDF·프롬프트를 한 창에서

**🤖 AI & Automation**
- `ai-automation-server` — 링크를 로컬 AI가 요약해 Notion에 저장
- `clipboard-ai` — 복사한 글을 로컬 AI로 다듬는 메뉴바 앱
- `work-memory-plugin` — Claude·Codex가 업무 기록을 이어 쓰게 하는 플러그인
- `skill-hub` — Claude Code·Codex Skill을 찾고 비교하고 관리하는 Mac 앱

**🦎 Personal Apps**
- `reptile-care` — 키우는 팻테일 게코 '콩이'의 다마고치형 사육일지
- `local-pdf-studio` — 내 컴퓨터 안에서만 PDF 합치기·나누기·변환
- `photo-nest` — 로컬에서만 도는 AI 사진 라이브러리
- `project-dashboard` — 서버·앱·프로젝트 현황을 한곳에서

<img src="assets/langs.svg" alt="Most used languages" />

### 📂 Projects

| Project | Description | Keywords |
|:---:|:---|:---|
| 다기관 RWD 치료 패턴 연구 | OMOP-CDM 기반 장기 치료 패턴·비교효과 분석 | RWE, Cohort, Survival |
| 치료제 시장 리서치 | 시장 점유율·신규 처방·치료 경로 분석 | Market Research |
| 산출물 disclosure 검사 도구 | 통계 산출물의 재식별 위험 사전검사 | Privacy, Automation |
| CML 치료성과 연구 | 건강보험 청구자료 기반 장기 outcome·의료비 분석 | Claims, Cox |
| 석사논문 | Alternative discrete hazard 기반 이산형 생존모형 제안 | Survival Model |
| 개인 금융 대시보드 | 금융 데이터 대시보드와 소비 예측 시스템 | Dashboard, Forecasting |
| 콘텐츠 자동화 | n8n·iPhone 단축어로 수집 → AI 요약 → Notion 기록 | n8n, Local LLM |

### 📧 Contact

- Email: [blacklaye0322@naver.com](mailto:blacklaye0322@naver.com)
- Portfolio: [Notion Portfolio](https://app.notion.com/p/Hyojin-Park-Portfolio-3ffca625b3e081caae35c21376fa154e)
<!-- - LinkedIn: [LinkedIn](링크드인 주소) -->

---

<div align="center">

<img src="assets/gecko.svg" alt="콩이가 잔디를 먹는 중" width="100%" />

<sub>🦎 콩이가 잔디를 먹는 중 · 매일 자정 갱신</sub>

</div>
