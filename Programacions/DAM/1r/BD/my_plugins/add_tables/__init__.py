try:
    from .plugin import AddTablesPlugin
except ModuleNotFoundError:
    # La generació directa del PDF només necessita transformer.py.
    AddTablesPlugin = None
