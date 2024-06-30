from pelican import signals
import markdown

def parse_toggle_content(generator, content):
    """
    Converts the {% toggle %} tag into a details/summary HTML tag and processes Markdown within.
    """
    content = content._content
    toggle_start = "{% toggle %}"
    toggle_end = "{% end_toggle %}"
    if toggle_start in content and toggle_end in content:
        start_index = content.find(toggle_start) + len(toggle_start)
        end_index = content.find(toggle_end)
        toggle_content = content[start_index:end_index]
        # Reemplazar el contenido original con el procesado
        details_tag = f"<details><summary>Demostración</summary>{toggle_content}</details>"
        print(details_tag)
        content = content.replace(f"{toggle_start}{toggle_content}{toggle_end}", details_tag)

    return content

def register():
    signals.article_generator_write_article.connect(parse_toggle_content)