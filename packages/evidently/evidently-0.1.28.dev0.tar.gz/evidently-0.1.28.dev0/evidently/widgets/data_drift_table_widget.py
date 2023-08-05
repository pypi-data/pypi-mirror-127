#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
import numpy as np

import plotly.graph_objs as go

from evidently.analyzers.data_drift_analyzer import DataDriftAnalyzer
from evidently.model.widget import BaseWidgetInfo, AlertStats, AdditionalGraphInfo
from evidently.widgets.widget import Widget, GREY, RED


class DataDriftTableWidget(Widget):
    def analyzers(self):
        return [DataDriftAnalyzer]

    def calculate(self,
                  reference_data: pd.DataFrame,
                  current_data: pd.DataFrame,
                  column_mapping,
                  analyzers_results):
        results = analyzers_results[DataDriftAnalyzer]
        num_feature_names = results["num_feature_names"]
        cat_feature_names = results["cat_feature_names"]

        # set params data
        params_data = []

        confidence = results['utility_columns']['drift_conf_level']
        date_column = results['utility_columns']['date']

        for feature_name in num_feature_names:
            current_small_hist = results['metrics'][feature_name]["current_small_hist"]
            ref_small_hist = results['metrics'][feature_name]["ref_small_hist"]
            feature_type = results['metrics'][feature_name]["feature_type"]

            p_value = results['metrics'][feature_name]["p_value"]

            distr_sim_test = "Detected" if p_value < (1. - confidence) else "Not Detected"

            params_data.append(
                {
                    "details": {
                        "parts": [
                            {
                                "title": "Data drift",
                                "id": feature_name + "_drift",
                                "type": "widget"
                            },
                            {
                                "title": "Data distribution",
                                "id": feature_name + "_distr"
                            }
                        ],
                        "insights": []
                    },
                    "f1": feature_name,
                    "f6": feature_type,
                    "f3": {
                        "x": list(ref_small_hist[1]),
                        "y": list(ref_small_hist[0])
                    },
                    "f4": {
                        "x": list(current_small_hist[1]),
                        "y": list(current_small_hist[0])
                    },
                    "f2": distr_sim_test,
                    "f5": round(p_value, 6)
                }
            )

        for feature_name in cat_feature_names:
            current_small_hist = results['metrics'][feature_name]["current_small_hist"]
            ref_small_hist = results['metrics'][feature_name]["ref_small_hist"]

            feature_type = results['metrics'][feature_name]["feature_type"]

            p_value = results['metrics'][feature_name]["p_value"]

            distr_sim_test = "Detected" if p_value < (1. - confidence) else "Not Detected"

            params_data.append(
                {
                    "details": {
                        "parts": [
                            {
                                "title": "Data drift",
                                "id": feature_name + "_drift",
                                "type": "widget"
                            },
                            {
                                "title": "Data distribution",
                                "id": feature_name + "_distr"
                            }
                        ],
                        "insights": []
                    },
                    "f1": feature_name,
                    "f6": feature_type,
                    "f3": {
                        "x": list(ref_small_hist[1]),
                        "y": list(ref_small_hist[0])
                    },
                    "f4": {
                        "x": list(current_small_hist[1]),
                        "y": list(current_small_hist[0])
                    },
                    "f2": distr_sim_test,
                    "f5": round(p_value, 6)
                }
            )

        # set additionalGraphs
        additional_graphs_data = []
        xbins = results['utility_columns']['xbins']
        nbinsx = results['utility_columns']['nbinsx']
        for feature_name in num_feature_names + cat_feature_names:
            # plot distributions
            fig = go.Figure()
            if xbins:
                current_xbins = results['utility_columns']['xbins'].get(feature_name)
                if current_xbins:
                    current_nbinsx = None
                else:
                    if nbinsx:
                        current_nbinsx = results['utility_columns']['nbinsx'].get(feature_name)
                        current_nbinsx = current_nbinsx if current_nbinsx else 10
                    else:
                        current_nbinsx = 10
                fig.add_trace(go.Histogram(x=reference_data[feature_name],
                           marker_color=GREY, opacity=0.6, xbins=current_xbins, nbinsx=current_nbinsx, name='Reference',
                           histnorm='probability'))

                fig.add_trace(go.Histogram(x=current_data[feature_name],
                                           marker_color=RED, opacity=0.6, xbins=current_xbins, nbinsx=current_nbinsx, name='Current',
                                           histnorm='probability'))
            else:
                current_nbinsx = None
                if nbinsx:
                    current_nbinsx = results['utility_columns']['nbinsx'].get(feature_name)
                current_nbinsx = current_nbinsx if current_nbinsx else 10
                fig.add_trace(go.Histogram(x=reference_data[feature_name],
                                           marker_color=GREY, opacity=0.6, nbinsx=current_nbinsx, name='Reference',
                                           histnorm='probability'))

                fig.add_trace(go.Histogram(x=current_data[feature_name],
                                           marker_color=RED, opacity=0.6, nbinsx=current_nbinsx, name='Current',
                                           histnorm='probability'))

            fig.update_layout(
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                xaxis_title=feature_name,
                yaxis_title="Share"
            )

            distr_figure = json.loads(fig.to_json())

            # plot drift
            reference_mean = np.mean(reference_data[feature_name][np.isfinite(reference_data[feature_name])])
            reference_std = np.std(reference_data[feature_name][np.isfinite(reference_data[feature_name])], ddof=1)
            x_title = "Timestamp" if date_column else "Index"

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=current_data[date_column] if date_column else current_data.index,
                y=current_data[feature_name],
                mode='markers',
                name='Current',
                marker=dict(
                    size=6,
                    color=GREY
                )
            ))

            fig.update_layout(
                xaxis_title=x_title,
                yaxis_title=feature_name,
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                shapes=[
                    dict(
                        type="rect",
                        # x-reference is assigned to the x-values
                        xref="paper",
                        # y-reference is assigned to the plot paper [0,1]
                        yref="y",
                        x0=0,
                        y0=reference_mean - reference_std,
                        x1=1,
                        y1=reference_mean + reference_std,
                        fillcolor="LightGreen",
                        opacity=0.5,
                        layer="below",
                        line_width=0,
                    ),
                    dict(
                        type="line",
                        name='Reference',
                        xref="paper",
                        yref="y",
                        x0=0,  # min(testset_agg_by_date.index),
                        y0=reference_mean,
                        x1=1,  # max(testset_agg_by_date.index),
                        y1=reference_mean,
                        line=dict(
                            color="Green",
                            width=3
                        )
                    ),
                ]
            )

            drift_figure = json.loads(fig.to_json())

            # add distributions data
            additional_graphs_data.append(
                AdditionalGraphInfo(
                    feature_name + '_distr',
                    {
                        "data": distr_figure['data'],
                        "layout": distr_figure['layout']
                    }
                )
            )

            # add drift data
            additional_graphs_data.append(
                AdditionalGraphInfo(
                    feature_name + '_drift',
                    {
                        "title": "",
                        "size": 2,
                        "text": "",
                        "type": "big_graph",
                        "params":
                            {
                                "data": drift_figure['data'],
                                "layout": drift_figure['layout']
                            }
                    }
                )
            )

        n_features = len(num_feature_names) + len(cat_feature_names)
        drift_share = round(100.*results['metrics']['share_drifted_features'], 1)

        title_prefix = 'Drift is detected for ' + str(drift_share) + '% of features (' + str(results['metrics']['n_drifted_features']) +  ' out of ' + str(n_features) + '). '
        title_suffix = 'Dataset Drift is detected.' if results['metrics']['dataset_drift'] else 'Dataset Drift is NOT detected.'

        self.wi = BaseWidgetInfo(
            title=title_prefix + title_suffix,
            type="big_table",
            details="",
            alertStats=AlertStats(),
            alerts=[],
            alertsPosition="row",
            insights=[],
            size=2,
            params={
                "rowsPerPage": min(n_features, 10),
                "columns": [
                    {
                        "title": "Feature",
                        "field": "f1"
                    },
                    {
                        "title": "Type",
                        "field": "f6"
                    },
                    {
                        "title": "Reference Distribution",
                        "field": "f3",
                        "type": "histogram",
                        "options": {
                            "xField": "x",
                            "yField": "y"
                        }
                    },
                    {
                        "title": "Current Distribution",
                        "field": "f4",
                        "type": "histogram",
                        "options": {
                            "xField": "x",
                            "yField": "y"
                        }
                    },
                    {
                        "title": "Data drift",
                        "field": "f2"
                    },
                    {
                        "title": "P-Value for Similarity Test",
                        "field": "f5",
                        "sort": "asc"
                    }
                ],
                "data": params_data
            },

            additionalGraphs=additional_graphs_data
        )
