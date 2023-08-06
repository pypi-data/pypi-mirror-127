#!/usr/bin/env python3
# flake8: noqa

"""Import ``graphviz`` here and run all scripts in the ``examples/`` dir."""

import os
import pathlib
import sys
import unittest.mock
import warnings

import graphviz  # noqa: F401

EXAMPLES = pathlib.Path('examples')

IO_KWARGS = {'encoding': 'utf-8'}

DEFAULT_FORMAT = 'pdf'


os.chdir(EXAMPLES)

graphviz.set_default_format(DEFAULT_FORMAT)

raised = []

with unittest.mock.patch.object(graphviz.graphs.BaseGraph, '_view') as mock_view:
    for path in pathlib.Path().glob('*.py'):
        print(path)
        code = path.read_text(**IO_KWARGS)
        try:
            exec(code)
        except Exception as e:
            raised.append(e)
            warnings.warn(e)
        else:
            rendered = f'{path.stem}.gv.{DEFAULT_FORMAT}'
            assert pathlib.Path(rendered).stat().st_size, f'non-empty {rendered}'
            mock_view.assert_called_once_with(rendered, DEFAULT_FORMAT, False)
            mock_view.reset_mock()

if not raised:
    print('all examples passed without raising (OK)')
    sys.exit(None)
else:
    message = f'{len(raised)} examples raised (WARNING)'
    print(message, *raised, sep='\n')
    sys.exit(message)
