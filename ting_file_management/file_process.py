import sys
from .file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for content in instance.data:
        if content["nome_do_arquivo"] == path_file:
            return
    listed_file = txt_importer(path_file)

    new_information = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(listed_file),
        "linhas_do_arquivo": listed_file,
    }
    instance.enqueue(new_information)
    sys.stdout.write(f'{new_information}')


def remove(instance):
    """Aqui irá sua implementação"""
    if(len(instance.data) == 0):
        return sys.stdout.write('Não há elementos\n')
    file_to_delete = instance.dequeue()
    sys.stdout.write(
        f'Arquivo {file_to_delete["nome_do_arquivo"]} removido com sucesso\n'
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
