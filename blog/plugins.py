from mistune import markdown
# python slugfy

def configure(app):
    # {{ markdown (texto) }}
    app.add_template_global(markdown) #Adicionando um template global chamado markdown
    # {{ post.date | format_date }}
    app.add_template_filter(
        lambda date: date.strftime("%d/%m/%Y"), #Lambda é uma função anônima, simplifica a função e existe só no contexto
        # Lambda função anônima (Clean Code) - Programação funcional
        "format_date"
    )
