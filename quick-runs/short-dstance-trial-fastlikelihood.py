import flavio
from flavio.statistics.likelihood import FastLikelihood
import wilson
from skopt import gp_minimize
from skopt.space import Real
import numpy as np

observables = ['BR(Bs->mumu)']

# Use a measurement you actually have installed, for instance 'LHCb Bs->mumu 2017'
fastlike = FastLikelihood(
    name="bsmumu_likelihood",
    observables=observables,
    include_measurements=['LHCb Bs->mumu 2017']
)

def custom_likelihood(params):
    C9, C10 = params[0:2]
    # For simplicity, let's remove the deltaC7 parameters for now and just test if it runs.
    # Once this works, you can re-introduce them.
    wc = wilson.Wilson({'C9_bsmumu': C9, 'C10_bsmumu': C10}, scale=4.8, eft='WET', basis='flavio')
    parameter_dict = {}
    return -fastlike.log_likelihood(wc, parameter_dict)

space = [
    Real(-10, 10, name='C9'),
    Real(-10, 10, name='C10')
]

result = gp_minimize(custom_likelihood, space, n_calls=10, random_state=1)

print("Fitted C9:", result.x[0])
print("Fitted C10:", result.x[1])
print("Best likelihood value:", -result.fun)
