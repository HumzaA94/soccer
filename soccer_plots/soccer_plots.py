import plotly.graph_objs as go


def shape_pseudo(x0, y0, x1, y1, shape_type, line_color):
    shape = dict(
        type=shape_type,
        xref="x",
        yref="y",
        x0=str(x0),
        y0=str(y0),
        x1=str(x1),
        y1=str(y1),
        line=dict(width=2, color=line_color),
    )
    return shape


blue = "blue"
white = "#FFFFFF"


def pitch_pseudo():
    pitch_shapes = []

    end_x = 52.5
    end_y = 34

    center_circle_r = 9.15

    six_yb_w = 18.32
    six_yb_l = 5.5
    eighteen_yb_w = 40.32
    eighteen_yb_l = 16.5

    penalty_distance = 11
    penalty_r = 0.2

    outer_shape = shape_pseudo(-end_x, -end_y, end_x, end_y, "rect", white)

    center_circle_shape = shape_pseudo(
        -center_circle_r,
        -center_circle_r,
        center_circle_r,
        center_circle_r,
        "circle",
        white,
    )
    kickoff_shape = shape_pseudo(
        -penalty_r, -penalty_r, penalty_r, penalty_r, "circle", white
    )
    center_line_shape = shape_pseudo(0, -end_y, 0, end_y, "line", white)

    def_6_yb_shape = shape_pseudo(
        -end_x, -six_yb_w / 2, -end_x + six_yb_l, six_yb_w / 2, "rect", white
    )
    off_6_yb_shape = shape_pseudo(
        end_x, -six_yb_w / 2, end_x - six_yb_l, six_yb_w / 2, "rect", white
    )
    def_18_yb_shape = shape_pseudo(
        -end_x,
        -eighteen_yb_w / 2,
        -end_x + eighteen_yb_l,
        eighteen_yb_w / 2,
        "rect",
        white,
    )
    off_18_yb_shape = shape_pseudo(
        end_x,
        -eighteen_yb_w / 2,
        end_x - eighteen_yb_l,
        eighteen_yb_w / 2,
        "rect",
        white,
    )

    deff_penalty_arc_shape = dict(
        type="path",
        path=f"M -36, -10 Q -32, 0, -36, 10",
        line=dict(width=2, color=white),
    )

    off_penalty_arc_shape = dict(
        type="path",
        path=f"M 36, -10 Q 32, 0, 36, 10",
        line=dict(width=2, color=white),
    )

    def_pen_x0 = -end_x + penalty_distance - penalty_r
    def_pen_x1 = -end_x + penalty_distance + penalty_r
    off_pen_x0 = end_x - penalty_distance - penalty_r
    off_pen_x1 = end_x - penalty_distance + penalty_r

    def_penalty_spot_shape = shape_pseudo(
        def_pen_x0, -penalty_r, def_pen_x1, penalty_r, "circle", white
    )
    off_penalty_spot_shape = shape_pseudo(
        off_pen_x0, -penalty_r, off_pen_x1, penalty_r, "circle", white
    )

    pitch_shapes.append(outer_shape)
    pitch_shapes.append(center_circle_shape)
    pitch_shapes.append(kickoff_shape)
    pitch_shapes.append(center_line_shape)
    pitch_shapes.append(def_6_yb_shape)
    pitch_shapes.append(off_6_yb_shape)
    pitch_shapes.append(def_18_yb_shape)
    pitch_shapes.append(off_18_yb_shape)
    pitch_shapes.append(def_penalty_spot_shape)
    pitch_shapes.append(off_penalty_spot_shape)
    pitch_shapes.append(off_penalty_arc_shape)
    pitch_shapes.append(deff_penalty_arc_shape)

    return pitch_shapes


def draw_pitch_example(graph_title=None):
    layout = go.Layout(
        autosize=True,
        xaxis=dict(
            zeroline=False, showgrid=False, showticklabels=False, range=[-58, 58]
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            range=[-39, 39],
            autorange=False,
        ),
        height=680,
        width=1050,
        bargap=0,
        legend=dict(x=0.75, y=-0.07),
        showlegend=True,
        title=dict(text=graph_title, font=dict(family="Arial", size=18, color="black")),
        shapes=pitch_pseudo(),
        # paper_bgcolor='green',
        plot_bgcolor="green",
    )

    fig = go.Figure(layout=layout)
    return fig
