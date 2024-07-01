import re

from pelican import signals

TOGGLE_REGEX = r"\{% toggle %\}(.*?)\{% end_toggle %\}"


def toggle_to_details(generator):
    def replace_toggle(match):
        inner_content = match.group(1).strip()
        summary = "<summary>Demostración</summary>"
        details = f"<details>{summary}{inner_content}</details>"
        return details

    for article in generator.articles:
        article._content = re.sub(
            TOGGLE_REGEX, replace_toggle, article._content, flags=re.DOTALL
        )


def register():
    signals.article_generator_finalized.connect(toggle_to_details)
