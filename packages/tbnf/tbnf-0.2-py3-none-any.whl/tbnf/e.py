from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, TYPE_CHECKING
from json import dumps

from tbnf.common import Pos, ref, TypeTaggable, Ref
if TYPE_CHECKING:
    from tbnf import t

Tag = TypeVar("Tag")


class ExDynamic:
    def show(self):
        raise NotImplementedError


def custom_show(e, *args):
    return e.show(*args)


@dataclass(order=True, frozen=True)
class Tuple(ExDynamic):
    _: tuple[Expr]

@dataclass(order=True, frozen=True)
class List(ExDynamic):
    _: tuple[Expr]

@dataclass(order=True, frozen=True)
class Int(ExDynamic):
    _: int


@dataclass(order=True, frozen=True)
class Float(ExDynamic):
    _: float

@dataclass(order=True, frozen=True)
class Bool(ExDynamic):
    _: bool

@dataclass(order=True, frozen=True)
class String(ExDynamic):
    _: float


@dataclass(order=True, frozen=True)
class App(ExDynamic):
    func: Expr
    args: tuple[Expr, ...]

    def __post_init__(self):
        assert isinstance(self.args, tuple)

@dataclass(order=True, frozen=True)
class Lam(ExDynamic):
    args: tuple[str, ...]
    reta: Expr


@dataclass(order=True, frozen=True)
class Attr:
    value: Expr
    attr: str


@dataclass(order=True, frozen=True)
class Binder:
    name: str
    value: Expr
    pos: Pos


@dataclass(order=True, frozen=True)
class Let(ExDynamic):
    rec: bool
    binders: tuple[Binder, ...]
    body: Expr


@dataclass
class Var(ExDynamic):
    _: str

    inst_targs: dict[t.BoundVar, t.TyStatic] | None = None
    generic : t.Forall | None = None


@dataclass(order=True, frozen=True)
class Slot(ExDynamic):
    _: int


@dataclass(order=True, frozen=True)
class While(ExDynamic):
    cond: Expr
    body: Expr


@dataclass(order=True, frozen=True)
class Block(ExDynamic):
    _: tuple[Expr, ...]


@dataclass
class Expr(TypeTaggable, Generic[Tag]):
    _tag: Tag
    _: ExStatic
    pos: Pos

ExStatic = (
    Attr
    | Tuple
    | Var
    | Let
    | Lam
    | App
    | String
    | Float
    | Int
    | Slot
    | While
    | Block
    | Bool
    | List
)

