from enum import Enum

from MSApi.MSLowApi import MSLowApi, error_handler
from MSApi.ObjectMS import ObjectMS, check_init
from MSApi.Meta import Meta
from MSApi.PriceType import PriceType
from MSApi.CustomEntity import CustomEntity


class DiscountStrategy(Enum):
    e_by_sum = "bySum"
    e_by_priority = "byPriority"


class CompanySettings(ObjectMS):
    def __init__(self, json):
        super().__init__(json)

    @check_init
    def get_currency(self) -> Meta:
        """Метаданные стандартной валюты"""
        return Meta(self._json.get('currency'))

    @check_init
    def gen_price_types(self):
        """Коллекция всех существующих типов цен."""
        for price_type in self._json.get('priceTypes'):
            yield PriceType(price_type)

    @check_init
    def get_discount_strategy(self) -> DiscountStrategy:
        """Совместное применение скидок."""
        return DiscountStrategy(self._json.get('discountStrategy'))

    @check_init
    def get_global_operation_numbering(self) -> bool:
        """Использовать сквозную нумерацию документов.
        Если проставлен true, будет установлена сквозная нумерация за всю историю,
        иначе нумерация документов будет начинаться заново каждый календарный год."""
        return bool(self._json.get('globalOperationNumbering'))

    @check_init
    def gen_custom_entities(self):
        response = MSLowApi.auch_get("context/companysettings/metadata")
        error_handler(response)
        for entity_json in response.json().get('customEntities', []):
            yield CustomEntity(entity_json)


