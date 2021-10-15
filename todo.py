from functools import reduce


last = lambda Li: Li[len(Li)-1]
inicial = lambda Li: Li[0][0].capitalize() + ". "


def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """
    
    return list( map( last, L ) )
    

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """

    return list( map( lambda Li: inicial(Li) + last(Li), L ) )


def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """

    iniciais = lambda Li: reduce( lambda str, si: str + si[0].capitalize() + ". ", Li[:len(Li)-1], "" )
    fcit = lambda Li: iniciais(Li) + last(Li)
    return list( map( fcit, L ) )



L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]

L2 = [ ['Antonio', 'Franco', 'Molina'],
       ['Caius', 'vitelus', 'Aquarius'],
       ['cristovao', 'buarque', 'Holanda'] ]



print( "Last: ", lastNames(L2) )

print( "Citação: ", citations(L2) ) 

print( "Full Citação: ", fullCitations(L2) ) 