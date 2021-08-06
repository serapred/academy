from setuptools import setup

setup(
    name="crypto",
    version="1.0",
    packages=["crypto"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        crypto=crypto.cli:cli
    """,
)
