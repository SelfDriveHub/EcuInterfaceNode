from setuptools import find_packages, setup

package_name = 'ecu_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lukas',
    maintainer_email='lukas.zimmermann@schoggipopcorn.ch',
    description='Node to interact with the ECU',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'ecu_interface_node = ecu_interface.ecu_interface_node:main',
        ],
    },
)
