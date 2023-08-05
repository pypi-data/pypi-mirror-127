#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
import numpy as np

import plotly.graph_objs as go

from evidently.analyzers.regression_performance_analyzer import RegressionPerformanceAnalyzer
from evidently.model.widget import BaseWidgetInfo, AlertStats
from evidently.widgets.widget import Widget


class RegColoredPredActualWidget(Widget):
    def __init__(self, title: str, dataset: str='reference'):
        super().__init__(title)
        self.dataset = dataset #reference or current

    def analyzers(self):
        return [RegressionPerformanceAnalyzer]

    def get_info(self) -> BaseWidgetInfo:
        if self.dataset == 'reference':
            if self.wi:
                return self.wi
            raise ValueError("no data for underperformance predicted vs actual widget provided")
        else:
            return self.wi

    def calculate(self,
                  reference_data: pd.DataFrame,
                  current_data: pd.DataFrame,
                  column_mapping,
                  analyzers_results):

        results = analyzers_results[RegressionPerformanceAnalyzer]

        if results['utility_columns']['target'] is not None and results['utility_columns']['prediction'] is not None:
            if self.dataset == 'current':
                dataset_to_plot = current_data.copy(deep=False) if current_data is not None else None
            else:
                dataset_to_plot = reference_data.copy(deep=False)

            if dataset_to_plot is not None:
                dataset_to_plot.replace([np.inf, -np.inf], np.nan, inplace=True)
                dataset_to_plot.dropna(axis=0, how='any', inplace=True)

                error = dataset_to_plot[results['utility_columns']['prediction']] - dataset_to_plot[results['utility_columns']['target']]

                quantile_5 = np.quantile(error, .05)
                quantile_95 = np.quantile(error, .95)

                dataset_to_plot['Error bias'] = list(map(lambda x : 'Underestimation' if x <= quantile_5 else 'Majority'
                                              if x < quantile_95 else 'Overestimation', error))

                #plot output correlations
                pred_actual = go.Figure()

                pred_actual.add_trace(go.Scatter(
                x = dataset_to_plot[dataset_to_plot['Error bias'] == 'Underestimation'][results['utility_columns']['target']],
                y = dataset_to_plot[dataset_to_plot['Error bias'] == 'Underestimation'][results['utility_columns']['prediction']],
                mode = 'markers',
                name = 'Underestimation',
                marker = dict(
                    color = '#6574f7',
                    showscale = False
                    )
                ))

                pred_actual.add_trace(go.Scatter(
                x = dataset_to_plot[dataset_to_plot['Error bias'] == 'Overestimation'][results['utility_columns']['target']],
                y = dataset_to_plot[dataset_to_plot['Error bias'] == 'Overestimation'][results['utility_columns']['prediction']],
                mode = 'markers',
                name = 'Overestimation',
                marker = dict(
                    color = '#ee5540',
                    showscale = False
                    )
                ))

                pred_actual.add_trace(go.Scatter(
                x = dataset_to_plot[dataset_to_plot['Error bias'] == 'Majority'][results['utility_columns']['target']],
                y = dataset_to_plot[dataset_to_plot['Error bias'] == 'Majority'][results['utility_columns']['prediction']],
                mode = 'markers',
                name = 'Majority',
                marker = dict(
                    color = '#1acc98',
                    showscale = False
                    )
                ))

                pred_actual.update_layout(
                    xaxis_title = "Actual value",
                    yaxis_title = "Predicted value",
                    xaxis = dict(
                        showticklabels=True
                    ),
                    yaxis = dict(
                        showticklabels=True
                    ),
                )

                pred_actual_json  = json.loads(pred_actual.to_json())

                self.wi = BaseWidgetInfo(
                    title=self.title,
                    type="big_graph",
                    details="",
                    alertStats=AlertStats(),
                    alerts=[],
                    alertsPosition="row",
                    insights=[],
                    size=1 if current_data is not None else 2,
                    params={
                        "data": pred_actual_json['data'],
                        "layout": pred_actual_json['layout']
                    },
                    additionalGraphs=[],
                )
            else:
                self.wi = None
        else:
            self.wi = None
