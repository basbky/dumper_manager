import pytest
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from dumpers.models import Dumper, Model


class ModelFactory(DjangoModelFactory):
    name = FuzzyText()
    load_capacity = 100

    class Meta:
        model = Model


class DumperFactory(DjangoModelFactory):
    tail_number = FuzzyText()
    model = SubFactory(ModelFactory)
    load_weight = 50

    class Meta:
        model = Dumper


@pytest.fixture
def model():
    return ModelFactory()


@pytest.fixture
def dumper(model):
    return DumperFactory(model=model)


@pytest.mark.django_db(transaction=True)
def test_dumper_str(dumper):
    assert str(dumper) == dumper.tail_number


@pytest.mark.django_db(transaction=True)
def test_dumper_create(dumper):
    assert Dumper.objects.count() == 1
    assert Dumper.objects.first() == dumper


@pytest.mark.django_db(transaction=True)
def test_dumper_load_weight(dumper):
    assert dumper.load_weight == 50


@pytest.mark.django_db(transaction=True)
def test_model_str(model):
    assert str(model) == model.name


@pytest.fixture
def models():
    return ModelFactory.create_batch(5)
