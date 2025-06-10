from setuptools import setup, find_packages

setup(
    name="python-app-installer",
    version="1.0.0",
    description="A simple GUI installer for downloading and installing applications.",
    author="oDev",
    packages=find_packages(),
    install_requires=[
        "guizero",
        "requests",
        "pyinstaller",
    ],
    include_package_data=True,
    python_requires=">=3.6",
)