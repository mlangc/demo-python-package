from setuptools import setup
import version_query

setup(
    name="demo_python_package",
    version=version_query.predict_version_str(),
    description="Demo library for demo and testing purposes",
    packages=["complexlib"],
    py_modules=["simplelib"],
    python_requires=">=3.7",
    install_requires=["requests>=2.24,<2.25"],
    setup_requires=["version-query"]
)
