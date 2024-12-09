import flavio
from flavio.statistics.likelihood import FastLikelihood
import wilson
from skopt import gp_minimize
from skopt.space import Real
import numpy as np

observables = ['BR(Bs->mumu)']

fastlike = FastLikelihood(
    name="bsmumu_likelihood",
    observables=observables,
    include_measurements=['LHCb Bs->mumu 2017']
)

# Call make_measurement() to finalize the measurement setup
fastlike.make_measurement()

def custom_likelihood(params):
    C9, C10 = params
    # Create the Wilson object as before
    wc = wilson.Wilson(
        {'C9_bsmumu': C9, 'C10_bsmumu': C10}, 
        scale=4.8, 
        eft='WET', 
        basis='flavio'
    )

    # Instead of passing 'wc' directly, get the dictionary of WCs
    wc_dict = wc.get_wc(basis='flavio', scale=4.8)

    # Now pass this dictionary to log_likelihood
    return -fastlike.log_likelihood(wc_dict, parameter_dict)


space = [
    Real(-10, 10, name='C9'),
    Real(-10, 10, name='C10'),
]

result = gp_minimize(custom_likelihood, space, n_calls=10, random_state=1)

print("Fitted C9:", result.x[0])
print("Fitted C10:", result.x[1])
print("Best likelihood value:", -result.fun)
