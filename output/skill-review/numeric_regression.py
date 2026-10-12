"""스킬 예제의 독립 산술 검산. 스킬 실행/원문 판독 검수와는 별도다.

실행: python3 output/skill-review/numeric_regression.py
결과: 같은 폴더의 numeric-regression-results.json
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path

results = []


def check(name, actual, expected, tolerance=0):
    passed = abs(float(actual) - float(expected)) <= tolerance
    results.append(dict(name=name, actual=float(actual), expected=float(expected),
                        tolerance=tolerance, passed=passed))
    assert passed, results[-1]


# 정확한 분수 계산으로 원문·스킬 표시값 및 표시 자릿수를 확인한다.
check('common-consumption-value', 100000 + 10000000 * F(1, 10000), 101000)
check('separate-stone-cost', 120000 * F(1, 100), 1200)
check('cost-effectiveness-exact', F(1782, 1200), F(1485, 1000))
check('chest-old-2dp', F(3515, 495), 7.10, .005)
check('chest-new-2dp', F(3475, 475), 7.32, .005)
check('uniform-drop-conditional', sum(range(4, 9)) / 5, 6)
check('uniform-drop-unconditional', F(1, 2) * F(sum(range(4, 9)), 5), 3)
check('unequal-drop-unconditional', F(1, 2) * (4 * F(4, 5) + 8 * F(1, 5)), F(12, 5))
check('weighted-drop-source', F(200,630)*F(9,2)+F(200,630)*F(13,2)
      +F(140,630)*10+F(90,630)*16, 8)
check('paid-depth-count', 120000 * F(2, 5), 48000)
check('residual-day30', 2083605 - 2506282, -422677)
check('residual-day30-percent', F(-422677, 2506282)*100, -16.9, .05)
check('production-day100-consistency', 11747361 + 10469466, 22216827)
check('residual-day100-percent', F(11747361, 10469466)*100, 112, .5)
check('weighted-arppu', 66*F(80,100)+398*F(16,100)+1958*F(4,100), F(1948,10))
check('diamond-gap', 360 - 670, -310)
check('diamond-shortfall', 360 - 300, 60)
check('ltv-source', F(40, 1) / F(80, 100), 50)
check('arpu-example', F(200000, 1000), 200)
check('arppu-example', F(200000, 100), 2000)
check('pr-example', F(100, 1000), F(1, 10))
check('arpu-identity', F(100, 1000)*F(200000,100), 200)
check('linear-atk-L10', 100+(10-1)*50, 550)
check('linear-cost-total-1to10', sum(100+(i-1)*50 for i in range(1,11)), 3250)
for level, expected in [(1,2),(2,6),(5,6),(6,6),(7,10)]:
    check(f'step-cost-L{level}', 4*math.ceil(F(level-1,5))+2, expected)
check('time-cost-character-map', F(1,5)*(50+F(1,2)*50)+3, 18)
check('quadratic-cost-source-L10', 3*(10-1)**2-10+3, 236)
# 원문 속성 변환 수정식: 변환된 고정값을 합산한 뒤 백분율을 적용한다.
check('converted-hp-before-percent', (100 + 20*10 + 50)*F(11,10), 385)
check('damage-base', F(100**2,200), 50)
check('damage-atk30', F(130**2,230), 73.478, .0005)
check('damage-final30', 50*F(13,10), 65)
check('damage-both30', F(130**2,230)*F(13,10), 95.522, .0005)
check('sequential-crit', (F(7,10)-F(7,10)*F(3,10))*F(5,100), F(245,10000))
check('sequential-expected-damage', F(21,100)*100+F(245,10000)*80+F(4655,10000)*50, F(46235,1000))
check('hp101-hit-count', math.ceil(F(101,20)), 6)
check('hp101-kill-time-first0', F(math.ceil(F(101,20))-1,2), F(5,2))
check('hp101-dps-approx', F(101,40), F(2525,1000))
check('npc-hp-coefficient', F(20,10), 2)
check('level-gap-damage', 100+100*(20-10)*F(5,100), 150)
check('lanchester-source', math.sqrt(13.57/2.96), 2.14, .005)
check('damage-reduction', F(100-70,100), F(3,10))
check('shared-invalid-allocation', 20*5+10*10, 200)

# 재확인한 원문 예시를 정확한 분수·독립 합산으로 검산한다.
check('source-growth-template', 18*F(20,100)*F(60,100), F(216,100))
check('source-hierarchical-allocation', 12*F(10,100)*F(40,100), F(48,100))
check('source-tank-weighted-power', 3+F(66,10)+84*F(1,10), 18)
check('source-damage-ratio-not-survival', F(435,768), .57, .005)
check('source-pve-user-survival', F(123,20-11), 13.67, .005)
check('source-pve-monster-survival', F(264,33-11), 12)
check('source-charging-column-low', sum([6,30,30]), 66)
check('source-charging-column-medium', sum([6,30,68,30,68,68,128]), 398)
check('source-consumption-column-low', sum([10,20,20,300,20,200,100]), 670)
check('source-consumption-column-medium', sum([10,100,20,20,300,800,20,200,300,200,800,100,200]), 3070)
check('source-consumption-column-heavy', sum([10,100,20,500,20,300,800,2800,20,200,300,200,800,3000,100,200,2000,1888,1888]), 15146)
check('source-paid-depth-equipment', 68082*F(40,100), 27232.8, .00001)
check('source-paid-depth-displayed-total', sum([3197,39961,27233,97587,21320,23171,29120]), 241589)
check('source-artifact-main-initial', F(15,100)*311, 46.65, .00001)
check('source-artifact-substat-max', F(388,4*5), 19.4, .00001)
check('source-artifact-level-15-ratio', F(15,100)+F(85,100)*F(15,20), F(7875,10000))
check('source-artifact-level-20-ratio', F(15,100)+F(85,100)*F(20,20), 1)
check('source-artifact-level-15-atk', F(7875,10000)*311, 244.9125, .00001)

# 판정 트리를 직접 열거한 확률과 간소화식이 일치하는지 경계값까지 검증한다.
probability_cases = 0
for h in [F(i,10) for i in range(11)]:
    for p in [F(i,10) for i in range(11)]:
        for c in [F(i,10) for i in range(11)]:
            tree = [1-h, h*p, h*(1-p)*c, h*(1-p)*(1-c)]
            compact = [1-h, h*p, (h-h*p)*c, h-h*p-(h-h*p)*c]
            assert tree == compact and sum(tree) == 1 and min(tree) >= 0
            probability_cases += 1

# 피해식의 대수적 동치와 유효 영역 내 범위를 다른 표현으로 검증한다.
damage_cases = 0
for attack in [F(1), F(100), F(10000)]:
    for defense in [F(0), F(1), F(100), F(10000)]:
        for k in [F(1), F(1200)]:
            upgraded = attack - attack*defense/(k+defense)
            assert upgraded == attack*k/(k+defense)
            division = attack**2/(attack+defense)
            assert division == attack*(1-defense/(attack+defense))
            assert 0 <= upgraded <= attack and 0 <= division <= attack
            damage_cases += 1

out = dict(status='PASS', arithmetic_assertions=len(results), results=results,
           probability_grid_cases=probability_cases, damage_identity_cases=damage_cases,
           limitation='산술과 명시한 모델 불변식 검증이며 전체 원문/에이전트 행동의 증명은 아님')
Path(__file__).with_name('numeric-regression-results.json').write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in out.items() if k != 'results'}, ensure_ascii=False))
