from setuptools import find_packages, setup

package_name = 'astar_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
    ],
     install_requires=['setuptools','qiskit'],
    zip_safe=True,
    maintainer='puja',
    maintainer_email='puja@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'astar_node = astar_planner.astar_node:main',
            'path_follower_node = astar_planner.path_follower_node:main',
            'occupancy_grid_node = astar_planner.occupancy_grid_node:main',
            'grover_node = astar_planner.grover_node:main',
        ],
    },
)
