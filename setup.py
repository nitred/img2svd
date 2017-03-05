"""Setup file for the package/project."""

from setuptools import find_packages, setup

setup(
    name='img2svd',
    version='0.0.1',
    description='SVD based image compression and visualization.',
    long_description='SVD based image compression and visualization.',
    author='Nitish Reddy Koripalli',
    author_email='nitish.k.reddy@gmail.com',
    url='https://github.com/nitred/img2svd',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
