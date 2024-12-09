import flavio
import wilson
from skopt import gp_minimize
from skopt.space import Real
import numpy as np

def custom_likelihood(params):
    # Unpack the parameters in order
    C9, C10, a0, a1, a2 = params[0:5]
    
    # Unpack delta C7 parameters
    deltaC7_a0_re, deltaC7_a0_im = params[5:7]    # a_0 real and imaginary parts
    deltaC7_b0_re, deltaC7_b0_im = params[7:9]    # b_0 real and imaginary parts
    deltaC7p_ap_re, deltaC7p_ap_im = params[9:11]  # a_+ real and imaginary parts
    deltaC7p_bp_re, deltaC7p_bp_im = params[11:13] # b_+ real and imaginary parts
    deltaC7_am_re, deltaC7_am_im = params[13:15]   # a_- real and imaginary parts
    deltaC7_bm_re, deltaC7_bm_im = params[15:17]   # b_- real and imaginary parts
    
    # Set Wilson coefficients
    wc = wilson.Wilson({'C9_bsmumu': C9, 'C10_bsmumu': C10}, scale=4.8, eft='WET', basis='flavio')
    
    # Set form factor parameters
    flavio.default_parameters.set_constraint('B->K*::a0_f+', a0)
    flavio.default_parameters.set_constraint('B->K*::a1_f+', a1)
    flavio.default_parameters.set_constraint('B->K*::a2_f+', a2)
    
    # Set delta C7 parameters
    par = flavio.default_parameters
    par.set_constraint('B->K*::deltaC7 a_0 Re', deltaC7_a0_re)
    par.set_constraint('B->K*::deltaC7 a_0 Im', deltaC7_a0_im)
    par.set_constraint('B->K*::deltaC7 b_0 Re', deltaC7_b0_re)
    par.set_constraint('B->K*::deltaC7 b_0 Im', deltaC7_b0_im)
    par.set_constraint('B->K*::deltaC7p a_+ Re', deltaC7p_ap_re)
    par.set_constraint('B->K*::deltaC7p a_+ Im', deltaC7p_ap_im)
    par.set_constraint('B->K*::deltaC7p b_+ Re', deltaC7p_bp_re)
    par.set_constraint('B->K*::deltaC7p b_+ Im', deltaC7p_bp_im)
    par.set_constraint('B->K*::deltaC7 a_- Re', deltaC7_am_re)
    par.set_constraint('B->K*::deltaC7 a_- Im', deltaC7_am_im)
    par.set_constraint('B->K*::deltaC7 b_- Re', deltaC7_bm_re)
    par.set_constraint('B->K*::deltaC7 b_- Im', deltaC7_bm_im)
    
    # Observables remain the same
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
    
    return -ll

# Define the search space including all delta C7 parameters
space = [
    Real(-10, 10, name='C9'),
    Real(-10, 10, name='C10'),
    Real(-1, 1, name='a0'),
    Real(-2, 2, name='a1'),
    Real(-5, 5, name='a2'),
    # Delta C7 parameters with reasonable bounds
    Real(-1, 1, name='deltaC7_a0_re'),
    Real(-1, 1, name='deltaC7_a0_im'),
    Real(-1, 1, name='deltaC7_b0_re'),
    Real(-1, 1, name='deltaC7_b0_im'),
    Real(-1, 1, name='deltaC7p_ap_re'),
    Real(-1, 1, name='deltaC7p_ap_im'),
    Real(-1, 1, name='deltaC7p_bp_re'),
    Real(-1, 1, name='deltaC7p_bp_im'),
    Real(-1, 1, name='deltaC7_am_re'),
    Real(-1, 1, name='deltaC7_am_im'),
    Real(-1, 1, name='deltaC7_bm_re'),
    Real(-1, 1, name='deltaC7_bm_im')
]

# Perform the optimization
result = gp_minimize(custom_likelihood, space, n_calls=50, random_state=1)

# Print the results
param_names = [
    'C9', 'C10', 'a0', 'a1', 'a2',
    'deltaC7_a0_re', 'deltaC7_a0_im',
    'deltaC7_b0_re', 'deltaC7_b0_im',
    'deltaC7p_ap_re', 'deltaC7p_ap_im',
    'deltaC7p_bp_re', 'deltaC7p_bp_im',
    'deltaC7_am_re', 'deltaC7_am_im',
    'deltaC7_bm_re', 'deltaC7_bm_im'
]
for name, value in zip(param_names, result.x):
    print(f"Fitted {name}: {value}")
print("Best likelihood value:", -result.fun)