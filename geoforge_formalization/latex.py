"""LaTeX input helpers with explicit rejection of unsupported commands."""
import re
from geoforge_upgrade_suite.formal_language import LaTeXGeometryParser
_SUPPORTED = ("\\angle", "\\parallel", "\\perp", "\\overline")
def contains_unrecognized_commands(source):
    commands=set(re.findall(r'\\[A-Za-z]+',source))
    return tuple(sorted(commands-set(_SUPPORTED)))
__all__=["LaTeXGeometryParser","contains_unrecognized_commands"]
