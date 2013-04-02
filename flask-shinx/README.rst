build
=====

次のコマンドでビルド ::

    % tree source
    source/
    ├── _static
    ├── _templates
    ├── app
    │   ├── myapp.py
    │   └── myapp.pyc
    ├── conf.py
    └── index.rst

    3 directories, 4 files
    % PYTHONPATH=source/app make html
