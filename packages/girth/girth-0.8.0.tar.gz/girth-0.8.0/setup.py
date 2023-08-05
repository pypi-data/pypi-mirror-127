from setuptools import setup, convert_path # pylint: disable=cyclic-import

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == '__main__':
    setup(
        name="girth", 
        packages=['girth', 'girth.utilities',
                  'girth.unidimensional.polytomous',
                  'girth.unidimensional.dichotomous',
                  'girth.multidimensional',
                  'girth.synthetic',
                  'girth.factoranalysis', 'girth.common'],
        package_dir={'girth': convert_path('./estimation'),
                     'girth.synthetic': convert_path('./synthetic'),
                     'girth.common': convert_path('./common'),
                     'girth.factoranalysis': convert_path('./factoranalysis')},
        version="0.8.0",
        license="MIT",
        description="A python package for Item Response Theory.",
        long_description=long_description.replace('<ins>','').replace('</ins>',''),
        long_description_content_type='text/markdown',
        author='Ryan C. Sanchez',
        author_email='ryan.sanchez@gofactr.com',
        url = 'https://eribean.github.io/girth/',
        keywords = ['IRT', 'Psychometrics', 'Item Response Theory', 
                    'Computer Adaptive Testing', 'Psychology'],
        install_requires = ['numpy', 'scipy'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering', 
            'License :: OSI Approved :: MIT License',          
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
        ]
    )
