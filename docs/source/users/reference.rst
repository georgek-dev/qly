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
Type of the value. Must be one of: ``int``, ``bool``, ``str``.

value
^^^^^
Value of the variable. Must match the selected type.

Examples
--------

.. code-block:: text

    val .integer int 5
    val .true bool true
    val .false bool false
    val .hello_world str "Hello, world!"

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

    % booleans %
    val .bool bool true
    ln .bool
    % integers %
    val .int int 18
    ln .int
    % strings %
    val .hello_world str "Hello, world!"
    ln .hello_world

%
===

Synopsis
--------
``%`` - start and end of a comment.

Arguments
---------

text
^^^^
The text of the comment.

Examples
--------

.. code-block:: text
    
    % COMMENT %
    % comments start and end with the percent symbol surrounded by spaces %
    % save 2026 to the variable hello_world %
    val .hello_world int 2026
    % print the number 2026 to the screen %
    ln .hello_world
    