import flavio
import wilson
from skopt import gp_minimize
from skopt.space import Real
import numpy as np

def custom_likelihood(params):
    C9, C10, a0, a1, a2 = params
    
    # Set Wilson coefficients
    wc = wilson.Wilson({'C9_bsmumu': C9, 'C10_bsmumu': C10}, scale=4.8, eft='WET', basis='flavio')
    
    # Set hadronic parameters
    flavio.default_parameters.set_constraint('B->K*::a0_f+', a0)
    flavio.default_parameters.set_constraint('B->K*::a1_f+', a1)
    flavio.default_parameters.set_constraint('B->K*::a2_f+', a2)
    
    # Note: We avoid q² bins above 6 GeV² due to unreliable QCDF corrections
    observables = [
        ('BR(Bs->mumu)', None),
        ('<FL>(B0->K*mumu)', [(0.1, 0.98), (1.1, 2.5), (2.5, 4), (4, 6)]),
        ('<P5p>(B0->K*mumu)', [(0.1, 0.98), (1.1, 2.5), (2.5, 4), (4, 6)])
    ]
    
    ll = 0
    for obs, q2_bins in observables:
        if q2_bins is None:
            try:
                exp = flavio.sm_prediction(obs)
                the = flavio.np_prediction(obs, wc)
                sigma = 0.1 * exp  # Assuming 10% uncertainty
                ll += -0.5 * ((exp - the) / sigma)**2
            except Exception as e:
                print(f"Error calculating {obs}: {str(e)}")
        else:
            for q2min, q2max in q2_bins:
                try:
                    exp = flavio.sm_prediction(obs, q2min, q2max)
                    the = flavio.np_prediction(obs, wc, q2min, q2max)
                    sigma = 0.1 * exp  # Assuming 10% uncertainty
                    ll += -0.5 * ((exp - the) / sigma)**2
                except Exception as e:
                    print(f"Error calculating {obs} at q2=({q2min}, {q2max}): {str(e)}")
    
    return -ll  # Return negative log-likelihood for minimization

# Define the search space
space = [
    Real(-10, 10, name='C9'),
    Real(-10, 10, name='C10'),
    Real(-1, 1, name='a0'),
    Real(-2, 2, name='a1'),
    Real(-5, 5, name='a2')
]

# Perform the optimization
result = gp_minimize(custom_likelihood, space, n_calls=50, random_state=1)
#  n_calls should be in the 100s at the very least. Any lower is just for testing

# Print the results
param_names = ['C9', 'C10', 'a0', 'a1', 'a2']
for name, value in zip(param_names, result.x):
    print(f"Fitted {name}: {value}")
print("Best likelihood value:", -result.fun)

# Print all parameters and their values
# print("\nAll parameters:")
# all_params = flavio.default_parameters.get_central_all()
# for name, value in all_params.items():
#     print(f"{name}: {value}")

# Print specifically the parameters we modified
# print("\nModified parameters:")
# for param in ['B->K*::a0_f+', 'B->K*::a1_f+', 'B->K*::a2_f+']:
#     print(f"{param}: {flavio.default_parameters.get_central(param)}")