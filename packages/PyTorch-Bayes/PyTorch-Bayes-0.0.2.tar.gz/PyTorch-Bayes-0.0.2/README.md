# PyTorch-Bayes

PyTorch-Bayes is

* a simple PyTorch wrapper making Bayesian learning much easier





## Quickstart


### Dependencies and Installation

#### Package Dependencies

`pip install -r requirements.txt` can handle all package dependencies.

#### Install PyTorch-Bayes

```bash
$ pip install pytorch-bayes
```



## Bayesian Learning

* ***Prior***
  $$
  p(\mathbf{w})
  $$
* ***Likelihood***
  $$
  p(\mathbf{y}_{1:n}|\mathbf{x}_{1:n}, \mathbf{w}) = \prod_{i=1}^{n} p(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})
  $$
* ***Posterior***
  $$
  p(\mathbf{w}|\mathbf{x}_{1:n}, \mathbf{y}_{1:n}) = \frac{1}{Z} p(\mathbf{w}) \prod_{i=1}^{n} p(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})
  $$
  where $Z = \int p(\mathbf{w}) \prod_{i=1}^{n} p(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})d\mathbf{w}$

* ***Prediction***
  $$
  p(\mathbf{y}^{*}|\mathbf{x}^{*}, \mathbf{x}_{1:n}, \mathbf{y}_{1:n}) = \int p(\mathbf{y}^{*}|\mathbf{x}^{*}, \mathbf{w}) p(\mathbf{w}|\mathbf{x}_{1:n}, \mathbf{y}_{1:n}) d\mathbf{w}
  $$

### Maximum Likelihood Estimation (MLE)

$$
\mathbf{w}^{\text{MLE}} = \arg\max_{\mathbf{w}} \log P(\mathbf{y}_{1:n}|\mathbf{x}_{1:n}, \mathbf{w}) = \arg\max_{\mathbf{w}} \sum_{i=1}^{n} \log P(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})
$$

### Maximum a Posteriori (MAP)

$$
\mathbf{w}^{\text{MAP}} = \arg\max_{\mathbf{w}} \log P(\mathbf{w}|\mathbf{x}_{1:n}, \mathbf{y}_{1:n}) = \log P(\mathbf{w}) + \arg\max_{\mathbf{w}} \sum_{i=1}^{n} \log P(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})
$$

### Being Bayesian by Backpropagation (Bayes by Backprop)

$$
\mathcal{F}(\mathbf{y}_{1:n}|\mathbf{x}_{1:n}, \mathbf{\theta}) \approx \sum_{j=1}^{N_{MC}} \left[\log q(\mathbf{w}^{(j)}|\mathbf{\theta}) - \log P(\mathbf{w}^{(j)}) - \sum_{i=1}^{n} \log P(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w}^{(j)})\right]
$$

* ***Variational Posterior Parameters***
  $$
  \mathbf{\theta} = (\mathbf{\mu}, \mathbf{\rho})
  $$

* ***Gaussian Variational Posterior***
  $$
  \mathbf{w} = \mathbf{\mu} + \mathbf{\sigma} \odot \mathbf{\epsilon}
  $$
  where $\odot$ is element-wise multiplication operator, $\sigma = \log(1 + e^{\rho})$ and $\epsilon \sim \mathcal{N}(0, I)$

* ***Cost Function***
  $$
  \mathcal{f} (\mathbf{w}, \theta) = \log q(\mathbf{w}|\theta)  - \log P(\mathbf{w}) - \sum_{i=1}^{n} \log P(\mathbf{y}_{i}|\mathbf{x}_{i}, \mathbf{w})
  $$
  where using either ***Gaussian prior***
  $$
  \log P(\mathbf{w}) = \sum_{k} \log \mathcal{N}(\mathbf{w}_{k} | 0, \sigma_{0}^{2})
  $$
  or ***Gaussian scale mixture prior***
  $$
  \log P(\mathbf{w}) = \sum_{k} \log \left[\pi \mathcal{N}(\mathbf{w}_{k} | 0, \sigma_{1}^{2}) + (1 - \pi) \mathcal{N}(\mathbf{w}_{k} | 0, \sigma_{2}^{2})\right]
  $$

* ***Update the Variational Posterior Parameters***
  $$
  \mu \leftarrow \mu - \alpha \Delta_{\mu}
  $$
  and
  $$
  \rho \leftarrow \rho - \alpha \Delta_{\rho}
  $$
  ​    

