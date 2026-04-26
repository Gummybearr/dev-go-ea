# EA Part 1 Week 1 Day 2 Deep Dive: Filing Status

기준일: 2026-04-27
시험 법 기준: tax law through December 31, 2025
대상: `part-1-week-1-day-2-100-practice-questions.md`

Day 2는 `filing status`를 깊게 파는 날이다. Day 1에서 `Form 1040 flow`와 전체 지도를 봤다면, Day 2는 taxpayer가 어떤 출발선에 서는지 결정한다.

`Filing status`는 단순한 이름표가 아니다. `standard deduction`, tax rate structure, filing requirement, credit eligibility, deduction limitation에 영향을 준다.

중요: 이 자료는 비공개 실제 SEE 문제나 brain dump를 사용하지 않는다. IRS 공개 SEE sample question 형식과 IRS Publication 501/Form 1040 자료를 기준으로 만든 학습 자료다.

## 0. Day 2 약어

| 약어 / 용어 | 풀어쓴 말 | 의미 |
|---|---|---|
| `SEE` | `Special Enrollment Examination` | EA 시험 |
| `IRS` | `Internal Revenue Service` | 미국 연방 세무 당국 |
| `MFJ` | `Married Filing Jointly` | married taxpayers가 one joint return으로 filing |
| `MFS` | `Married Filing Separately` | married taxpayers가 separate returns로 filing |
| `HOH` | `Head of Household` | unmarried 또는 considered unmarried + home cost + qualifying person |
| `QSS` | `Qualifying Surviving Spouse` | spouse death 이후 일정 요건에서 가능한 surviving spouse status |

## 1. Day 2 한 줄 공식

`Start with December 31, then test special statuses.`

문제 읽는 순서:

1. taxpayer의 `marital status`를 December 31 기준으로 본다.
2. married이면 `MFJ` 또는 `MFS`에서 시작한다.
3. unmarried이면 `Single`, `HOH`, `QSS` 가능성을 본다.
4. spouse death가 있으면 year of death의 `MFJ`와 following years의 `QSS`를 구분한다.
5. child/home facts가 있으면 `HOH` 또는 `QSS`를 검토한다.
6. MFS가 나오면 credit/deduction limitation을 의심한다.

## 2. 기본 filing status 5개

| Status | 언제 보는가 | 시험 함정 |
|---|---|---|
| `Single` | year-end unmarried이고 더 좋은 status가 없을 때 | HOH 가능성을 안 보고 바로 Single 선택 |
| `MFJ` | married taxpayers가 joint return filing | joint liability, education credit eligibility |
| `MFS` | married taxpayers가 separate returns filing | credits/deductions 제한 |
| `HOH` | unmarried 또는 considered unmarried + home cost + qualifying person | home cost와 support를 섞음 |
| `QSS` | spouse death 이후 2년 window | year of death MFJ와 혼동 |

## 3. December 31 rule

일반적으로 `marital status`는 tax year의 마지막 날 기준이다. Calendar-year taxpayer는 December 31 기준으로 본다.

예시:

- November 30에 결혼하고 December 31에도 married이면 married로 시작한다.
- December 20에 final divorce decree가 있고 December 31에 remarried하지 않았으면 unmarried로 시작한다.
- married but living apart는 final decree가 없으면 generally married다.
- common-law marriage가 state law상 recognized이면 generally married다.

시험에서는 날짜가 나오면 filing status 문제라고 표시한다.

## 4. MFJ

`MFJ`, 즉 `Married Filing Jointly`는 spouses가 combined income and deductions를 one joint return에 신고하는 status다.

핵심:

- one spouse에게 income이 없어도 가능할 수 있다.
- spouse died during the year이면, survivor가 remarried하지 않고 요건을 충족하면 year of death에 MFJ 가능성이 있다.
- joint return은 generally both spouses가 sign한다.
- joint return은 generally joint and several liability를 만든다.

## 5. MFS

`MFS`, 즉 `Married Filing Separately`는 married taxpayers가 separate returns를 filing하는 status다.

시험에서 MFS는 보통 limitation trigger다.

대표 감각:

- many credits/deductions가 limited 또는 disallowed될 수 있다.
- education credits는 generally MFS에서 불가능하다.
- one spouse itemizes deductions이면 other spouse도 generally standard deduction을 사용할 수 없다.
- 2025 Publication 501의 filing requirement chart에서 MFS gross income threshold는 `$5`로 매우 낮다.

