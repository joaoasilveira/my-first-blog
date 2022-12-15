from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    FORMATACAO_COM_BKP = "FCB", "Formatação com Backup"
    FORMATACAO_SEM_BKP = "FSB", "Formatação sem Backup"
    MONTAGEM_DESKTOP_COMPLETA = "MDC", "Montagem de Desktop Completa"
    MONTAGEM_NOTEBOOK_COMPLETA = "MNC", "Montagem de Notebook Completa"
    LIMPEZA_COMPLETA = "LC", "Limpeza Completa"
