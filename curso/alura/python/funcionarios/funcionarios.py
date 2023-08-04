class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('horas registradas.')

    def mostrar_tarefas(self):
        print('fez muita cosia...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa, caelumer')

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do forum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'
        

class Junior(Alura):
    pass
class Pleno(Alura,Caelum,Hipster):
    pass

jose = Junior('josé')
jose.busca_perguntas_sem_resposta()

luan = Pleno('luan')
luan.busca_perguntas_sem_resposta()
luan.busca_curso_do_mes()

luan.mostrar_tarefas()

print(luan)