MFS는 Single과 같은 말이 아니다. married status 안에서 separate return을 선택하는 것이다.

## 6. HOH

`HOH`, 즉 `Head of Household`는 세 문을 통과해야 한다.

1. taxpayer가 unmarried 또는 considered unmarried인가
2. taxpayer가 `more than half the cost of keeping up a home`을 paid했는가
3. qualifying person이 있는가

세 문 중 하나만 맞으면 안 된다. 반드시 함께 본다.

## 7. Cost of keeping up a home

HOH에서 `cost of keeping up a home`은 household 유지비다.

포함되는 대표 항목:

- rent
- mortgage interest
- real estate taxes
- insurance on the home
- repairs
- utilities
- food eaten in the home

일반적으로 포함하지 않는 항목:

- clothing
- education
- medical treatment
- vacations
- life insurance
- transportation

`More than half`는 50% 초과다. exactly 50%는 fail이다.

## 8. Considered unmarried

Married taxpayer도 certain facts가 있으면 HOH 목적상 `considered unmarried`가 될 수 있다.

핵심 trigger:

- taxpayer files a separate return
- taxpayer paid more than half the cost of keeping up the home
- spouse did not live in the home during the last 6 months of the tax year
- home was the main home of taxpayer's child, stepchild, or eligible foster child for more than half the year
- child is dependent, or would be dependent except for certain noncustodial-parent rules

이건 자동 Single이 아니다. married taxpayer가 HOH로 갈 수 있는 특별한 길이다.

## 9. Qualifying person for HOH

HOH qualifying person은 specific rules를 따른다.

중요 함정:

- qualifying child가 taxpayer와 more than half the year lived하면 HOH qualifying person 가능성이 크다.
- dependent parent는 taxpayer와 같이 살지 않아도 parent rule로 HOH qualifying person이 될 수 있다.
- unrelated friend는 all-year household member로 dependent가 되어도, 그 이유만으로 HOH qualifying person은 generally 아니다.
- temporary absence, birth/death year rules를 놓치지 않는다.

## 10. QSS

`QSS`, 즉 `Qualifying Surviving Spouse`는 spouse death 이후 일정 요건에서 사용하는 status다.

핵심:

- spouse died in one of the two years before the current tax year
- taxpayer did not remarry before the end of the tax year
- taxpayer could have filed a joint return with the deceased spouse for the year of death
- taxpayer has a qualifying child or stepchild for the status
- taxpayer paid more than half the cost of keeping up the home
- that home was the child's main home for the entire year, except temporary absences

Year of death에는 generally MFJ 가능성을 먼저 본다. QSS는 following two years다.

## 11. 문제 풀이 루틴

문제를 읽으면 아래처럼 적는다.

`date? spouse? child? home cost? status limitation?`

예:

- `married Nov 30, still married Dec 31` -> married status
- `divorced Dec 20 final decree` -> unmarried
- `spouse died in 2025` -> MFJ for year of death
- `spouse died in 2023, dependent child, no remarriage` -> QSS in 2025
- `paid more than half cost of keeping up home` -> HOH
- `unrelated friend dependent` -> HOH warning
- `MFS education credit` -> limitation warning

## 12. Day 2 반드시 외울 10문장

1. `Filing status` affects standard deduction, tax rates, filing requirements, and credit eligibility.
2. There are five filing statuses: `Single`, `MFJ`, `MFS`, `HOH`, and `QSS`.
3. Marital status is generally determined on the last day of the tax year.
4. Married taxpayers generally start with `MFJ` or `MFS`.
5. `MFS` often limits credits and deductions.
6. `HOH` requires status, home cost, and qualifying person.
7. `Cost of keeping up a home` is not the same as support of a person.
8. A married taxpayer may be considered unmarried for HOH only if specific tests are met.
9. A dependent parent does not always have to live with the taxpayer for HOH.
10. `QSS` is generally for the two years after the spouse's year of death.

## Sources Used

- IRS Sample SEE Questions and Answers: https://www.irs.gov/tax-professionals/enrolled-agents/sample-special-enrollment-examination-questions-and-answers
- IRS Publication 501 (2025): https://www.irs.gov/publications/p501
- IRS About Form 1040: https://www.irs.gov/forms-pubs/about-form-1040
