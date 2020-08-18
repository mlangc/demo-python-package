from setuptools import setup

setup(
    name="demo_python_package",
    version="0.0.2",
    description="Demo library for demo and testing purposes",
    packages=["complexlib"],
    py_modules=["simplelib"],
    python_requires=">=3.7",
    install_requires=["requests>=2.24,<2.25"],
)
