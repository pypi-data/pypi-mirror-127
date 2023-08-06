"""src/talus_utils/plot.py module."""

import functools

from typing import Any, Callable, Dict, List, Optional, Set, Tuple

import matplotlib.pyplot as plt
import plotly.graph_objects as go

from matplotlib_venn import venn2, venn3
from scipy.special import binom

from .constants import PRIMARY_COLOR, SECONDARY_COLOR


def update_layout(*px_args: str, **px_kwargs: str) -> Callable[..., Any]:
    """Override the layout of a Plotly Figure.

    Parameters
    ----------
    px_args :
        The positional arguments to pass to the Plotly Figure.
    px_kwargs :
        The keyword arguments to pass to the Plotly Figure.

    Returns
    -------
    Callable[..., Any]
        The wrapped function.

    """

    def update_layout_wrap(func: Callable[..., Any]) -> Callable[..., Any]:
        """Override the layout of a Plotly Figure.

        Parameters
        ----------
        func: Callable[..., Any] :
            The input function.

        Returns
        -------
        Callable[..., Any]
            The wrapped function.

        """

        @functools.wraps(func)
        def wrapped_func(*args: Tuple[Any], **kwargs: Dict[str, str]) -> Any:
            return_value = func(*args, **kwargs)
            if type(return_value) == go.Figure:
                return return_value.update_layout(*px_args, **px_kwargs)
            return return_value

        return wrapped_func

    return update_layout_wrap


def venn(
    sets: List[Set[str]],
    labels: Optional[List[str]] = None,
    dim: Tuple[Optional[int], Optional[int]] = (None, None),
    title: Optional[str] = None,
    colors: Tuple[str, str] = (PRIMARY_COLOR, SECONDARY_COLOR),
) -> go.Figure:
    """Create a Venn Diagram Overlap Plot using Matplotlib and Plotly.

    Parameters
    ----------
    sets : List[Set]
        Sets to plot overlap for.
    labels : List[str]
        Label for each set. (Default value = None).
    dim : Tuple[int, int]
        The plot dimensions (width, height). (Default value = (None, None)).
    title : str
        The figure title. (Default value = None).
    colors : Tuple[str
        Color to use for each set in the plot. (Default value = (PRIMARY_COLOR, SECONDARY_COLOR)).

    Returns
    -------
    fig : Figure
        A plotly figure.

    """
    n_sets = len(sets)

    # Choose and create matplotlib venn diagramm
    if n_sets == 2:
        if labels and len(labels) == n_sets:
            venn_diagram = venn2(sets, labels)
        else:
            venn_diagram = venn2(sets)
    elif n_sets == 3:
        if labels and len(labels) == n_sets:
            venn_diagram = venn3(sets, labels)
        else:
            venn_diagram = venn3(sets)
    # Supress output of venn diagramm
    plt.close()

    # Create empty lists to hold shapes and annotations
    shapes = []
    annotations = []

    # Create empty list to make hold of min and max values of set shapes
    x_max = []
    y_max = []
    x_min = []
    y_min = []

    for i in range(0, n_sets):
        # create circle shape for current set
        shape = go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=venn_diagram.centers[i][0] - venn_diagram.radii[i],
            y0=venn_diagram.centers[i][1] - venn_diagram.radii[i],
            x1=venn_diagram.centers[i][0] + venn_diagram.radii[i],
            y1=venn_diagram.centers[i][1] + venn_diagram.radii[i],
            fillcolor=colors[i],
            line_color=colors[i],
            opacity=0.75,
        )

        shapes.append(shape)

        # create set label for current set
        anno_set_label = go.layout.Annotation(
            xref="x",
            yref="y",
            x=venn_diagram.set_labels[i].get_position()[0],
            y=venn_diagram.set_labels[i].get_position()[1],
            text=venn_diagram.set_labels[i].get_text(),
            showarrow=False,
        )

        annotations.append(anno_set_label)

        # get min and max values of current set shape
        x_max.append(venn_diagram.centers[i][0] + venn_diagram.radii[i])
        x_min.append(venn_diagram.centers[i][0] - venn_diagram.radii[i])
        y_max.append(venn_diagram.centers[i][1] + venn_diagram.radii[i])
        y_min.append(venn_diagram.centers[i][1] - venn_diagram.radii[i])

    # determine number of subsets
    n_subsets = sum([binom(n_sets, i + 1) for i in range(0, n_sets)])

    for i in range(0, int(n_subsets)):
        if venn_diagram.subset_labels[i]:
            # create subset label (number of common elements for current subset
            anno_subset_label = go.layout.Annotation(
                xref="x",
                yref="y",
                x=venn_diagram.subset_labels[i].get_position()[0],
                y=venn_diagram.subset_labels[i].get_position()[1],
                text=venn_diagram.subset_labels[i].get_text(),
                showarrow=False,
            )
            annotations.append(anno_subset_label)

    # define off_set for the figure range
    off_set = 0.2

    # get min and max for x and y dimension to set the figure range
    x_max_value = max(x_max) + off_set
    x_min_value = min(x_min) - off_set
    y_max_value = max(y_max) + off_set
    y_min_value = min(y_min) - off_set

    # create plotly figure
    fig = go.Figure()

    # set xaxes range and hide ticks and ticklabels
    fig.update_xaxes(range=[x_min_value, x_max_value], showticklabels=False, ticklen=0)

    # set yaxes range and hide ticks and ticklabels
    fig.update_yaxes(
        range=[y_min_value, y_max_value],
        scaleanchor="x",
        scaleratio=1,
        showticklabels=False,
        ticklen=0,
    )

    # set figure properties and add shapes and annotations
    fig.update_layout(
        plot_bgcolor="white",
        margin=dict(b=0, l=10, pad=0, r=10, t=40),
        width=dim[0],
        height=dim[1],
        shapes=shapes,
        annotations=annotations,
        title=dict(text=title, x=0.5, xanchor="center"),
    )

    return fig
