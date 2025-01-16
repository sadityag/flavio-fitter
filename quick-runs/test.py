import flavio
import wilson
import numpy as np
from skopt import gp_minimize
from skopt.space import Real
from flavio.statistics.likelihood import FastLikelihood

########################################
# 1) Define Observables
########################################
# We list various *observables* in Flavio notation without specifying q^2 bins.
# Flavio's internal "measurements" and the references in 'include_measurements'
# handle the actual data & binning under the hood.

observables = [
    # Common inclusive observable:
    'BR(Bs->mumu)',

    # Typical unbinned "symbolic" angular observables for B0->K*mumu:
    'FL(B0->K*mumu)',
    'AFB(B0->K*mumu)',
    'S3(B0->K*mumu)',
    'P5p(B0->K*mumu)',

    # If you want more B+ or additional channels:
    'BR(B+->K+mumu)',
    # etc. 
]

print("Setting up FastLikelihood...")

########################################
# 2) Include Full Measurements
########################################
# Each string references a set of measurements in Flavio's database
# that cover the full (unbinned or official binning) data for these observables.
# Check 'flavio.measurements.show_measurements()' for available labels.
include_meas = [
    # Already includes unbinned or official bin data for B->K*mumu angular:
    'LHCb B->K*mumu angular analysis 2020',
    'Belle B->K*mumu 2019 angular',
    # Combination for Bs->mumu:
    'ATLAS CMS LHCb combination Bs->mumu 2020',
    # Possibly more for B+->K+mumu:
    'LHCb B+->K+mumu 2019 branching fraction',
    # etc.
]

fastlike = FastLikelihood(
    name="b_decay_likelihood_full",
    observables=observables,
    include_measurements=include_meas,
)
fastlike.make_measurement()
print("Successfully created likelihood!\n")

########################################
# 3) Extended Parameter Space
########################################
# Let's now include not only C9, C10, but also C7, C7p, C9p, C10p,
# plus the original a0, a1, a2 for form factors, and the "deltaC7" expansions
# if you wish to keep them (example placeholders).

# You can also remove the "deltaC7" expansions if your model has C7, C7' directly.
# We'll show an example of many possible parameters at once.
space = [
    # Standard WCs:
    Real(-5, 5,   name='C7_bsmumu'),
    Real(-5, 5,   name='C7p_bsmumu'),
    Real(-10, 10, name='C9_bsmumu'),
    Real(-10, 10, name='C9p_bsmumu'),
    Real(-10, 10, name='C10_bsmumu'),
    Real(-10, 10, name='C10p_bsmumu'),
    # Some form-factor expansions for B->K* (example):
    Real(-1, 1,   name='a0_f+'),
    Real(-2, 2,   name='a1_f+'),
    Real(-5, 5,   name='a2_f+'),
    # If you want to keep the "deltaC7" expansions from your previous code:
    # (these are hypothetical placeholders - adapt to your local definitions)
    Real(-1, 1,   name='deltaC7_a0_re'),
    Real(-1, 1,   name='deltaC7_a0_im'),
    # etc. ...
]

########################################
# 4) Build a Parameter Dictionary from Defaults
########################################
def build_parameter_dict():
    """
    Manually build a dictionary of param->central_value from
    'flavio.default_parameters', avoiding older .get_central_all() issues.
    """
    pd = {}
    for pn in flavio.default_parameters.all_parameters:
        try:
            pd[pn] = flavio.default_parameters.get_central(pn)
        except Exception:
            pass
    return pd

########################################
# 5) Define Likelihood Function
########################################
def custom_likelihood(params):
    """
    Evaluate -log(likelihood) with the extended WCs & form-factor expansions.
    """
    # 1) Unpack the WCs, form factors, etc. from 'params'.
    #    Match the order in 'space' above!
    # Example (adapt as needed):
    (C7, C7p, C9, C9p, C10, C10p,
     a0, a1, a2,
     deltaC7_a0_re, deltaC7_a0_im) = params[:11]
     # If you included more, keep unpacking them here...

    # 2) Construct par_dict from default
    par_dict = build_parameter_dict()

    # 3) Override relevant form-factor expansions
    par_dict['B->K*::a0_f+'] = a0
    par_dict['B->K*::a1_f+'] = a1
    par_dict['B->K*::a2_f+'] = a2

    # 4) If you're keeping the "deltaC7" expansions:
    par_dict['B->K*::deltaC7 a_0 Re'] = deltaC7_a0_re
    par_dict['B->K*::deltaC7 a_0 Im'] = deltaC7_a0_im
    # etc. for all expansions you want.

    # 5) Construct the Wilson object with the extended WCs
    wc_dict = {
        'C7_bsmumu':  C7,
        'C7p_bsmumu': C7p,
        'C9_bsmumu':  C9,
        'C9p_bsmumu': C9p,
        'C10_bsmumu': C10,
        'C10p_bsmumu':C10p,
    }
    wc_obj = wilson.Wilson(
        wc_dict, 
        scale=4.8,  # ~ mb
        eft='WET',
        basis='flavio'
    )

    # 6) Evaluate the log-likelihood from fastlike
    ll = fastlike.log_likelihood(par_dict, wc_obj)
    if not np.isfinite(ll):
        return 1e10  # penalty if ill-defined
    return -ll       # negative log-likelihood

########################################
# 6) Run Optimization
########################################
print("Starting optimization with all relevant parameters...\n")
result = gp_minimize(
    custom_likelihood,
    space,
    n_calls=30,          # Increase as needed
    n_initial_points=15, # More initial points for better coverage
    random_state=1,
    n_jobs=-1,
    noise=1e-10,
    verbose=True
)

# Print the best-fit
best_params = result.x
print("\nOptimization Results (Full Observables + Extended WCs):")
for param, val in zip([sp.name for sp in space], best_params):
    print(f"{param} = {val}")
print("Best log-likelihood value:", -result.fun)

########################################
# 7) Predictions at Best Fit
########################################
print("\nPredictions at best fit point:")
try:
    # A) Override global default parameters for form factors, etc.
    flavio.default_parameters.set_constraint('B->K*::a0_f+',  best_params[6])
    flavio.default_parameters.set_constraint('B->K*::a1_f+',  best_params[7])
    flavio.default_parameters.set_constraint('B->K*::a2_f+',  best_params[8])
    # If you still do deltaC7 expansions:
    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_0 Re', best_params[9])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_0 Im', best_params[10])
    # etc.

    # B) Wilson object at best fit
    wc_best = {
        'C7_bsmumu':  best_params[0],
        'C7p_bsmumu': best_params[1],
        'C9_bsmumu':  best_params[2],
        'C9p_bsmumu': best_params[3],
        'C10_bsmumu': best_params[4],
        'C10p_bsmumu':best_params[5],
    }
    best_wc = wilson.Wilson(wc_best, scale=4.8, eft='WET', basis='flavio')

    # C) Evaluate each observable 
    #    (No q^2 bins => unbinned "full" observables)
    for obs in observables:
        if isinstance(obs, tuple):
            # Actually, we used no explicit q2 range, but if you do:
            obs_name, qmin, qmax = obs
            val = flavio.np_prediction(obs_name, best_wc, qmin, qmax)
            print(f"{obs_name}[{qmin}-{qmax}] = {val}")
        else:
            val = flavio.np_prediction(obs, best_wc)
            print(f"{obs} = {val}")

except Exception as e:
    print("Error computing final predictions:", e)
