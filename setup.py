from setuptools import setup, find_packages

setup(
    name="youtube_subscription",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "streamlit",
        "langchain",
        "openai",
        "chromadb",
        "sentence-transformers",
        "tiktoken",
        "youtube-search-python",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "google-cloud-aiplatform",
    ],
    entry_points="""
        [console_scripts]
        youtube_subscription=main.main:cli
    """,
)
