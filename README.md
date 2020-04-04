## **Cluster Sampling csv using python**
### Implementation of one of the statistical methods for sampling
Cluster sampling is a sampling plan used when mutually homogeneous yet internally heterogeneous groupings are evident in a statistical population (https://en.wikipedia.org/wiki/Cluster_sampling)  
  
This repository implement cluster sampling for .csv (Comma-separated values) file using python languange programming, 
**Requirement :**
* Python 3.6
* csv, numpy, random Library
* .csv dataset with categorical label/class

**Input**  
put your data (.csv) in data/ folder  
**Output**  
the result of sampling will replace taget in output/result.csv file  
**Step**  
1. Put your dataset .csv in folder /data/
1. Open file cluster_sampling.py 
1. Edit #INPUT# section based on your dataset
  * variable **data_path** <- load path's csv dataset
  * variable **idx_label** <- index column label or class
  * variable **is_header** <- True if dataset has header, False without header
  * variable **n_sample** <- n sample each cluster or class, n_sample cannot be larger than population or is negative
1. Run Program (comment in **Issues** tab if you had an error)
1. Result cluster sampling automaticly exported on /output/result.csv
