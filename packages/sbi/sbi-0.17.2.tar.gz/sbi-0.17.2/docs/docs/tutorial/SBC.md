```python
from sbi.inference import SNPE, simulate_for_sbi
from sbi.analysis import pairplot

import torch
from torch.distributions import MultivariateNormal, Normal
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from tqdm.auto import tqdm

from sbi.diagnostics.sbc import sbc_in_batches, check_uniformity
```


```python
D = 2
num_workers = 2
sbc_batch_size = 10
show_progress_bars = True

def simulator(theta, sigma=.1):
    return theta + torch.randn_like(theta) * sigma

prior = MultivariateNormal(torch.zeros(D), covariance_matrix=torch.eye(D))
```


```python
inferer = SNPE(prior, density_estimator="mdn")
```


```python
theta, x = simulate_for_sbi(simulator, prior, num_simulations=100, 
                            simulation_batch_size=1000, num_workers=num_workers)
```


```python
de = inferer.append_simulations(theta, x).train()
```

    Neural network successfully converged after 277 epochs.



```python
posterior = inferer.build_posterior()
```


```python
broad_prior = MultivariateNormal(torch.zeros(D), covariance_matrix=torch.eye(D))
for L in [100, 1000]:
# L = 100
# B = int(L/40)
# N = 1000
    for N in [50, 100]:
        ranks, log_probs, dap_samples = sbc_in_batches(prior, simulator, posterior, N, L, sbc_batch_size=100, num_workers=num_workers)
        cc = check_uniformity(ranks, L, num_repetitions=10)
        print(f"{N}, {L}, {cc[0].float()}, {cc[1]}")

```

    /home/janfb/qode/sbi/sbi/diagnostics/sbc.py:38: UserWarning: Number of SBC samples should be on the order ~100 to give realiable
                results. We recommend using 1000.
      results. We recommend using 1000."""



    Running 50 sbc runs in 1
                        batches.:   0%|          | 0/1 [00:00<?, ?it/s]


    50, 100, tensor([0.0986, 0.4338]), tensor([0.5340, 0.4690])


    /home/janfb/qode/sbi/sbi/diagnostics/sbc.py:38: UserWarning: Number of SBC samples should be on the order ~100 to give realiable
                results. We recommend using 1000.
      results. We recommend using 1000."""



    Running 100 sbc runs in 1
                        batches.:   0%|          | 0/1 [00:00<?, ?it/s]


    100, 100, tensor([0.5182, 0.5182]), tensor([0.4925, 0.4780])


    /home/janfb/qode/sbi/sbi/diagnostics/sbc.py:38: UserWarning: Number of SBC samples should be on the order ~100 to give realiable
                results. We recommend using 1000.
      results. We recommend using 1000."""



    Running 50 sbc runs in 1
                        batches.:   0%|          | 0/1 [00:00<?, ?it/s]


    50, 1000, tensor([0.4133, 0.6981]), tensor([0.4620, 0.4630])


    /home/janfb/qode/sbi/sbi/diagnostics/sbc.py:38: UserWarning: Number of SBC samples should be on the order ~100 to give realiable
                results. We recommend using 1000.
      results. We recommend using 1000."""



    Running 100 sbc runs in 1
                        batches.:   0%|          | 0/1 [00:00<?, ?it/s]


    100, 1000, tensor([0.0012, 0.7511]), tensor([0.5330, 0.4955])



```python
N = 1000
L = 1000
ranks, log_probs, dap_samples = sbc_in_batches(prior, simulator, posterior, N, L, sbc_batch_size=100, num_workers=num_workers)
```


    Running 1000 sbc runs in 10
                        batches.:   0%|          | 0/10 [00:00<?, ?it/s]



```python
check_uniformity(ranks, L, num_repetitions=1)
```




    (tensor([3.0792e-10, 3.6275e-03]), tensor([0.5430, 0.5025]))




```python
fig, ax = plt.subplots(2, D, figsize=(18, 10), sharey="row")
B = 20

for i in range(D):
    plt.sca(ax[0, i] if D > 1 else ax)
    plt.hist(ranks[:, i].numpy(), bins=B, alpha=0.8);
#     plt.fill_between(x=np.arange(-1, B+1), 
#                      y1=binom(N, p=1 / B).ppf(0.005), 
#                      y2=binom(N, p=1 / B).ppf(0.995), 
#                      color="grey", 
#                      alpha=0.2)
    plt.xlabel("Rank of true parameter under posterior samples")
    if i == 0:
        plt.ylabel("count")
    plt.title(rf"Parameter $\theta_{i+1}$")
    
for ii in range(D):
    plt.sca(ax[1, ii])
    _, bins, _ = plt.hist(prior.sample((N,))[:, ii].numpy(), bins=B, alpha=0.8);
    plt.hist(dap_samples[:, ii].numpy(), bins=bins, alpha=0.8)
    plt.legend(["prior", "DAP"]);
```


    
![png](SBC_files/SBC_9_0.png)
    



```python
D
```


```python
fig, ax = plt.subplots(1, 1, figsize=(12, 5))

repeats = 1
nbins = B
M = N
ndim = D

hb = binom(M, p=1 / nbins).ppf(0.5) * np.ones(nbins)
hbb = hb.cumsum() / hb.sum()

lower = [binom(M, p=p).ppf(0.005) for p in hbb]
upper = [binom(M, p=p).ppf(0.995) for p in hbb]

for i in range(ndim):

    hist, *_ = np.histogram(ranks[:, i], bins=nbins, density=False)
    histcs = hist.cumsum()
    plt.plot(np.linspace(0, nbins, repeats*nbins), 
             np.repeat(histcs / histcs.max(), repeats), 
#              np.repeat(histcs / histcs.max() - hbb, repeats), 
             label=r"$\theta_{}$".format(i+1), 
             color=f"C{i+3}")
    
plt.legend(frameon=False)
    
plt.plot(np.linspace(0, nbins, repeats*nbins), 
         np.repeat(hbb, repeats),
#          np.repeat(hbb - hbb, repeats),
         color="C2", lw=2)

plt.fill_between(x=np.linspace(0, nbins, repeats*nbins), 
                 y1=np.repeat(lower / np.max(lower), repeats), 
#                  y1=np.repeat(lower / np.max(lower) - hbb, repeats), 
                 y2=np.repeat(upper / np.max(lower), repeats), 
#                  y2=np.repeat(upper / np.max(lower) - hbb, repeats), 
                 color='C2', 
                 alpha=0.3)

```


```python

```
