from setuptools import setup

version = "1.0"

setup(
    name="euclidean_algorithm",
    version=version,

    author="Hspu1",
    author_email="rumyantsev1m0s1@gmail.com",

    description="A Python package, or rather a function, "
                "to reproduce the Euclidean algorithm",
    # long_description_content_type="text/markdown",

    url="https://github.com/Hspu1/Euclidean-Algorithm",
    download_url=f"https://github.com/Hspu1/"
                 f"Euclidean-Algorithm/archive/{version}.zip",

    license="MIT",

    packages=["euclidean_algorithm"],
    install_requires=["numba", "numpy", "llvmlite"],
    # in poetry (pyproject.toml) only numba

    classifiers=[
        "License :: MIT",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Implementation :: CPython"
    ]
)