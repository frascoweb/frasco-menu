from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-menu',
    version='0.1',
    url='http://github.com/frascoweb/frasco-menu',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Menu management for Frasco",
    long_description=desc(),
    py_modules=['frasco_menu'],
    platforms='any',
    install_requires=[
        'frasco'
    ]
)