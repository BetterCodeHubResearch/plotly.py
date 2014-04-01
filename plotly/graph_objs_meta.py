"""
graph_objs_meta
============

A module that contains language data for plotly. There is not meant to be
functionality here, only some definitions for use with the graph_objs module.

"""

# TODO: match valid KEY TYPES with valid VALUE TYPES!!

INFO = dict(

    base=dict(
        kind='base',
        doc="""A base class for all objects that style a figure in plotly.

        A PlotlyDict can be instantiated like any dict object. This class
        offers some useful recursive methods that can be used by higher-level
        subclasses and containers so long as all plot objects are instantiated
        as a subclass of PlotlyDict. Each PlotlyDict should be instantiated
        with a `kind` keyword argument. This defines the special _info
        dictionary for the object.

        Any available methods that hold for a dict hold for a PlotlyDict.

        """,
        safe=[],
        valid=[],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    data=dict(
        kind='data',
        doc="""A general data class for plotly.

        This class is meant to hold any type of allowable plotly data.

        """,
        safe=['name',
              'mode',
              'y',
              'x',
              'type',
              'bardir',
              'xaxis',
              'yaxis'],
        valid=['textfont',
               'name',
               'marker',
               'mode',
               'y',
               'x',
               'line',
               'type',
               'error_y',
               'opacity',
               'bardir',
               'showlegend',
               'xaxis',
               'yaxis'],
        descriptors=dict(
            textfont="a Font instance, PlotlyDict(kind='font')",
            name="label for the data, this shows up in legend, etc.",
            marker="a Marker instance, PlotlyDict(kind='marker')",
            mode="style of data, e.g. 'lines+markers'",
            y="the y data",
            x="the x data",
            line="a Line instance, PlotlyDict(kind='line')",
            type="the type of plot this data represents, e.g., 'scatter'",
            error_y="an Error_Y instance, PlotlyDict(kind='error_y')",
            opacity="the degree to which you can see through the plot object",
            bardir="if type is 'bar', bardir describes bar orientation",
            showlegend="toggle whether or not data will show up in legend",
            xaxis="the xaxis this data belongs to, e.g., 'x2'",
            yaxis="the yaxis this data belongs to, e.g., 'y3'"
            ),
        types=dict(
            textfont="dict, PlotlyDict, Font",
            name="str",
            marker="dict, PlotlyDict, Marker",
            mode="str",
            y="int, float, etc.",
            x="int, float, etc.",
            line="dict, PlotlyDict, Line",
            error_y="dict, PlotlyDict, Error_Y",
            type="str",
            opacity="float in [0,1]",
            bardir="str, 'h' or 'v'",
            showlegend="bool",
            xaxis="str",
            yaxis="str"
            ),
        repair_vals=dict(xaxis=['x1', None],
                         yaxis=['y1', None]),
        repair_keys=dict()
    ),

    layout=dict(
        kind='layout',
        doc="""doc for layout.

        ain't it good to ya.

        """,
        safe=['title',
              'width',
              'height',
              'autosize'],
        valid=['title',
               'xaxis',
               'yaxis',
               'legend',
               'width',
               'height',
               'autosize',
               'margin',
               'paper_bgcolor',
               'plot_bgcolor',
               'barmode',
               'bargap',
               'bargroupgap',
               'boxmode',
               'boxgap',
               'boxgroupgap',
               'font',
               'titlefont',
               'dragmode',
               'hovermode',
               'separators',
               'hidesources',
               'showlegend',
               'annotations'],
        types=dict(
            title='blah',
            xaxis='blah',
            yaxis='blah',
            legend='blah',
            width='blah',
            height='blah',
            autosize='blah',
            margin='blah',
            paper_bgcolor='blah',
            plot_bgcolor='blah',
            barmode='blah',
            bargap='blah',
            bargroupgap='blah',
            boxmode='blah',
            boxgap='blah',
            boxgroupgap='blah',
            font='blah',
            titlefont='blah',
            dragmode='blah',
            hovermode='blah',
            separators='blah',
            hidesources='blah',
            showlegend='blah',
            annotations='blah'),
        descriptors=dict(
            title='blah',
            xaxis='blah',
            yaxis='blah',
            legend='blah',
            width='blah',
            height='blah',
            autosize='blah',
            margin='blah',
            paper_bgcolor='blah',
            plot_bgcolor='blah',
            barmode='blah',
            bargap='blah',
            bargroupgap='blah',
            boxmode='blah',
            boxgap='blah',
            boxgroupgap='blah',
            font='blah',
            titlefont='blah',
            dragmode='blah',
            hovermode='blah',
            separators='blah',
            hidesources='blah',
            showlegend='blah',
            annotations='blah'),
        repair_vals=dict(),
        repair_keys=dict(xaxis1='xaxis',
                         yaxis1='yaxis')
    ),

    xaxis=dict(
        kind='xaxis',
        doc="""XAxis doc.

        """,
        safe=['range',
              'type',
              'showticklabels',
              'exponentformat',
              'zeroline',
              'overlaying',
              'domain',
              'position',
              'anchor',
              'title'],
        valid=['range',
               'type',
               'showline',
               'mirror',
               'linecolor',
               'linewidth',
               'tick0',
               'dtick',
               'ticks',
               'ticklen',
               'tickcolor',
               'nticks',
               'showticklabels',
               'tickangle',
               'exponentformat',
               'showexponent',
               'showgrid',
               'gridcolor',
               'gridwidth',
               'autorange',
               'rangemode',
               'autotick',
               'zeroline',
               'zerolinecolor',
               'zerolinewidth',
               'titlefont',
               'tickfont',
               'overlaying',
               'domain',
               'position',
               'anchor',
               'title'],
        types=dict(
            range='blah',
            type='blah',
            showline='blah',
            mirror='blah',
            linecolor='blah',
            linewidth='blah',
            tick0='blah',
            dtick='blah',
            ticks='blah',
            ticklen='blah',
            tickcolor='blah',
            nticks='blah',
            showticklabels='blah',
            tickangle='blah',
            exponentformat='blah',
            showexponent='blah',
            showgrid='blah',
            gridcolor='blah',
            gridwidth='blah',
            autorange='blah',
            autotick='blah',
            zeroline='blah',
            zerolinecolor='blah',
            zerolinewidth='blah',
            titlefont='blah',
            tickfont='blah',
            overlaying='blah',
            domain='blah',
            position='blah',
            anchor='blah',
            title='blah'),
        descriptors=dict(
            range='blah',
            type='blah',
            showline='blah',
            mirror='blah',
            linecolor='blah',
            linewidth='blah',
            tick0='blah',
            dtick='blah',
            ticks='blah',
            ticklen='blah',
            tickcolor='blah',
            nticks='blah',
            showticklabels='blah',
            tickangle='blah',
            exponentformat='blah',
            showexponent='blah',
            showgrid='blah',
            gridcolor='blah',
            gridwidth='blah',
            autorange='blah',
            autotick='blah',
            zeroline='blah',
            zerolinecolor='blah',
            zerolinewidth='blah',
            titlefont='blah',
            tickfont='blah',
            overlaying='blah',
            domain='blah',
            position='blah',
            anchor='blah',
            title='blah'),
        repair_vals=dict(anchor=['y1', 'y']),
        repair_keys=dict()
    ),

    yaxis=dict(
        kind='yaxis',
        doc="""YAxis doc.

        """,
        safe=['range',
              'type',
              'showticklabels',
              'exponentformat',
              'zeroline',
              'overlaying',
              'domain',
              'position',
              'anchor',
              'title'],
        valid=['range',
               'type',
               'showline',
               'mirror',
               'linecolor',
               'linewidth',
               'tick0',
               'dtick',
               'ticks',
               'ticklen',
               'tickcolor',
               'nticks',
               'showticklabels',
               'tickangle',
               'exponentformat',
               'showexponent',
               'showgrid',
               'gridcolor',
               'gridwidth',
               'autorange',
               'rangemode',
               'autotick',
               'zeroline',
               'zerolinecolor',
               'zerolinewidth',
               'titlefont',
               'tickfont',
               'overlaying',
               'domain',
               'position',
               'anchor',
               'title'],
        types=dict(
            range='blah',
            type='blah',
            showline='blah',
            mirror='blah',
            linecolor='blah',
            linewidth='blah',
            tick0='blah',
            dtick='blah',
            ticks='blah',
            ticklen='blah',
            tickcolor='blah',
            nticks='blah',
            showticklabels='blah',
            tickangle='blah',
            exponentformat='blah',
            showexponent='blah',
            showgrid='blah',
            gridcolor='blah',
            gridwidth='blah',
            autorange='blah',
            autotick='blah',
            zeroline='blah',
            zerolinecolor='blah',
            zerolinewidth='blah',
            titlefont='blah',
            tickfont='blah',
            overlaying='blah',
            domain='blah',
            position='blah',
            anchor='blah',
            title='blah'),
        descriptors=dict(
            range='blah',
            type='blah',
            showline='blah',
            mirror='blah',
            linecolor='blah',
            linewidth='blah',
            tick0='blah',
            dtick='blah',
            ticks='blah',
            ticklen='blah',
            tickcolor='blah',
            nticks='blah',
            showticklabels='blah',
            tickangle='blah',
            exponentformat='blah',
            showexponent='blah',
            showgrid='blah',
            gridcolor='blah',
            gridwidth='blah',
            autorange='blah',
            autotick='blah',
            zeroline='blah',
            zerolinecolor='blah',
            zerolinewidth='blah',
            titlefont='blah',
            tickfont='blah',
            overlaying='blah',
            domain='blah',
            position='blah',
            anchor='blah',
            title='blah'),
        repair_vals=dict(anchor=['x1', 'x']),
        repair_keys=dict()
    ),

    marker=dict(
        kind='marker',
        doc="""Marker doc.

        """,
        safe=['symbol',
              'size'],
        valid=['symbol',
               'line',
               'size',
               'color',
               'opacity'],
        types=dict(
            symbol='blah',
            line='blah',
            size='blah',
            color='blah',
            opacity='blah'),
        descriptors=dict(
            symbol='blah',
            line='blah',
            size='blah',
            color='blah',
            opacity='blah'),
        repair_vals=dict(),
        repair_keys=dict()
    ),

    legend=dict(
        kind='legend',
        doc="""Legend doc.

        """,
        safe=['traceorder'],
        valid=['bgcolor',
               'bordercolor',
               'font',
               'traceorder'],
        types=dict(
            bgcolor='blah',
            bordercolor='blah',
            font='blah',
            traceorder='blah'),
        descriptors=dict(
            bgcolor='blah',
            bordercolor='blah',
            font='blah',
            traceorder='blah'),
        repair_vals=dict(),
        repair_keys=dict()
    ),

    line=dict(
        kind='line',
        doc="""Line doc.

        """,
        safe=['dash'],
        valid=['dash',
               'color',
               'width',
               'opacity'],
        types=dict(
            dash='blah',
            color='blah',
            width='blah',
            opacity='blah'),
        descriptors=dict(
            dash='blah',
            color='blah',
            width='blah',
            opacity='blah'),
        repair_vals=dict(),
        repair_keys=dict()
    ),

    margin=dict(
        kind='margin',
        doc="""Margin doc.

        """,
        safe=['l',
               'r',
               'b',
               't',
               'pad'],
        valid=['l',
               'r',
               'b',
               't',
               'pad'],
        types=dict(
            l='blah',
            r='blah',
            b='blah',
            t='blah',
            pad='blah'),
        repair_vals=dict(),
        repair_keys=dict()
    ),

    font=dict(
        kind='font',
        doc="""Font doc.

        """,
        safe=[],
        valid=['color',
               'size',
               'family'],
        types=dict(
            color='blah',
            size='blah',
            family='blah'),
        descriptors=dict(
            color='blah',
            size='blah',
            family='blah'),
        repair_vals=dict(),
        repair_keys=dict()
    ),

    annotation=dict(
        kind='annotation',
        doc="""Annotation doc.

        """,
        safe=['text',
              'xref',
              'yref',
              'showarrow',
              'align',
              'xanchor',
              'yanchor',
              'ay',
              'ax',
              'y',
              'x'],
        valid=['text',
               'bordercolor',
               'borderwidth',
               'borderpad',
               'bgcolor',
               'xref',
               'yref',
               'showarrow',
               'arrowwidth',
               'arrowcolor',
               'arrowhead',
               'arrowsize',
               'tag',
               'font',
               'opacity',
               'align',
               'xanchor',
               'yanchor',
               'ay',
               'ax',
               'y',
               'x'],
        types=dict(
            text='blah',
            bordercolor='blah',
            borderwidth='blah',
            borderpad='blah',
            bgcolor='blah',
            xref='blah',
            yref='blah',
            showarrow='blah',
            arrowwidth='blah',
            arrowcolor='blah',
            arrowhead='blah',
            arrowsize='blah',
            tag='blah',
            font='blah',
            opacity='blah',
            align='blah',
            xanchor='blah',
            yanchor='blah',
            ay='blah',
            ax='blah',
            y='blah',
            x='blah'),
        descriptors=dict(
            text='blah',
            bordercolor='blah',
            borderwidth='blah',
            borderpad='blah',
            bgcolor='blah',
            xref='blah',
            yref='blah',
            showarrow='blah',
            arrowwidth='blah',
            arrowcolor='blah',
            arrowhead='blah',
            arrowsize='blah',
            tag='blah',
            font='blah',
            opacity='blah',
            align='blah',
            xanchor='blah',
            yanchor='blah',
            ay='blah',
            ax='blah',
            y='blah',
            x='blah'),
        repair_vals=dict(xref=['x1', 'x'],
                         yref=['y1', 'y']),
        repair_keys=dict()
    )

)

