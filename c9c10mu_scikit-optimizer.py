import flavio
import wilson
from skopt import gp_minimize
from skopt.space import Real
import numpy as np

# Define the likelihood function
def custom_likelihood(x):
    C9, C10 = x
    wc = wilson.Wilson({'C9_bsmumu': C9, 'C10_bsmumu': C10}, scale=4.8, eft='WET', basis='flavio')
    
    # Define observables
    observables = [
        ('BR(Bs->mumu)', None),
        ('<FL>(B0->K*mumu)', np.linspace(0.1, 19, 20)),
        ('<P5p>(B0->K*mumu)', np.linspace(0.1, 19, 20))
    ]
    
    # Calculate log-likelihood
    ll = 0
    for obs, q2 in observables:
        try:
            if q2 is None:
                exp = flavio.sm_prediction(obs)
                the = flavio.np_prediction(obs, wc)
            else:
                exp = flavio.sm_prediction(obs, q2)
                the = flavio.np_prediction(obs, wc, q2)
            
            # Assume 10% uncertainty for simplicity
            sigma = 0.1 * exp
            ll += -0.5 * ((exp - the) / sigma)**2
        except:
            # Skip if observable calculation fails
            pass
    
    return -ll  # Return negative log-likelihood for minimization

# Define the search space
space = [Real(-10, 10, name='C9'),
         Real(-10, 10, name='C10')]

# Perform the optimization
result = gp_minimize(custom_likelihood, space, n_calls=100, random_state=1)

# Print the results
print("Best C9_bsmumu:", result.x[0])
print("Best C10_bsmumu:", result.x[1])
print("Best likelihood value:", -result.fun)