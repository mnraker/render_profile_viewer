# Copyright 2023-2024 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

import sys

uuid = "73528efd-c17e-40b7-aaf0-6b4e31358c55"
name = "render_profile_viewer"  # This must match the value in setup.cfg.
requires_rez_version = "2"
help = "http://readthedocs/docs/render_profile_viewer/en/stable"

authors = [
    'moonbase-dev@dreamworks.com',
]

# Supply arguments to the "python setup.py" call rez-build will make.
# These are appended after "python setup.py build [install]"
# Add --no-build-sphinx to disable the automatic building of docs.
rez_build_args = {
    'python-3.9': ['--no-build-sphinx'],
    'python-3.10': ['--no-build-sphinx'],
}

if 'cmake' in sys.argv:
    build_system = 'cmake'
    private_build_requires = [
        'cmake_modules-1.0'
    ]
else:
    build_system = 'setuptools'

def preprocess(this, data):
    from rez.package_py_utils import InvalidPackageError
    try:
        import rezbuild.earlybind
    except ImportError:
        raise InvalidPackageError("The package cannot be configured because "
                                  "rezbuild.earlybind cannot be imported.")
    rezbuild.earlybind.configure_package(this, data)
    data["requires"].extend([
    ])


@late()
def test_arguments():
    import os
    return os.getenv("REZ_TEST_ARGUMENTS", "")


def commands():
    env.PYTHONPATH.append("{root}")
    env.PATH.append("{root}/bin")

with scope("config") as config:
    config.package_filter = []

