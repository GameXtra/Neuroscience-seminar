from distutils.core import setup

setup(
    name='Localize',
    version='0.1dev',
    packages=['python'], # TODO(loya) see if this name needs to be changed
    scripts=['python/src/localize'], # TODO(loya) validate and rename.
    long_description='TBD', requires=['numpy', 'scikit-learn']  # TODO(loya)
)