#!/usr/bin/env python3
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')
""" Définir une variable de type générique T """


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Récupère la valeur associée à `key` dans `dct`.
    Si `key` n'existe pas dans `dct`,
    retourne la valeur par défaut `default`.

    :param dct: Un dictionnaire ou une autre forme de mapping
    avec des clés et des valeurs de tout type.
    :param key: La clé à rechercher dans le dictionnaire.
    :param default: La valeur par défaut à retourner si la c
    lé n'existe pas dans le dictionnaire.
                    Peut être de n'importe quel type ou None.
    :return: La valeur associée à la clé si elle existe,
    sinon la valeur par défaut.
    """
    if key in dct:
        return dct[key]
    else:
        return default
