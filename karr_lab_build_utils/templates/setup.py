import setuptools
try:
    import pkg_utils
except ImportError:
    import pip
    pip_version = tuple(pip.__version__.split('.'))
    if pip_version >= ('19', '3', '0'):
        import pip._internal.main as pip_main
    elif pip_version >= ('19', '0', '0'):
        import pip._internal as pip_main
    pip_main.main(['install', 'pkg_utils'])
    import pkg_utils
import os

name = '{{ name }}'
dirname = os.path.dirname(__file__)

# get package metadata
md = pkg_utils.get_package_metadata(dirname, name)

# install package
setuptools.setup(
    name=name,
    version=md.version,
    description='{{ description }}',
    long_description=md.long_description,
    url="https://github.com/KarrLab/" + name,
    download_url='https://github.com/KarrLab/' + name,
    author="Karr Lab",
    author_email="info@karrlab.org",
    license="MIT",
    keywords='{{ keywords|join(' ') }}',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    package_data=md.package_data,
    install_requires=md.install_requires,
    extras_require=md.extras_require,
    tests_require=md.tests_require,
    dependency_links=md.dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
