import time
import sys

def barra_progresso(iteravel, prefixo='', tamanho=60, preenchimento='█'):
    total = len(iteravel)

    def imprimir_barra(atual):
        percentual = ("{0:.1f}").format(100 * (atual / float(total)))
        preenchido = int(tamanho * atual // total)
        barra = preenchimento * preenchido + '-' * (tamanho - preenchido)
        sys.stdout.write(f'\r{prefixo} |{barra}| {percentual}% Completo')
        sys.stdout.flush()

    imprimir_barra(0)
    for i, item in enumerate(iteravel):
        yield item
        imprimir_barra(i + 1)
    sys.stdout.write('\n') 
    sys.stdout.flush()

print("Iniciando a barra de progresso...")

itens = range(200)

for item in barra_progresso(itens, prefixo='Progresso', tamanho=50):
    time.sleep(0.01)

print("Barra de progresso concluída!")