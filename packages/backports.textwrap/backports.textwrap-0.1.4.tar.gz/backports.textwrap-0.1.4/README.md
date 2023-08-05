# textwrap

[![PyPI version](https://badge.fury.io/py/backports.textwrap.svg)](https://badge.fury.io/py/backports.textwrap)

A backport of upcoming python/cpython#28136 with some additional fixes.

Motivated due to jquast/blessed using textwrap, but this fails for zero-width characters. This allows setting text_len
to, for example, wcswidth for more accuracy when word wrapping in the terminal.

This uses the backports package style, see https://pypi.python.org/pypi/backports.
