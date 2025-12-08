import pytest

from tasks.storage_package.limited_storage import LimitedStorage


def test_init_with_valid_capacity():
    storage = LimitedStorage[int](capacity=3)
    assert storage.capacity == 3
    assert storage.len() == 0
    assert not storage.is_full()


def test_init_with_invalid_capacity():
    with pytest.raises(ValueError) as exc:
        LimitedStorage[int](capacity=0)
    assert "Ёмкость хранилища должна быть больше нуля" in str(exc.value)


def test_init_with_items_exceeding_capacity():
    with pytest.raises(ValueError) as exc:
        LimitedStorage[int](items=[1, 2, 3], capacity=2)
    assert "Начальный список элементов превышает ёмкость хранилища" in str(exc.value)


def test_add_item():
    storage = LimitedStorage[str](capacity=2)
    storage.add("элемент1")
    assert storage.len() == 1
    storage.add("элемент2")
    assert storage.len() == 2
    assert storage.is_full()


def test_add_item_overflow():
    storage = LimitedStorage[str](capacity=1)
    storage.add("элемент")
    with pytest.raises(OverflowError) as exc:
        storage.add("новый элемент")
    assert "Хранилище заполнено— невозможно добавить новый элемент" in str(exc.value)


def test_is_full_method():
    storage = LimitedStorage[int](capacity=2)
    assert not storage.is_full()
    storage.add(10)
    assert not storage.is_full()
    storage.add(20)
    assert storage.is_full()


def test_repr_method():
    storage = LimitedStorage[int](capacity=2)
    storage.add(5)
    repr_str = repr(storage)
    assert "Ограниченное Хранилище" in repr_str
    assert "вместимость=2" in repr_str
    assert "5" in repr_str
