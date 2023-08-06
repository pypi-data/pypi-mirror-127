"""
PyDetex
https://github.com/ppizarror/PyDetex

PIPELINES
Defines the pipelines which apply parsers.
"""

__all__ = [
    'simple',
    'strict',
    'PipelineType'
]

import pydetex.parsers as par
from typing import Callable

PipelineType = Callable[[str, str], str]


def simple(s: str, lang: str = 'en', cite_replace_tags: bool = True) -> str:
    """
    The most simple pipeline ever.

    :param s: String latex
    :param lang: Language tag of the code
    :param cite_replace_tags: Replace cite tags
    :return: String with no latex!
    """
    if len(s) == 0:
        return s
    s = '\n'.join(s.splitlines())  # Removes \r\n
    s = par.remove_comments(s)
    s = par.simple_replace(s)
    s = par.remove_common_tags(s)
    s = par.process_cite(s)
    s = par.process_ref(s)
    s = par.process_labels(s)
    s = par.process_items(s)
    s = par.process_quotes(s)
    s = par.process_inputs(s)
    s = par.process_chars_equations(s, lang, True)
    s = par.unicode_chars_equations(s)
    if len(s) > 0 and s[-1] == '\\':
        s = s[0:len(s) - 1]
    s = par.remove_comments(s)  # comments, replace tags, strip
    if cite_replace_tags:
        s = par.replace_pydetex_tags(s)
    s = par.strip_punctuation(s)
    return s


def strict(s: str, lang: str = 'en') -> str:
    """
    Applies simple + removes all commands.

    :param s: String latex
    :param lang: Language tag of the code
    :return: String with no latex!
    """
    s = simple(s, lang, cite_replace_tags=False)
    s = par.process_chars_equations(s, lang, False)
    s = par.remove_equations(s)
    s = par.remove_commands_param(s, lang)
    s = par.remove_commands_param_noargv(s)
    s = par.remove_comments(s)
    s = par.replace_pydetex_tags(s)
    s = par.strip_punctuation(s)
    return s
