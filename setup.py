from setuptools import setup
import setuptools


setup(
    name='coppredict',
    version='1.0.0',
    description='Recommender Systems using Temporal Restricted Sequential Patterns',
    url='',
    author='Hilda Ana Samame Jimenez',
    author_email='hsamame@pucp.edu.pe',
    maintainer=['Hilda Ana Samame Jimenez', 'Yoshitomi Eduardo Maehara Aliaga'],
    maintainer_email=['hsamame@pucp.edu.pe', 'ye.maeharaa@up.edu.pe'],
    packages=setuptools.find_packages(),
    license="MIT",
    install_requires=['pandas', 'numpy', 'psutil', 'IPython'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.*'
)