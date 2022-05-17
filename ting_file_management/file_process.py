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


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
