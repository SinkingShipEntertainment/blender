name = "blender"

authors = [
    "Blender Foundation"
]

# NOTE: version = <external_version>.sse.<sse_version>
version = "3.6.4.sse.1.0.0"

description = \
    """
    3D DCC
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]
    #c.build_thread_count = "physical_cores"

requires = [
    "ffmpeg",
]

private_build_requires = [
    # "Jinja2",
    # "pyside2_setup-5.14.1",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "usd-22.11"],
]

# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"
#
# Pass cmake arguments (with debug symbols):
# rez-build -i --bt Debug
# rez-release --bt Debug

uuid = "repository.blender"

def pre_build_commands():
    command("source /opt/rh/devtoolset-11/enable")

def commands():
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.BLENDER_VERSION = external_version
    env.BLENDER_PACKAGE_VERSION = external_version
    if internal_version:
        env.BLENDER_PACKAGE_VERSION = internal_version

    env.BLENDER_ROOT.append("{root}")
    env.BLENDER_LOCATION.append("{root}")

    # env.BLENDER_INCLUDE_DIR = "{root}/include"
    # env.BLENDER_LIBRARY_DIR = "{root}/lib"
    # env.BLENDER_PYTHON_DIR = "{root}/lib/python"

    # env.PATH.append("{root}/bin")
    # env.PATH.append("{root}/lib")

    # env.LD_LIBRARY_PATH.append("{root}/bin")
    # env.LD_LIBRARY_PATH.append("{root}/lib")

    # env.PYTHONPATH.append("{root}/lib/python")
