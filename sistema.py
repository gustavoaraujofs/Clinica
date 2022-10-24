import abc

class Sistema(abc.ABC):

    @abc.abstractclassmethod
    def cadastrar(self):
        pass

    @abc.abstractclassmethod
    def agendar(self):
        pass

    @abc.abstractclassmethod
    def listar(self):
        pass

    @abc.abstractclassmethod
    def listar_pac(self):
        pass

    @abc.abstractclassmethod
    def deletar(self):
        pass
