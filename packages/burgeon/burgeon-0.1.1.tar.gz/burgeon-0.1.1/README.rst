Burgeon - Python Code Reloading
-------------------------------

This project exposes one function -- `with_reloading` -- which is used to run a
single callable. This callable gets run in a separate thread which gets
restarted whenever a Python source file from the current working directory down
changes. This improves the development cycle by removing the need to manually
restart long running services whenever its source code changes.

> Burgeon: To grow or develop rapidly; expand or proliferate.

Example Usage
=============

.. code-block:: python

    from burgeon import with_reloading


    def my_function():
        while True:
            print("hello")

    with_reloading(func)

The function above demonstrates a minimal example of using `with_reloading`.
Once the code is executed, any changes to the file (that get saved) will notify
`burgeon` to restart the thread running the function and execute the new
changes.

Acknowledgements
================

This implementation of Python file reloading uses watchgod and is heavily based
off the `BaseReload` class in the `uvicorn`_ repository. For context, this is
how uvicorn implements its own development server reloading. This project
simplifies the implementation and exposes the reloading functionality via a
simple and opinionated interface.

.. _uvicorn: https://github.com/encode/uvicorn