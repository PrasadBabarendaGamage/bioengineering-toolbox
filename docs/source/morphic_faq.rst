Morphic FAQ
===========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

`Using groups <https://github.com/duanemalcolm/morphic/blob/master/test/test_io.py>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: python

    cranial_elem = range(11)
    for element in mesh.elements[cranial_elem.tolist()]:
        element.add_to_group('cranial')
    for element in mesh.elements.groups['cranial']:
        print node.id

