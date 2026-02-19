from setuptools import setup

setup(
    name='myfilters',
    version='0.1',
    py_modules=['myfilters'],
    entry_points={
        'ufo2ft.filters': [
            'dumpAnchors = myfilters:DumpAnchors',
        ]
    }
)