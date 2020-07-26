CMGUI FAQ
=============

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Replicating cmgui 3.01 visualisation using gfx commands
-------------------------------------------------------

  .. code-block:: perl

    # For each region you need to list commands to recreate computed fields
    # (this orders them so that source fields are defined first, otherwise
    # its alphabetical):
    gfx list field "/" commands; # for root region
    gfx list field REGION_PATH commands; # for any other region
    # Images (textures) are now fields in each region so for each region with
    # images list:
    gfx list texture commands region REGION_PATH;
    # tessellation, material, spectrum are needed if you created any of your
    # own (including tessellations automatically created for old commands:
    gfx list tessellation;
    gfx list material commands;
    gfx list spectrum commands;
    # there are a bunch of other objects such as lights, graphics_filter which
    # you probably don’t change
    # graphics are simply listed for all regions
    gfx list g_element comm;
    # list window commands (for any windows you have):
    gfx list window 1 commands;
