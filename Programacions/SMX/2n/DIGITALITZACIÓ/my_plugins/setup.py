from setuptools import setup

setup(
    name='mkdocs-radd-tables',
    version='0.1',
    packages=['add_tables'],
    entry_points={
        'mkdocs.plugins': [
            'add_tables = add_tables:AddTablesPlugin',
        ],
    },
)
