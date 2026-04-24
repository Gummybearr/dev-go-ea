# EA Part 2 Week 1 Day 1

기준일: 2026-04-24  
가정: 하루 `5시간`

이 파일은 Part 2 시작용 `Day 1 전용` 노트다.  
목표는 `entity classification + form flow`를 머리에 넣는 것이다.

## 오늘 핵심 원칙

Part 2 Day 1에서 가장 중요한 문장은 이것이다.

`Entity first, tax level second, form third.`

문제를 보면 먼저 아래를 순서대로 본다.

- entity가 무엇인가
- 누가 세금을 내는가
- 어떤 return을 쓰는가
- K-1이 나오는가
- basis / E&P / separately stated items 중 무엇이 중요한가

## 오늘 꼭 잡을 것

- `sole prop / disregarded single-member LLC` -> owner level taxation, `Schedule C`, `K-1 없음`
- `partnership / default multi-member LLC` -> `Form 1065`, `K-1`, pass-through, `partner basis`
- `C corp` -> `Form 1120`, entity-level tax, `E&P`
- `S corp` -> `Form 1120S`, `K-1`, pass-through, `shareholder basis`, qualification rules
- `trust / estate` -> `Form 1041`, 보통 `K-1` 흐름
- `exempt org` -> `Form 990 series`, 면세여도 filing issue 존재

## 한 장으로 외울 표

| Entity | Taxed Where | Main Return | K-1 | 제일 자주 틀리는 것 |
|---|---|---|---|---|
| Sole proprietorship | Owner | `Schedule C` | No | hobby vs business, SE tax |
| Single-member LLC default | Owner | 보통 `Schedule C` | No | LLC를 tax type 자체로 착각 |
| Partnership | Pass-through | `Form 1065` | Yes | guaranteed payment, partner basis |
| C corporation | Entity | `Form 1120` | No | E&P, dividends, redemptions |
| S corporation | Pass-through | `Form 1120S` | Yes | qualification, shareholder basis |
| Trust / Estate | Entity or beneficiary flow | `Form 1041` | Often | DNI, K-1 흐름 |
| Exempt organization | Generally exempt | `Form 990 series` | No | UBTI, filing requirement |

## 오늘의 트리거 문장

- `LLC`가 보이면 먼저 `어떻게 과세되지?`를 묻는다
- `K-1`이 보이면 바로 `pass-through + basis`를 떠올린다
- `distribution`이 보이면 먼저 `C corp인지 S corp인지`를 가른다
- `loss`가 보이면 pass-through에서는 거의 항상 `basis`를 먼저 본다

## 오늘 5시간 루틴

- `60분`: IRS sample questions와 outline 훑기
- `60분`: 위 entity 표를 손으로 다시 쓰기
- `90분`: entity classification / basic entity choice 문제 `20~25문제`
- `60분`: `1065 / 1120 / 1120S / 2553` 역할 정리
- `30분`: 오답노트
- `30분`: 마지막 복습

## 오늘 산출물

- `Entity comparison table`
- `Core forms radar`
- `Day 1 오답 Top 5`

## Day 1 미니퀴즈

답안은 `1B 2C ...` 형식으로 정리해서 스스로 채점하거나 튜터와 검토한다.

### 문제

1. A single-member LLC with no election is generally treated as:
   - A. A C corporation
   - B. A disregarded entity
   - C. A partnership
   - D. An S corporation

2. Which form is generally used by a partnership?
   - A. Form 1120
   - B. Form 1120S
   - C. Form 1065
   - D. Form 1041

3. Which concept is especially central in many C corporation distribution questions?
   - A. Filing status
   - B. E&P
   - C. SE tax
   - D. FBAR

4. Which form is commonly associated with electing S corporation status?
   - A. Form 2553
   - B. Form 4562
   - C. Form 4797
   - D. Form 3115

5. Absent an election, a multi-member LLC is generally treated as:
   - A. A C corporation
   - B. An S corporation
   - C. A partnership
   - D. A sole proprietorship

6. In an S corporation loss question, what should you usually check first?
   - A. Child tax credit
   - B. Shareholder basis
   - C. Standard deduction
   - D. FBAR threshold

7. If a question mentions K-1 and separately stated items, what should come to mind first?
   - A. Wage withholding
   - B. Pass-through entity
   - C. Exempt organization only
   - D. Estate tax only

8. A sole proprietor generally reports business activity on:
   - A. Form 1065
   - B. Form 1120
   - C. Schedule C
   - D. Form 990

### 정답

`1B 2C 3B 4A 5C 6B 7B 8C`

## 공식 출처

- IRS SEE Part 2 Sample Questions: https://www.irs.gov/tax-professionals/enrolled-agents/see-sample-test-questions-part-2
- Archived SEE Part 2 Outline PDF: https://www.prometric.com/files/2021-01/SEE%202%20Clean.pdf
