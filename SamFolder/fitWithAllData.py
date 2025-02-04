import flavio
import wilson
import numpy as np
import measurementFile1
import observablesFile1
#import dataset #limited test set Adi requested
from skopt import gp_minimize
from skopt.space import Real
from flavio.statistics.likelihood import FastLikelihood

flavio.measurements.read_file('my_bsll_measurements.yml')

########################################
# 1) Observables & FastLikelihood
########################################
observables = observablesFile1.list_1 #dataset.Observables

print("Setting up FastLikelihood...")
fastlike = FastLikelihood(
    name="b_decay_likelihood",
    observables=observables,
    include_measurements = measurementFile1.list_2 #dataset.Measurements
)
fastlike.make_measurement()
print("Successfully created likelihood!\n")

########################################
# 2) Helper: Build dict of param -> central_value
########################################
def build_parameter_dict():
    """
    Manually build a dictionary of param->central_value from
    'flavio.default_parameters', avoiding .get_central_all() on older flavio.
    """
    pd = {}
    for pn in flavio.default_parameters.all_parameters:
        try:
            pd[pn] = flavio.default_parameters.get_central(pn)
        except Exception:
            pass
    return pd

########################################
# 3) Custom Likelihood Function
########################################
def custom_likelihood(params):
    """
    Evaluate -log(likelihood) for (C9, C10, a0, a1, a2, deltaC7..., deltaC7p...).
    """
    # Unpack the first five: C9, C10, a0, a1, a2
    C9, C10, a0, a1, a2 = params[:5]

    # Next 12 are the deltaC7 & deltaC7p parameters (real/imag parts)
    (deltaC7_a0_re,   deltaC7_a0_im,
     deltaC7_b0_re,   deltaC7_b0_im,
     deltaC7p_ap_re,  deltaC7p_ap_im,
     deltaC7p_bp_re,  deltaC7p_bp_im,
     deltaC7_am_re,   deltaC7_am_im,
     deltaC7_bm_re,   deltaC7_bm_im) = params[5:17]

    try:
        # (A) Build a parameter dictionary from the current default
        par_dict = build_parameter_dict()

        # (B) Override form-factor and deltaC7 parameters
        par_dict['B->K*::a0_f+'] = a0
        par_dict['B->K*::a1_f+'] = a1
        par_dict['B->K*::a2_f+'] = a2

        par_dict['B->K*::deltaC7 a_0 Re']  = deltaC7_a0_re
        par_dict['B->K*::deltaC7 a_0 Im']  = deltaC7_a0_im
        par_dict['B->K*::deltaC7 b_0 Re']  = deltaC7_b0_re
        par_dict['B->K*::deltaC7 b_0 Im']  = deltaC7_b0_im

        par_dict['B->K*::deltaC7p a_+ Re'] = deltaC7p_ap_re
        par_dict['B->K*::deltaC7p a_+ Im'] = deltaC7p_ap_im
        par_dict['B->K*::deltaC7p b_+ Re'] = deltaC7p_bp_re
        par_dict['B->K*::deltaC7p b_+ Im'] = deltaC7p_bp_im

        par_dict['B->K*::deltaC7 a_- Re']  = deltaC7_am_re
        par_dict['B->K*::deltaC7 a_- Im']  = deltaC7_am_im
        par_dict['B->K*::deltaC7 b_- Re']  = deltaC7_bm_re
        par_dict['B->K*::deltaC7 b_- Im']  = deltaC7_bm_im

        # (C) Construct the Wilson object
        wc_obj = wilson.Wilson(
            {'C9_bsmumu': C9, 'C10_bsmumu': C10},
            scale=4.8, eft='WET', basis='flavio'
        )

        # (D) Compute log-likelihood
        ll = fastlike.log_likelihood(par_dict, wc_obj)

        if not np.isfinite(ll):
            return 1e10

        # Return -logL for minimization
        return -ll

    except Exception as e:
        print("Error in likelihood calculation:", e)
        return 1e10

########################################
# 4) Define Parameter Space
########################################
space = [
    Real(-10, 10, name='C9'),
    Real(-10, 10, name='C10'),
    Real(-1, 1,   name='a0'),
    Real(-2, 2,   name='a1'),
    Real(-5, 5,   name='a2'),
    # deltaC7 param space
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
    Real(-1, 1, name='deltaC7_bm_im'),
]

########################################
# 5) Run Optimization
########################################
print("Starting optimization...\n")

res = gp_minimize(
    custom_likelihood,
    space,
    n_calls=20,
    n_initial_points=10,
    random_state=1,
    n_jobs=-1,
    noise=1e-10,
    verbose=True
)

param_names = [
    'C9', 'C10', 'a0', 'a1', 'a2',
    'deltaC7_a0_re', 'deltaC7_a0_im',
    'deltaC7_b0_re', 'deltaC7_b0_im',
    'deltaC7p_ap_re', 'deltaC7p_ap_im',
    'deltaC7p_bp_re', 'deltaC7p_bp_im',
    'deltaC7_am_re', 'deltaC7_am_im',
    'deltaC7_bm_re', 'deltaC7_bm_im'
]

print("\nOptimization Results:")
for name, val in zip(param_names, res.x):
    print(f"{name} = {val}")
print("Best log-likelihood value:", -res.fun)

########################################
# 6) Print Predictions at Best-Fit
########################################
print("\nPredictions at best fit point:")

# (A) Override global default parameters
#     so np_prediction(...) picks them up automatically.
try:
    flavio.default_parameters.set_constraint('B->K*::a0_f+',  res.x[2])
    flavio.default_parameters.set_constraint('B->K*::a1_f+',  res.x[3])
    flavio.default_parameters.set_constraint('B->K*::a2_f+',  res.x[4])

    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_0 Re', res.x[5])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_0 Im', res.x[6])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 b_0 Re', res.x[7])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 b_0 Im', res.x[8])

    flavio.default_parameters.set_constraint('B->K*::deltaC7p a_+ Re', res.x[9])
    flavio.default_parameters.set_constraint('B->K*::deltaC7p a_+ Im', res.x[10])
    flavio.default_parameters.set_constraint('B->K*::deltaC7p b_+ Re', res.x[11])
    flavio.default_parameters.set_constraint('B->K*::deltaC7p b_+ Im', res.x[12])

    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_- Re', res.x[13])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 a_- Im', res.x[14])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 b_- Re', res.x[15])
    flavio.default_parameters.set_constraint('B->K*::deltaC7 b_- Im', res.x[16])

    # Build best-fit Wilson object for C9 & C10
    best_wc = wilson.Wilson(
        {'C9_bsmumu': res.x[0], 'C10_bsmumu': res.x[1]},
        scale=4.8, eft='WET', basis='flavio'
    )

    # (B) Evaluate each observable with no 'par=' or 'q2min=' keywords
    for obs in observables:
        if isinstance(obs, tuple):
            obs_name, qmin, qmax = obs
            pred = flavio.np_prediction(obs_name, best_wc, qmin, qmax)
            print(f"{obs_name}[{qmin}-{qmax}] = {pred}")
        else:
            pred = flavio.np_prediction(obs, best_wc)
            print(f"{obs} = {pred}")

except Exception as e:
    print("Error during final predictions:", e)
