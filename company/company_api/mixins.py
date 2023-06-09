from typing import Type, TypeVar

from django.db.models import QuerySet
from rest_framework import serializers

SERIALIZER_KEY = "serializer"
QUERYSET_KEY = "queryset"

T = TypeVar("T", bound=serializers.ModelSerializer)


class ActionsMapMixin:
    """Данный миксин переопределяет логику работы с методами get_queryset
    и get_serializer_class во ViewSet через словарь action_map. Для корректной
    работы миксина в наследумеом классе необходимо создать соответствующий
    словарь, ключами в нем становятся названия методов из self.action. В
    подсловарях под ключом SERIALIZER_KEY нужно установить сериализатор,
    а под ключом QUERYSET_KEY - соответствующий запрос"""

    actions_map = None

    def get_queryset(self) -> QuerySet:
        return self.actions_map[self.action][QUERYSET_KEY]

    def get_serializer_class(self) -> Type[T]:
        return self.actions_map[self.action][SERIALIZER_KEY]
