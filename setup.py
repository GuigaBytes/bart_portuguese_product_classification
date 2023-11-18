from setuptools import setup, find_packages

setup(
    name='bart_portuguese_product_classification',
    version='0.1',
    author='Guilherme Lourenço',
    author_email='guilhermelourenco.contato@gmail.com',
    description = 'Case Study: Using Facebook\'s BART Large MNLI Model for Portuguese Supermarket Product Classification',
    url='https://github.com/GuigaBytes/bart_portuguese_product_classification',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'datasets',
        'scikit-learn',
        'pandas',
        'numpy',
        'torch',
        'accelerate',
        'nltk'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3',
)
