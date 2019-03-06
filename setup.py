from setuptools import setup

setup(
    name='c_hack_api',
    packages=['c_hack_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_jwt_extended',
        'flask_migrate',        
        'flask_cors',
    ],
)
