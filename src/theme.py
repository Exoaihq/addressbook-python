from typing import List
from material_ui.core import create_mui_theme, responsive_font_sizes

primary_colors = {
    "main": "#ec6101",
    "light": "#ff923d",
    "dark": "#b23000"
}

secondary_colors = {
    "main": "#F1B596"
}

font_family: List[str] = ["sans-serif", "Roboto", "Helvetica Neue", "Arial"]

theme = create_mui_theme({
    "palette": {
        "primary": primary_colors,
        "secondary": secondary_colors
    },
    "typography": {
        "fontFamily": ",".join(font_family)
    }
})

theme = responsive_font_sizes(theme)

__all__ = ["theme"]