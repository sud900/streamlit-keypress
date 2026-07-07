import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-keypress",
    version="0.1.2",
    author="Sudarsan",
    author_email="sudarsan900@gmail.com",
    description="A Streamlit component to capture keyboard events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sud900/streamlit-keypress",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "streamlit_keypress.component": ["*.js", "*.html"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "streamlit>=1.59.0",
    ],
)