import logging
import os
from logging.config import dictConfig
from pathlib import Path
from typing import Optional, Union

import coloredlogs
from jinja2 import (
    Environment,
    FileSystemLoader,
    PackageLoader,
    Template,
    select_autoescape,
)

SEARCH_URL = "https://idord.arnastofnun.is/leit/{}/ordabok/{}"

jinja2_env = Environment(loader=PackageLoader("sphinxcontrib.hoverrole","hoverrole/templates"), autoescape=select_autoescape())


def configure_logger(name):
    level = os.getenv("LOG_LEVEL", "INFO")
    fmt = "%(name)s(%(lineno)d): [%(levelname)s] %(message)s"
    styles = coloredlogs.DEFAULT_FIELD_STYLES | {
        "levelname": {"bold": True, "color": "blue", "faint": True}
    }
    logger = logging.getLogger(name)
    coloredlogs.install(fmt=fmt, field_styles=styles, level=level, logger=logger)
    return logger


def serialize(items: list) -> str:
    if items and isinstance(items, list):
        return ", ".join(items)
    return items


def get_html(
    tpl: str, word: str, term: str, terms: list, ordabok: str, html_link: bool = False, stae_index: bool = None
) -> str:
    url: Optional[str] = SEARCH_URL.format(term, ordabok) if html_link else None
    template = jinja2_env.get_template(tpl)
    return template.render(word=word, term=terms, url=url)


def get_latex(latexIt: bool, latexLink: bool, word: str, term: str) -> str:
    if latexIt:
        return f"\\textit{{{word}}}"
    if latexLink:
        url = SEARCH_URL.format(term, ordabok)
        return f"\\href{{{url}}}{{{word}}}"
    return word


def get_translations_file():
    # TODO: add to extension config
    return "LIST_OF_HOVER_TERMS.json"
