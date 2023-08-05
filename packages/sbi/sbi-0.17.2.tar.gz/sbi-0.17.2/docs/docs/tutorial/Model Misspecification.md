```
import numpy as np
import torch

from sbi.inference import SNPE, prepare_for_sbi
from sbi.simulators import linear_gaussian, diagonal_linear_gaussian
from sbi.utils import pairplot

from torch.distributions import Gamma
```


```
D = 1
def assumed_model(theta, niid=10):
    x = diagonal_linear_gaussian(theta.repeat(niid, 1)).reshape(theta.shape[0], theta.shape[1], niid)
    return torch.cat((x.mean(axis=-1), x.std(axis=-1)**2), dim=1)

def true_model(theta, v, niid=10):
    x = linear_gaussian(theta.repeat(niid, 1), 
                        likelihood_shift=torch.zeros(D), 
                        likelihood_cov=v * torch.eye(D)).reshape(theta.shape[0], theta.shape[1], niid)
    return torch.cat((x.mean(axis=-1), x.std(axis=-1)**2), dim=1)
```

## Samples from assumed and true model


```
v = 5
N = 1000
prior = torch.distributions.MultivariateNormal(torch.zeros(D), torch.eye(D))
th = prior.sample((N, ))
pairplot([assumed_model(th), true_model(th, v=v)], upper="scatter", 
#          hist_diag=dict(bins=np.linspace(-3, 3, 20))
        );
```

    /home/janfb/qode/sbi/sbi/utils/plot.py:181: UserWarning: Importing `pairplot` from `sbi.utils` is deprecated since sbi v0.15.0. Instead, use `from sbi.analysis import pairplot`.
      "Importing `pairplot` from `sbi.utils` is deprecated since sbi "



    
![png](Model%20Misspecification_files/Model%20Misspecification_3_1.png)
    


## Augment simulator with Gaussian noise model

Standard simulator and prior: 
$$
x = f(\theta) \\ 
\theta \sim p(\theta)
$$

Augmented simulator
$$
x = f(\theta) + \xi(\gamma) \\ 
\theta \sim p(\theta) \\ 
\gamma \sim \Gamma(1, 2),
$$
where $\xi(\gamma) \sim \mathcal{N}(0, \gamma)$ is a Gaussian noise model with scale parameter $\gamma$

Augmented simulator
$$
x = f(\theta) + \gamma \\ 
\theta \sim p(\theta) \\ 
\gamma \sim \mathcal{N}(0, 1),
$$


```
def augmented_simulator(simulator, noise_model, theta, gamma):
    return simulator(theta) + noise_model(gamma)

def noise_model(gamma):
    return gamma * torch.randn(gamma.shape)

sim = lambda th: augmented_simulator(assumed_model, noise_model, th[:, :D], th[:, D:])
```


```
s, p = prepare_for_sbi(sim, [prior] + [Gamma(torch.ones(1), 5 * torch.ones(1))] * 2)
```

    /home/janfb/qode/sbi/sbi/utils/user_input_checks.py:45: UserWarning: Prior was provided as a sequence of 3 priors. They will be
                interpreted as independent of each other and matched in order to the
                components of the parameter.
      components of the parameter."""



```
N = 100000
th = p.sample((N,))
x = s(th)
```


```
estimator = SNPE(p, density_estimator="mdn")
estimator = estimator.append_simulations(th, x)
```


```
estimator.train(training_batch_size=1000)
posterior = estimator.build_posterior()
```

    /home/janfb/anaconda3/envs/consbi/lib/python3.7/site-packages/torch/autograd/__init__.py:147: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward compatibility was attempted on non supported HW (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:109.)
      allow_unreachable=True, accumulate_grad=True)  # allow_unreachable flag


    Neural network successfully converged after 75 epochs.



```
xo = true_model(torch.ones(1, 1), v=1)
xo
```




    tensor([[0.9480, 1.4844]])




```
ps = posterior.sample((1000,), x=xo)
```


    HBox(children=(HTML(value='Drawing 1000 posterior samples'), FloatProgress(value=0.0, max=1000.0), HTML(value=…


    



```
pairplot(ps, upper="scatter");
```

    /home/janfb/qode/sbi/sbi/utils/plot.py:181: UserWarning: Importing `pairplot` from `sbi.utils` is deprecated since sbi v0.15.0. Instead, use `from sbi.analysis import pairplot`.
      "Importing `pairplot` from `sbi.utils` is deprecated since sbi "



    
![png](Model%20Misspecification_files/Model%20Misspecification_12_1.png)
    



```
pps = assumed_model(ps)
```


```
ps.shape
```




    torch.Size([1000, 3])




```
pps.shape
```




    torch.Size([1000, 6])




```
pairplot(pps, points=xo, upper="scatter")
```

    /home/janfb/qode/sbi/sbi/utils/plot.py:181: UserWarning: Importing `pairplot` from `sbi.utils` is deprecated since sbi v0.15.0. Instead, use `from sbi.analysis import pairplot`.
      "Importing `pairplot` from `sbi.utils` is deprecated since sbi "



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-27-70febf8dc15f> in <module>
    ----> 1 pairplot(pps, points=xo, upper="scatter")
    

    ~/qode/sbi/sbi/utils/plot.py in pairplot(samples, points, limits, subset, upper, diag, figsize, labels, ticks, points_colors, warn_about_deprecation, **kwargs)
        364                     pass
        365 
    --> 366     return _pairplot_scaffold(diag_func, upper_func, dim, limits, points, opts)
        367 
        368 


    ~/qode/sbi/sbi/utils/plot.py in _pairplot_scaffold(diag_func, upper_func, dim, limits, points, opts)
        692                     for n, v in enumerate(points):
        693                         h = plt.plot(
    --> 694                             v[:, col],
        695                             v[:, row],
        696                             color=opts["points_colors"][n],


    IndexError: index 2 is out of bounds for axis 1 with size 2



    
![png](Model%20Misspecification_files/Model%20Misspecification_16_2.png)
    



```

```
