from setuptools import setup


setup(
    name="lektor-envvars",
    version="18.6.12.4",
    description="A Lektor plugin making environment variables available in templates.",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="Sebastian Vetter",
    author_email="seb@roadsi.de",
    url="https://www.github.com/elbaschid/lektor-envvars",
    py_modules=["lektor_envvars"],
    entry_points={"lektor.plugins": ["envvars = lektor_envvars:EnvvarsPlugin"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
