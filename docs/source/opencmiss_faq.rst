OpenCMISS FAQ
=============

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_


Building OpenCMISS
------------------

  .. code-block:: bash

      ~/hpc/opt/OpenCMISS/cercmissprd01
      mkdir main
      cd main/
      git clone https://github.com/OpenCMISS/setup.git
      mkdir setup-build
      cd setup-build
      cmake -DOPENCMISS_ROOT=../ -DOPENCMISS_PERFORM_INITIAL_BUILD=false -DOPENCMISS_CONFIG_BUILD_TYPE=Debug ../setup
      make
      cd ../build/manage/release/
      pluma OpenCMISSInstallationConfig.cmake
      # set(IRON_BRANCH devel)
      # set(IRON_DEVEL git@github.com:PrasadBabarendaGamage/iron)
      # option(OPENCMISS_USE_ARCHITECTURE_PATH "Use architecture path to enable multiple configs in the same installation." YES)
      # option(OPENCMISS_DEVEL_ALL "Download/checkout development branches of all components of the OpenCMISS build." YES)
      cmake -DOPENCMISS_MPI=mpich -DOPENCMISS_MPI_USE_SYSTEM=NO -DOPENCMISS_TOOLCHAIN=gnu -DOPENCMISS_BUILD_TYPE=debug .
      make create_config
      pluma configs/x86_64_linux/gnu-C5.4-gnu-F5.4/mpich_release/OpenCMISSLocalConfig.cmake
      # set(OC_SYSTEM_LIBXML2 OFF)
      # set(OC_PYTHON_BINDINGS_USE_VIRTUALENV YES)
      # set(OC_USE_ZINC OFF)
      # set(IRON_WITH_Python_BINDINGS YES)
      make build_config
      cd /home/psam012/hpc/opt/OpenCMISS/cercmissprd01/main/install/x86_64_linux/gnu-C5.4-gnu-F5.4/mpich_release/python/Release
      python setup.py install --force
      source /home/psam012/hpc/opt/OpenCMISS/cercmissprd01/main/install/x86_64_linux/gnu-C5.4-gnu-F5.4/mpich_release/virtual_environments/oclibs_venv_py27_release/bin/activate



Using python bindings on hpc3
-----------------------------

  .. code-block:: bash

    # To use it, open a terminal and log in​to​ the hpc3 machine:
    ssh hpc3 # or
    ssh upi@hpc3​

    # Make sure you are running the bash shell
    bash

    # Setup environmental variables for OpenCMISS
    source /people/cmiss/develop_opencmiss.sh

    # Tell python where the OpenCMISS libraries are located
    source /people/cmiss/opencmiss/install/x86_64_linux/gnu-C4.4-gnu-F4.4/openmpi_release/virtual_environments/bin/activate

    # Go to the directory where the Laplace example is located (if needed, download from the OpenCMISS-examples repo)
    cd python/example/location/

    # Run the OpenCMISS example.
    python LaplaceExample.py


Debugging OpenCMISS examples
----------------------------

Set diagnostics on and off before/after the line of interest.

Use Totalview.
