#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass, field


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    category: str


@dataclass
class Product_list:
    products: list[Product] = field(default_factory=list)

    def add(self, name: str, price: float, category: str) -> None:
        new_product = Product(name=name, price=price, category=category)
        self.products.append(new_product)
        self.products.sort(key=lambda product: product.name)

    def get_products_by_category(self, category: str) -> str:
        filtered_products = [
            product for product in self.products if product.category == category
        ]
        if not filtered_products:
            return f"В категории '{category}' нет продуктов."
        return f"Продукты в категории '{category}':\n" + "\n".join(
            f"- {product.name}: {product.price} ({product.category})"
            for product in filtered_products
        )

    def __str__(self) -> str:
        try:
            if not self.products:
                raise ValueError(
                    "Списко продуктов пуст, добавьте хотя бы один продукт."
                )
            return "Список продуктов:\n" + "\n".join(
                f"- {product.name}: {product.price} ({product.category})"
                for product in self.products
            )
        except Exception as ex:
            return f"Ошибка: {ex}"


if __name__ == "__main__":
    product_list = Product_list()
    product_list.add("Banana", 0.8, "Fruits")
    product_list.add("Apple", 1.2, "Fruits")
    product_list.add("Carrot", 0.5, "Vegetables")
    print(product_list.get_products_by_category("Fruits"))
    print(product_list.get_products_by_category("Meat"))

    print(product_list)
