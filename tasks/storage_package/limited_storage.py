#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass
class LimitedStorage(Generic[T]):

    items: List[T] = field(default_factory=list, repr=False)
    capacity: int = 1

    def __post_init__(self) -> None:
        if self.capacity <= 0:
            raise ValueError("Ёмкость хранилища должна быть больше нуля")
        if len(self.items) > self.capacity:
            raise ValueError("Начальный список элементов превышает ёмкость хранилища")

    def add(self, item: T) -> None:
        if len(self.items) >= self.capacity:
            raise OverflowError(
                "Хранилище заполнено— невозможно добавить новый элемент"
            )
        self.items.append(item)

    def len(self) -> int:
        return len(self.items)

    def is_full(self) -> bool:
        return len(self.items) == self.capacity

    def __repr__(self) -> str:
        return f"Ограниченное Хранилище\
    (вместимость={self.capacity}, элементы={self.items})"
