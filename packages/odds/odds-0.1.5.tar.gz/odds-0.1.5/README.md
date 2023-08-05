# Outlier Data Detection Systems - ODDS

# As used in paper "Simple Models are Effective in Anomaly Detection in Multi-variate Time Series"

Contains an OD object

Instantiate the object with the 'algo' argument

eg. od = OD('VAR')
instantiates an outlier detection system using vector autoregression

get outlier scores using the 'get_os()' function

eg. outlier_scores = od.get_os(X)

Where X is a data matrix, n samples by p features. P must be 2 or greater to work
on many of the systems, this returns a vector with n scores, one for each sample.

Higher numbers mean more outlying.


Valid strings for outlier algorithms:

- 'VAR' vector autoregression
- 'FRO' ordinary feature regression
- 'FRL' LASSO feature regression
- 'FRR' Ridge feature regression
- 'GMM' Gaussian Mixture model
- 'IF' isolation Forest
- 'DBSCAN' Density Based Spatial clustering and noise
- 'OCSVM' one class support vector machine
- 'LSTM' long short term memory
- 'GRU' gated recurrent unit
- 'AE' autoencoder
- 'VAE' variational autoencoder
- 'OP' outlier pursuit
- 'GOP' graph regularised outlier pursuit
- 'RAND' random scoring (for baseline comparison)
