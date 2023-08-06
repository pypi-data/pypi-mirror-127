try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    # python <3.8
    import importlib_metadata  # type: ignore

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:  # pragram: no cover
    __version__ = "0.0.0"


from di.container import Container
from di.dependant import Dependant
from di.params import Depends

__all__ = ("Container", "Dependant", "Depends")
