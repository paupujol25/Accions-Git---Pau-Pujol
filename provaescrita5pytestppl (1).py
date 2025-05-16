import pytest
from provaescrita5pytestppl import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

def setup_biblioteca():
    """
    Configura una biblioteca d'exemple per a les proves.
    Retorna:
        biblioteca (llista de diccionaris): Una estructura de dades de biblioteca predefinida.
    """
    return [
        {
            "llibre": "El Quixot", 
            "autor": "Cervantes",
            "categoria": "novel·la",
            "prestecs": [
                {"usuari": "Joan", "dies": 15, "retornat": True},
                {"usuari": "Maria", "dies": 20, "retornat": False},
                {"usuari": "Pere", "dies": 12, "retornat": True}
            ]
        },
        {
            "llibre": "1984",
            "autor": "Orwell",
            "categoria": "ciència-ficció",
            "prestecs": [
                {"usuari": "Pere", "dies": 10, "retornat": True},
                {"usuari": "Anna", "dies": 25, "retornat": True},
                {"usuari": "Marta", "dies": 18, "retornat": False}
            ]
        },
        {
            "llibre": "El Senyor dels Anells",
            "autor": "Tolkien",
            "categoria": "fantasia",
            "prestecs": [
                {"usuari": "Maria", "dies": 30, "retornat": True},
                {"usuari": "Joan", "dies": 22, "retornat": True},
                {"usuari": "Pere", "dies": 15, "retornat": False}
            ]
        },
        {
            "llibre": "Crim i Càstig",
            "autor": "Dostoievski",
            "categoria": "novel·la",
            "prestecs": [
                {"usuari": "Anna", "dies": 28, "retornat": True},
                {"usuari": "Marta", "dies": 14, "retornat": True},
                {"usuari": "Joan", "dies": 21, "retornat": True}
            ]
        }
    ]

@pytest.mark.parametrize("categoria, esperat", [
    ("novel·la", ["El Quixot", "Crim i Càstig"]),
    ("ciència-ficció", ["1984"]),
    ("fantasia", ["El Senyor dels Anells"]),
    ("poesia", [])
])
def test_llibres_per_categoria(categoria, esperat):
    """
    Test de la funció llibres_per_categoria per comprovar si retorna correctament els títols segons la categoria.
    """
    biblioteca = setup_biblioteca()
    assert llibres_per_categoria(biblioteca, categoria) == esperat

@pytest.mark.parametrize("llibre, esperat", [
    ("El Quixot", False),
    ("1984", False),
    ("El Senyor dels Anells", False),
    ("Crim i Càstig", True)
])
def test_esta_disponible(llibre, esperat):
    """
    Test de la funció esta_disponible per comprovar si indica correctament la disponibilitat d'un llibre.
    """
    biblioteca = setup_biblioteca()
    assert esta_disponible(biblioteca, llibre) == esperat

@pytest.mark.parametrize("usuari, esperat", [
    ("Joan", False),
    ("Maria", True),
    ("Pere", True),
    ("Anna", False)
])
def test_usuari_te_prestecs(usuari, esperat):
    """
    Test de la funció usuari_te_prestecs per comprovar si detecta correctament usuaris amb préstecs pendents.
    """
    biblioteca = setup_biblioteca()
    assert usuari_te_prestecs(biblioteca, usuari) == esperat

@pytest.mark.parametrize("llibre, esperat", [
    ("El Quixot", 47),
    ("1984", 53),
    ("El Senyor dels Anells", 67),
    ("Crim i Càstig", 63)
])
def test_dies_prestec_total(llibre, esperat):
    """
    Test de la funció dies_prestec_total per comprovar si calcula correctament els dies totals de préstec.
    """
    biblioteca = setup_biblioteca()
    assert dies_prestec_total(biblioteca, llibre) == esperat
