from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hoangtts",
    description="Chuyển đổi text sang audio sử dụng AI",
    author="Hoang Nguyen",
    author_email="nguyenluongdinhhoang@gmail.com",
    url="https://github.com/lordnic99/hoangtts",
    license="Apache License, Version 2.0",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
    py_modules=["hoangtts"],
    entry_points={"console_scripts": ["hoangtts = hoangtts:main"]},
)
