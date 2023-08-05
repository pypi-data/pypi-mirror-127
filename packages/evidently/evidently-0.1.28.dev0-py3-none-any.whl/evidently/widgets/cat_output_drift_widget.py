#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd

import plotly.graph_objs as go

from evidently.analyzers.cat_target_drift_analyzer import CatTargetDriftAnalyzer
from evidently.model.widget import BaseWidgetInfo, AlertStats
from evidently.widgets.widget import Widget, RED, GREY


class CatOutputDriftWidget(Widget):
    def __init__(self, title: str, kind: str = 'target'):
        super().__init__(title)
        self.kind = kind #target or prediction

    def analyzers(self):
        return [CatTargetDriftAnalyzer]

    def get_info(self) -> BaseWidgetInfo:
        return self.wi

    def calculate(self,
                  reference_data: pd.DataFrame,
                  current_data: pd.DataFrame,
                  column_mapping,
                  analyzers_results):

        results = analyzers_results[CatTargetDriftAnalyzer]

        if results['utility_columns'][self.kind] is None:
            return

        output_name = results['metrics'][self.kind + '_name']
        #output_type = results['metrics'][self.kind + '_type']
        output_p_value = results['metrics'][self.kind + '_drift']
        output_sim_test = "detected" if output_p_value < 0.05 else "not detected"
        #plot output distributions
        fig = go.Figure()

        fig.add_trace(go.Histogram(x=reference_data[output_name],
                marker_color=GREY, opacity=0.6, nbinsx=10,  name='Reference', histnorm='probability'))

        fig.add_trace(go.Histogram(x=current_data[output_name],
                marker_color=RED, opacity=0.6,nbinsx=10, name='Current', histnorm='probability'))

        fig.update_layout(
            legend = dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            ),
            xaxis_title = output_name.title(),
            yaxis_title = "Share"
        )

        output_drift_json  = json.loads(fig.to_json())

        self.wi = BaseWidgetInfo(
            title= self.kind.title() + " drift: ".title() + output_sim_test + ", p_value=" + str(round(output_p_value, 6)),
            type="big_graph",
            details="",
            alertStats=AlertStats(),
            alerts=[],
            alertsPosition="row",
            insights=[],
            size=2,
            params={
                "data": output_drift_json['data'],
                "layout": output_drift_json['layout']
            },
            additionalGraphs=[],
        )
