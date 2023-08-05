Chrysalio README
================

Getting Started
---------------

.. code-block:: bash

    $ cd <directory containing this file>
    $ source $VENV/bin/activate
    (virtualenv)$ pip install -e .
    (virtualenv)$ ciopopulate development.ini
    (virtualenv)$ pserve development.ini


Testing the Application
-----------------------

.. code-block:: bash

    (virtualenv)$ pip install -e ".[testing]"
    (virtualenv)$ py.test --pep8 --last-failed -v --cov --cov-report=term-missing


Developping the Application
---------------------------

.. code-block:: bash

    (virtualenv)$ pip install -e ".[development]"

..
   Creating a new Chrysalio Project
   --------------------------------

   (virtualenv)$ pcreate -s chrysalio_project MyProject

   Creating a new Chrysalio Theme
   ------------------------------

   (virtualenv)$ pcreate -s chrysalio_theme MyTheme


Generating Localization Files
-----------------------------

.. code-block:: bash

    (virtualenv)$ ./i18n.sh
