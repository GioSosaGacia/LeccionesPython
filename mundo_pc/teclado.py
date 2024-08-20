from mundo_pc.dispositivo_enttrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contatador_teclados = 0
    def __init__(self,marca,tipo_entrada):
        Teclado.contatador_teclados += 1
        self.id_teclado = Teclado.contatador_teclados
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self._marca},' \
               f'Tipo_Entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('Samgsum','USB')
    print(teclado1)
    teclado2 = Teclado('Lg','Bluetooth')
    print(teclado2)
