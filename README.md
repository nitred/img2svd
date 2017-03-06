# About
This is a python module to get the compressed singular values decomposition of an image.

To understand the module better, checkout the Jupyter Notebook in the `notebooks` folder!

# Installation
## Prerequisites
- `python 2.7 or 3.5`
- `numpy`
- `scikit-image`
- `matplotlib`

`requirements.txt` is not provided because numpy is painful to install using pip.

## Regular Installation
```
git clone https://github.com/nitred/img2svd.git
cd img2svd
python setup.py install
```

## Development Installation (Anaconda3)
```
git clone https://github.com/nitred/img2svd.git
cd img2svd
enable anaconda-3 environment
conda env create -f environment.yml
source activate img2svd
python setup.py develop
```

# Usage
## Get Compressed Coordinates
```
import img2svd
u, s, v = img2svd.get_svd_from_grayscale_image("/home/user/kingfisher.png",
                                            sigma_coverage_percentage=95,
                                            plot=True)

total_components = u.shape[0]
n_components_chosen = u.shape[1]
```
