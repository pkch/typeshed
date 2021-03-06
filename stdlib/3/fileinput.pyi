from typing import Iterable, Callable, IO, AnyStr, Generic, Any, Union, Iterator, Optional

import os
import sys

if sys.version_info >= (3, 6):
    _Path = Union[str, bytes, os.PathLike[Any]]
else:
    _Path = Union[str, bytes]
_Opener = Callable[[_Path, str], IO[AnyStr]]


def input(
    files: Union[str, Iterable[str]]=None,
    inplace: bool=...,
    backup: str=...,
    bufsize: int=...,
    mode: str=...,
    openhook: Callable[[str, str], IO[AnyStr]]=...) -> Iterable[AnyStr]: ...


def close() -> None: ...
def nextfile() -> None: ...
def filename() -> str: ...
def lineno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...

class FileInput(Iterable[AnyStr], Generic[AnyStr]):
    def __init__(
        self,
        files: Union[None, _Path, Iterable[_Path]] = ...,
        inplace: bool = ...,
        backup: str = ...,
        bufsize: int = ...,
        mode: str = ...,
        openhook: _Opener[AnyStr] = ...
    ) -> None: ...

    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> 'FileInput[AnyStr]': ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def __iter__(self) -> Iterator[AnyStr]: ...
    def __next__(self) -> AnyStr: ...
    def __getitem__(self, i: int) -> AnyStr: ...
    def nextfile(self) -> None: ...
    def readline(self) -> AnyStr: ...
    def filename(self) -> str: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...

def hook_compressed(filename: _Path, mode: str) -> IO[Any]: ...
def hook_encoded(encoding: str, errors: Optional[str] = ...) -> _Opener[Any]: ...
