import quickstats

from .hypotest_inverter_plot import HypoTestInverterPlot
from .abstract_plot import AbstractPlot
from .score_distribution_plot import score_distribution_plot
from .test_statistic_distribution_plot import TestStatisticDistributionPlot
from .upper_limit_1D_plot import UpperLimit1DPlot
from .upper_limit_2D_plot import UpperLimit2DPlot

from matplotlib import style, colors

# Reference from https://github.com/beojan/atlas-mpl

style.core.USER_LIBRARY_PATHS.append(quickstats.stylesheet_path)
style.core.reload_library()
style.use("quick_default")

_EXTRA_COLORS = {
    "paper:bg": "#eeeeee",
    "paper:fg": "#444444",
    "paper:bgAlt": "#e4e4e4",
    "paper:red": "#af0000",
    "paper:green": "#008700",
    "paper:blue": "#005f87",
    "paper:yellow": "#afaf00",
    "paper:orange": "#d75f00",
    "paper:pink": "#d70087",
    "paper:purple": "#8700af",
    "paper:lightBlue": "#0087af",
    "paper:olive": "#5f7800",
    "on:bg": "#1b2b34",
    "on:fg": "#cdd3de",
    "on:bgAlt": "#343d46",
    "on:fgAlt": "#d8dee9",
    "on:red": "#ec5f67",
    "on:orange": "#f99157",
    "on:yellow": "#fac863",
    "on:green": "#99c794",
    "on:cyan": "#5fb3b3",
    "on:blue": "#6699cc",
    "on:pink": "#c594c5",
    "on:brown": "#ab7967",
    "series:cyan": "#54c9d1",
    "series:orange": "#eca89a",
    "series:blue": "#95bced",
    "series:olive": "#ceb776",
    "series:purple": "#d3a9ea",
    "series:green": "#9bc57f",
    "series:pink": "#f0a1ca",
    "series:turquoise": "#5fcbaa",
    "atlas:onesigma": "#00ff26",
    "atlas:twosigma": "#fbff1f",
    "series2:green": "#00ff26",
    "series2:yellow": "#fbff1f",
    "series2:blue": "#00a1e0",
    "series2:red": "#a30013",
    "series2:purple": "#5100c2",
    "hdbs:starcommandblue": "#047cbc",
    "hdbs:spacecadet": "#283044",
    "hdbs:mintcream": "#ebf5ee",
    "hdbs:outrageousorange": "#fa7e61",
    "hdbs:pictorialcarmine": "#ca1551",
    "hdbs:maroonX11": "#b8336a",
    "hh:darkpink": "#f2385a",
    "hh:darkblue": "#343844",
    "hh:medturquoise": "#36b1bf",
    "hh:lightturquoise": "#4ad9d9",
    "hh:offwhite": "#e9f1df",
    "hh:darkyellow": "#fdc536",
    "hh:darkgreen": "#125125",
    "transparent": "#ffffff00",
}

colors.EXTRA_COLORS = _EXTRA_COLORS
colors.colorConverter.colors.update(_EXTRA_COLORS)