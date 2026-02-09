from mongo_frases import inicializar_frases, obtener_frases


def frotar(n_frases: int = 1) -> list:
    inicializar_frases()
    return obtener_frases(n_frases)

from mongo_frases import insertar_frases as insertar_frases_mongo

def añadir_frases(frases: list[str]) -> None:
    insertar_frases_mongo(frases)
