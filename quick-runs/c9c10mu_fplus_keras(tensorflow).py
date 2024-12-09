import flavio
import wilson
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Define the parameter space
param_names = ['C9', 'C10', 'a0', 'a1', 'a2']
param_ranges = [(-10, 10), (-10, 10), (-1, 1), (-1, 1), (-1, 1)]

class FlavioModel(keras.Model):
    def __init__(self):
        super(FlavioModel, self).__init__()
        self.params = [self.add_weight(shape=(1,), initializer="random_normal", trainable=True, name=name) 
                       for name in param_names]

    def call(self, inputs):
        return self.custom_likelihood()

    @tf.function
    def custom_likelihood(self):
        params = [p[0] for p in self.params]
        C9, C10, a0, a1, a2 = params
        
        # We'll use tf.py_function to wrap the Flavio and Wilson calculations
        ll = tf.py_function(self._calculate_likelihood, [C9, C10, a0, a1, a2], tf.float32)
        return tf.reshape(ll, shape=(1,))

    def _calculate_likelihood(self, C9, C10, a0, a1, a2):
        # Set Wilson coefficients
        wc = wilson.Wilson({'C9_bsmumu': C9.numpy(), 'C10_bsmumu': C10.numpy()}, scale=4.8, eft='WET', basis='flavio')
        
        # Set hadronic parameters
        flavio.default_parameters.set_constraint('B->K*::a0_f+', a0.numpy())
        flavio.default_parameters.set_constraint('B->K*::a1_f+', a1.numpy())
        flavio.default_parameters.set_constraint('B->K*::a2_f+', a2.numpy())
        
        observables = [
            ('BR(Bs->mumu)', None),
            ('<FL>(B0->K*mumu)', [(0.1, 0.98), (1.1, 2.5), (2.5, 4), (4, 6)]),
            ('<P5p>(B0->K*mumu)', [(0.1, 0.98), (1.1, 2.5), (2.5, 4), (4, 6)])
        ]
        
        ll = 0.0
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
        
        return tf.constant([-ll], dtype=tf.float32)  # Return negative log-likelihood for minimization

# Create and compile the model
model = FlavioModel()
optimizer = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=optimizer, loss=lambda y_true, y_pred: y_pred)

# Dummy data for training
dummy_x = np.array([[0]])
dummy_y = np.array([[0]])

# Train the model
history = model.fit(dummy_x, dummy_y, epochs=500, verbose=0)

# Print results
print("Optimization results:")
for name, param in zip(param_names, model.params):
    print(f"Best {name}: {param.numpy()[0]}")
print(f"Best likelihood value: {-history.history['loss'][-1]}")

# Print specifically the parameters we modified
print("\nModified parameters:")
for param in ['B->K*::a0_f+', 'B->K*::a1_f+', 'B->K*::a2_f+']:
    print(f"{param}: {flavio.default_parameters.get_central(param)}")