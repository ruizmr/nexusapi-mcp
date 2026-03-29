from setuptools import setup

setup(
    name="nexusapi",
    version="0.1.0",
    py_modules=["nexusapi"],
    install_requires=["httpx>=0.24"],
    author="NexusAPI",
    description="18 compute tools for AI agents: web scraping, code execution, ML inference. 250 free credits.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruizmr/nexusapi-mcp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    keywords="ai agents mcp web-scraping code-execution ml-inference api compute",
)
