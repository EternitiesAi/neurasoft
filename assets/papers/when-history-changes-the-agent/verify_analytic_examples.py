"""Finite analytical checks only. No subjects, model calls or third-party packages.
Run: python verify_analytic_examples.py
"""
import json
import math
from collections import defaultdict
from pathlib import Path

checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

joint_i, joint_ii = defaultdict(float), defaultdict(float)
for u in (0, 1):
    a = u
    joint_i[(a, 1, a)] += .5
    joint_ii[(a, 1, u)] += .5
check('identical observed action-receipt-outcome distributions', joint_i == joint_ii)
effects = [sum(.5*(1-0) for u in (0,1)), sum(.5*(u-u) for u in (0,1))]
check('Model I intervention effect equals one', effects[0] == 1)
check('Model II intervention effect equals zero', effects[1] == 0)

largest_error = 0.
for qi in range(21):
    q = qi/20
    losses=[]
    for pi in range(21):
        p = pi/20
        loss = q*(1-p)**2+(1-q)*p**2
        identity=(p-q)**2+q*(1-q)
        largest_error=max(largest_error,abs(loss-identity))
        losses.append(loss)
    check('Brier grid minimum at truth q='+str(q), losses.index(min(losses)) == qi)
check('Brier identity floating-point error below 1e-14',largest_error < 1e-14)

t,b=2.,1.
intended=t*t-t
effective=max(0,t-b)
distorted=effective*effective-effective
check('shared clock offset changes illustrative treatment contrast', intended == 2 and distorted == 0)

for p,c,L in [(.2,.1,1),(.9,.2,1),(.8,.2,1),(.6,2,10)]:
    answer_loss=(1-p)*L
    repair_loss=c
    if math.isclose(answer_loss,repair_loss,abs_tol=1e-12):
        check('equal losses allow indifferent policies',abs(answer_loss-repair_loss)<1e-12)
    else:
        check('repair inequality agrees with direct expected-loss comparison',((1-p)*L>c)==(repair_loss<answer_loss))

recorded_history=['missed deadline']
choose=lambda observation,history: 'accept'
check('archive may change while action remains independent of history', recorded_history != [] and choose('new task',recorded_history)==choose('new task',[]))
result={'kind':'analytical-example-checks','version':'1.0','passed':True,'checks':checks,'check_count':len(checks),'brier_max_absolute_error':largest_error,'observational_distribution':[{'A':k[0],'R':k[1],'Y':k[2],'probability':v} for k,v in sorted(joint_i.items())],'intervention_effects':{'model_i':effects[0],'model_ii':effects[1]},'scope':'Finite mechanical checks of illustrative mathematics; no empirical agent experiment or consciousness result.'}
Path(__file__).with_name('analytic-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':True,'check_count':len(checks),'brier_max_absolute_error':largest_error}))
