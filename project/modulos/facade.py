from typing import List
from project.modulos.models import Modulo, Aula
from django.db.models import Prefetch


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados pela ordem definida
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def listar_modulos_com_aulas():
    """
    Lista módulos com as aulas
    """
    aulas_ordenadas = Aula.objects.order_by('order').all()
    return Modulo.objects.order_by('order').prefetch_related(Prefetch('aula_set', aulas_ordenadas, 'aulas')).all()