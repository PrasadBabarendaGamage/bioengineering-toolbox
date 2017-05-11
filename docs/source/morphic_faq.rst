Morphic FAQ
===========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

`Using groups <https://github.com/duanemalcolm/morphic/blob/master/test/test_io.py>`_
-------------------------------------------------------------------------------------

  .. code-block:: python

    cranial_elem = range(11)
    for element in mesh.elements[cranial_elem.tolist()]:
        element.add_to_group('cranial')
    for element in mesh.elements.groups['cranial']:
        print node.id


Build wxPython on Ubuntu 16.04 (required by mayavi2, which is used by morphic)
-------------------------------------------------------------------------------------

sudo apt-get install libgstreamer-plugins-base0.10-dev

`Speed up mayavi rendering <http://docs.enthought.com/mayavi/mayavi/tips.html>`_
--------------------------------------------------------------------------------

You’ve just created a nice Mayavi/mlab script and now want to generate an animation or a series of images. You realize that it is way too slow rendering the images and takes ages to finish. There are two simple ways to speed up the rendering. Let’s assume that obj is any Mayavi pipeline object that has a scene attribute:

  .. code-block:: python

   obj.scene.disable_render = True
   # Do all your scripting that takes ages.
   # ...
   # Once done, do the following:
   obj.scene.disable_render = False

This will speed things up for complex visualizations sometimes by an order of magnitude.

While saving the visualization to an image you can speed up the image generation at the cost of loosing out on anti-aliasing by doing the following:

  .. code-block:: python

   obj.scene.anti_aliasing_frames = 0

The default value is typically 8 and the rendered image will be nicely anti-aliased. Setting it to zero will not produce too much difference in the rendered image but any smooth lines will now appear slightly jagged. However, the rendering will be much faster. So if this is acceptable (try it) this is a mechanism to speed up the generation of images.