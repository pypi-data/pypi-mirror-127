"""
Stub representaton of the public objects exposed by the _psycopg module.

TODO: this should be generated by mypy's stubgen but it crashes with no
information. Will submit a bug.
"""

# Copyright (C) 2020-2021 The Psycopg Team

from typing import Any, Iterable, List, Optional, Sequence, Tuple

from psycopg import pq
from psycopg import abc
from psycopg.rows import Row, RowMaker
from psycopg.adapt import AdaptersMap, PyFormat
from psycopg.pq.abc import PGconn, PGresult
from psycopg.connection import BaseConnection

class Transformer(abc.AdaptContext):
    types: Optional[Tuple[int, ...]]
    formats: Optional[List[pq.Format]]
    def __init__(self, context: Optional[abc.AdaptContext] = None): ...
    @property
    def connection(self) -> Optional[BaseConnection[Any]]: ...
    @property
    def adapters(self) -> AdaptersMap: ...
    @property
    def pgresult(self) -> Optional[PGresult]: ...
    def set_pgresult(
        self,
        result: Optional["PGresult"],
        *,
        set_loaders: bool = True,
        format: Optional[pq.Format] = None,
    ) -> None: ...
    def set_dumper_types(
        self, types: Sequence[int], format: pq.Format
    ) -> None: ...
    def set_loader_types(
        self, types: Sequence[int], format: pq.Format
    ) -> None: ...
    def dump_sequence(
        self, params: Sequence[Any], formats: Sequence[PyFormat]
    ) -> Sequence[Optional[abc.Buffer]]: ...
    def get_dumper(self, obj: Any, format: PyFormat) -> abc.Dumper: ...
    def load_rows(
        self, row0: int, row1: int, make_row: RowMaker[Row]
    ) -> List[Row]: ...
    def load_row(self, row: int, make_row: RowMaker[Row]) -> Optional[Row]: ...
    def load_sequence(
        self, record: Sequence[Optional[bytes]]
    ) -> Tuple[Any, ...]: ...
    def get_loader(self, oid: int, format: pq.Format) -> abc.Loader: ...

# Generators
def connect(conninfo: str) -> abc.PQGenConn[PGconn]: ...
def execute(pgconn: PGconn) -> abc.PQGen[List[PGresult]]: ...
def send(pgconn: PGconn) -> abc.PQGen[None]: ...
def fetch_many(pgconn: PGconn) -> abc.PQGen[List[PGresult]]: ...
def fetch(pgconn: PGconn) -> abc.PQGen[Optional[PGresult]]: ...

# Copy support
def format_row_text(
    row: Sequence[Any], tx: abc.Transformer, out: Optional[bytearray] = None
) -> bytearray: ...
def format_row_binary(
    row: Sequence[Any], tx: abc.Transformer, out: Optional[bytearray] = None
) -> bytearray: ...
def parse_row_text(data: bytes, tx: abc.Transformer) -> Tuple[Any, ...]: ...
def parse_row_binary(data: bytes, tx: abc.Transformer) -> Tuple[Any, ...]: ...

# vim: set syntax=python:
