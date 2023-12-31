from setuptools import find_packages, setup

setup(
    name="dagster_gsheets",
    packages=find_packages(exclude=["dagster_gsheets_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pygsheets",
        "pandas"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
