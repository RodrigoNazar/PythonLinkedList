
if __name__ == '__main__':
    from lib.linkedlist import LinkedList

    ll = LinkedList(2)
    print('\nLista inicial:\n', ll, '\nLargo:', len(ll))

    ll.append(3)
    print('\nAppendeamos el 3:\n', ll, '\nLargo:', len(ll))

    print('\nHacemos un gran append de 5 elementos:')
    for i in range(5, 10):
        ll.append(i)

    print(ll, '\nLargo', len(ll))

    print('\nIntentamos borrar el 9 de la lista (ultimo elemento):')

    ll.remove(9)

    print('\nLa lista después de borrarlo:\n', ll, '\nLargo: ', len(ll))

    print('\nIntentamos borrar el 2 de la lista (primer elemento):')

    ll.remove(2)

    print('\nLa lista después de borrarlo:\n', ll, '\nLargo: ', len(ll))

    print('\nIntentamos borrar el 2 de la lista (elemento del medio):')

    ll.remove(6)

    print('\nLa lista después de borrarlo:\n', ll, '\nLargo: ', len(ll))

    ll.append('hola')

    print(ll)
