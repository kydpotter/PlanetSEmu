import GPy
from likelihood.likelihood import PoissonLikelihood

def build_layer1_model(x_sample, y_sample):
    # First Layer
    kernel = GPy.kern.RatQuad(input_dim=1)
    likelihood_layer1 = PoissonLikelihood()
    model_layer1 = GPy.core.GP(x_sample, y_sample.reshape(-1, 1), kernel=kernel, likelihood=likelihood_layer1)
    model_layer1.optimize(messages=True)
    return model_layer1

def build_layer2_model(x_sample, y_sample, layer1_output_train):
    # Second Layer
    kernel2 = GPy.kern.RatQuad(input_dim=1)
    likelihood_layer2 = PoissonLikelihood()
    model_layer2 = GPy.core.GP(layer1_output_train, y_sample.reshape(-1, 1), kernel=kernel2, likelihood=likelihood_layer2)
    model_layer2.optimize(messages=True)

    return model_layer2

def predict_with_model(model, x_new):
    mean, variance = model.predict(x_new)
    return mean, variance
