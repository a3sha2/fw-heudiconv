import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
#with open("requirements.txt", "r") as fh:
#    requirements = fh.read().splitlines()

setuptools.setup(
    name="fw_heudiconv",
    version="0.2.4",
    author="Tinashe M. Tapera, Matt Cieslak, Harsha Kethineni",
    author_email="tinashemtapera@gmail.com",
    description="Use heudiconv heuristics for BIDS curation on flywheel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PennBBL/fw_heudiconv",
    packages=setuptools.find_packages(),
    install_requires=[
        "flywheel-sdk",
        "heudiconv",
        "pandas",
        "bids-validator"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'fw-heudiconv-curate=fw_heudiconv.cli.curate:main',
            'fw-heudiconv-export=fw_heudiconv.cli.export:main',
            'fw-heudiconv-tabulate=fw_heudiconv.cli.tabulate:main',
            'fw-heudiconv-clear=fw_heudiconv.cli.clear:main',
            'fw-heudiconv-validate=fw_heudiconv.cli.validate:main',
            'fw-heudiconv-meta=fw_heudiconv.cli.meta:main',
            'fw-heudiconv-reproin=fw_heudiconv.cli.reproin_check:main'
        ],
    }
)
