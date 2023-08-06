from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    final,
)

from typing_extensions import Annotated


@final
class JSON:
    ...


# For use in Config and settings module annotations only.
JSONList = Annotated[list, JSON]
JSONDict = Annotated[dict, JSON]


class _NotAnnotated:

    def __getitem__(self, item: Type[_T]) -> Type[_T]:
        ...


NotAnnotated: _NotAnnotated


class _NotNull:

    def __getitem__(self, item: Type[Optional[_T]]) -> Type[_T]:
        ...


NotNull: _NotNull


class _Empty:
    ...


empty: _Empty


def as_property_name(name: str) -> str:
    ...


_T = TypeVar("_T")
_D = TypeVar("_D")

_C = Callable[[str], _T]
_JSBase = Union[str, bool, int, float, None, List, Dict]
_JS = Union[_JSBase, List[_JSBase], Dict[str, _JSBase]]
_Seq = Union[Mapping[str, str], Iterable[Tuple[str, str]]]


def validate_setting_value(name: str, value: _T, annotation, allow_null: bool) -> Tuple[str, _T]:
    ...


class Env:

    @classmethod
    def get_default(cls) -> Env:
        ...

    @classmethod
    def load(
        cls: Type[_T],
        strict: bool = ...,
        *,
        variable: Optional[str] = ...,
        filename: str = ...,
        path: str = ...,
        find: bool = ...
    ) -> _T:
        ...

    def __init__(self, __updates: _Seq = ..., **updates: str):
        ...

    def get_by_annotations(
        self,
        obj: Any,
        key_to_name: Optional[Callable[[str], str]] = ...,
        name_is_setting: Optional[Callable[[str], bool]] = ...,
        custom_processing: Optional[Dict[str, Callable[[], Any]]] = ...,
    ) -> Iterator[Tuple[str, Any]]:
        ...

    @staticmethod
    def read(key: str, cast: _C, *, default: _D = ...) -> Union[_D, _T]:
        ...

    def tuple(self, key: str, *, default: _D = ...) -> Union[_D, Tuple[str, ...]]:
        ...

    def float(self, key: str, *, default: _D = ...) -> Union[_D, float]:
        ...

    def bool(self, key: str, *, default: _D = ...) -> Union[_D, bool]:
        ...

    def json(self, key: str, *, default: _D = ...) -> Union[_D, _JS]:
        ...

    def json_list(self, key: str, *, default: _D = ...) -> Union[_D, list]:
        ...

    def json_dict(self, key: str, *, default: _D = ...) -> Union[_D, dict]:
        ...

    def list(self, key: str, *, default: _D = ...) -> Union[_D, List[str]]:
        ...

    def dict(self, key: str, *, default: _D = ...) -> Union[_D, Dict[str, str]]:
        ...

    def int(self, key: str, *, default: _D = ...) -> Union[_D, int]:
        ...

    def str(self, key: str, *, default: _D = ...) -> Union[_D, str]:
        ...
