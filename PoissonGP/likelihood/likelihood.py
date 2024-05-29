import GPy
import numpy as np
from scipy.special import gammaln

class PoissonLikelihood(GPy.likelihoods.Likelihood):
    def __init__(self, gp_link=None, name='poisson'):
        if gp_link is None:
            gp_link = GPy.likelihoods.link_functions.Log()
        super(PoissonLikelihood, self).__init__(gp_link=gp_link, name=name)
        
    def pdf_link(self, f, y, Y_metadata=None):
        return np.exp(self.logpdf_link(f, y))
    
    def logpdf_link(self, f, y, Y_metadata=None):
        # Log of Poisson probability mass function
        return y*f - np.exp(f) - gammaln(y+1)
    
    def log_predictive_density(self, f_mean, f_var, y):
        return self.logpdf_link(f_mean, y)

    def conditional_mean(self, gp):
        return np.exp(gp)
    
    def conditional_variance(self, gp):
        return np.exp(gp)
