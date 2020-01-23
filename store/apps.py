from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class StoreConfig(AppConfig):
    name = 'store'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'