=====================
qly command reference
=====================

val
===

Synopsis
--------

``val`` - sets a variable.

The variable can then be accessed by various commands.

Arguments
---------

variable
^^^^^^^^
The name of the variable to store the value into. Must start with a dot ..

type
^^^^
Type of the value. Must be one of: ``int``, ``bool``.

value
^^^^^
Value of the variable. Must match the selected type.

Examples
--------

.. code-block:: text

    val .integer int 5
    val .true bool true
    val .false bool false

ln
===

Synopsis
--------
``ln`` - prints a line to the screen.

Must provide a variable.

Arguments
---------

variable
^^^^^^^^
The name of the variable who's content should be printed to the screen.

Examples
--------

.. code-block:: text
    
    val .bool bool true
    val .int int 18
    ln .bool
    ln .int