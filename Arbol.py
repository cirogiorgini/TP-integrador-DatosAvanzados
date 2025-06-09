# Nodo de un arbol Binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# arbol Binario de Búsqueda (ABB)
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return Nodo(valor)
            if valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _insertar(nodo.derecha, valor)
            return nodo
        self.raiz = _insertar(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None or nodo.valor == valor:
                return nodo
            if valor < nodo.valor:
                return _buscar(nodo.izquierda, valor)
            else:
                return _buscar(nodo.derecha, valor)
        return _buscar(self.raiz, valor)

    def eliminar(self, valor):
        def _min_value_node(nodo):
            actual = nodo
            while actual.izquierda:
                actual = actual.izquierda
            return actual

        def _eliminar(nodo, valor):
            if nodo is None:
                return nodo
            if valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                temp = _min_value_node(nodo.derecha)
                nodo.valor = temp.valor
                nodo.derecha = _eliminar(nodo.derecha, temp.valor)
            return nodo
        self.raiz = _eliminar(self.raiz, valor)

    # Metodos para reccorrer el arbol
    def preorden(self):
        resultado = []
        def _preorden(nodo):
            if nodo:
                resultado.append(nodo.valor)
                _preorden(nodo.izquierda)
                _preorden(nodo.derecha)
        _preorden(self.raiz)
        return resultado

    def inorden(self):
        resultado = []
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                resultado.append(nodo.valor)
                _inorden(nodo.derecha)
        _inorden(self.raiz)
        return resultado

    def postorden(self):
        resultado = []
        def _postorden(nodo):
            if nodo:
                _postorden(nodo.izquierda)
                _postorden(nodo.derecha)
                resultado.append(nodo.valor)
        _postorden(self.raiz)
        return resultado

# Prueba del arbol
tree = ArbolBinarioBusqueda()
valores = [50, 30, 70, 20, 40, 60, 80, 10]
for v in valores:
    tree.insertar(v)

print("Inorden:", tree.inorden())
print("Preorden:", tree.preorden())
print("Postorden:", tree.postorden())

print("\nBuscando 60:", "Encontrado" if tree.buscar(60) else "No encontrado")
tree.eliminar(30)
print("\nInorden tras eliminar 30:", tree.inorden())
