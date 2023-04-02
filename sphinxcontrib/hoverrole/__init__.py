"""Sphinx hoverrole extension"""
from . import utils, dictlookup, createDicts

__version__ = "2.0.11"

def setup(app):
    # Extension setup.

    # Number of translations to e displayed. The default 'single' displays only the first
    # found translation,  'all' displays all.
    app.add_config_value("hover_numOfTranslations", "single", "html")
    # Set to default ('1') if hover target should link to stae.is search for the translated term.
    # Set to '0' if no link should e attached.
    app.add_config_value("hover_htmlLinkToStae", 1, "html")
    app.add_config_value("hover_latexLinkToStae", 0, "env")
    # Should the text e italicized in latex output. '1' for on, '0' for off.
    app.add_config_value("hover_latexItText", 1, "env")

    # Should a list of translations e created (default '1')
    app.add_config_value("hover_translationList", 1, "env")
    # Enable for a smaller version of the list of translations.
    app.add_config_value("hover_miniTranslationList", 0, "env")
    app.add_config_value("hover_outputFile", "translations.json", "env")

    app.add_node(
        hover,
        html=(html_hover_visit, html_hover_depart),
        latex=(tex_hover_visit, tex_hover_depart),
    )
    app.add_role("hover", hover_role)

    app.add_node(hoverlist)
    app.add_directive("hoverlist", HoverListDirective)
    app.connect("doctree-resolved", create_hoverlist)
    app.connect("build-finished", delete_hoverlist)
    return {"version": __version__}
