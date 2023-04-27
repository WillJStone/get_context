from setuptools import setup, find_packages

setup(
    name='get_context',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'get-context = get_context.get_context:main',
        ],
    },
    install_requires=[
        'tiktoken',
        'pyperclip',
        'rich',
    ],
    python_requires='>=3.6',
)

