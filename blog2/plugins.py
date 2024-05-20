from mistune import markdown

def configure(app):
    #{{ markdown (texto) }}
    app.add_template_global(markdown)
    #{{ date console.date | format_date }}
    app.add_template_filter(
        lambda date: date.strftime("%d/%m/%Y"),
        "format_date"
    )



