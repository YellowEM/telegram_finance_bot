"""Категории расходов"""
from typing import Dict, List, NamedTuple



class Category(NamedTuple):
    """Структура категории"""
    codename: str
    name: str
    is_base_expense: bool
    aliases: List[str]

class Categories:
    def __init__(self)