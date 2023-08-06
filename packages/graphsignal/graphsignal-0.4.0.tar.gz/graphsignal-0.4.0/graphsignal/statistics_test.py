import time
import unittest
import logging
from unittest.mock import patch, Mock
import sys
import numpy as np
import pandas as pd
import pprint
from google.protobuf.json_format import MessageToDict

import graphsignal
from graphsignal import statistics
from graphsignal.windows import *
from graphsignal import metrics_pb2

logger = logging.getLogger('graphsignal')


class StatisticsTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(api_key='k1', debug_mode=True)

    def tearDown(self):
        graphsignal.shutdown()

    def test_data_size(self):
        self.assertEqual(statistics.estimate_size([[1], [2]]), 2)
        self.assertEqual(statistics.estimate_size(np.array([[1], [2]])), 2)
        self.assertEqual(statistics.estimate_size(
            {'a': [1, 2, 3], 'b': [4, 5, 6]}), 3)
        self.assertEqual(statistics.estimate_size(
            {'a': np.asarray([1, 2, 3]), 'b': np.asarray([4, 5, 6])}), 3)
        self.assertEqual(
            statistics.estimate_size(
                pd.DataFrame(
                    data=[
                        [1],
                        [2]])),
            2)

    def test_convert_to_numpy_dict_of_lists(self):
        d1 = {'c1': [1, 2], 'c2': [3.1, 4.1]}
        d2 = {'c1': [3], 'c2': [5.1]}
        columns, data = statistics._convert_to_numpy([d1, d2])
        self.assertIsNotNone(data)
        self.assertEqual(columns, ['c1', 'c2'])
        self.assertTrue(np.array_equal(
            data[0], np.asarray([1, 2, 3])))
        self.assertTrue(np.array_equal(
            data[1], np.asarray([3.1, 4.1, 5.1])))
        self.assertEqual(data[0].dtype, 'int64')
        self.assertEqual(data[1].dtype, 'float64')

    def test_convert_to_numpy_list_of_list(self):
        d1 = [[1, 2], [3.1, 4.1]]
        d2 = [[3, 4], [5.1, 6.1]]
        columns, data = statistics._convert_to_numpy(
            [d1, d2], columns=['A', 'B'])
        self.assertIsNotNone(data)
        self.assertEqual(columns, ['A', 'B'])
        self.assertTrue(np.array_equal(
            data[0], np.asarray([1, 3.1, 3, 5.1])))
        self.assertTrue(np.array_equal(
            data[1], np.asarray([2, 4.1, 4, 6.1])))

    def test_convert_to_numpy_dataframe_with_columns(self):
        d1 = pd.DataFrame(data={'c1': [1, 2], 'c2': [3.1, 4.1]})
        d2 = pd.DataFrame(data={'c1': [3], 'c2': [5.1]})
        columns, data = statistics._convert_to_numpy([d1, d2])
        self.assertIsNotNone(data)
        self.assertEqual(columns, ['c1', 'c2'])
        self.assertTrue(np.array_equal(
            data[0], np.asarray([1, 2, 3])))
        self.assertTrue(np.array_equal(
            data[1], np.asarray([3.1, 4.1, 5.1])))
        self.assertEqual(data[0].dtype, 'int64')
        self.assertEqual(data[1].dtype, 'float64')

    def test_convert_to_numpy_dataframe_wo_columns(self):
        d = pd.DataFrame(data=[[1, 3.1], [2, 4.1]])
        columns, data = statistics._convert_to_numpy([d])
        self.assertIsNotNone(data)
        self.assertEqual(columns, ['0', '1'])
        self.assertTrue(np.array_equal(
            data[0], np.asarray([1, 2])))
        self.assertTrue(np.array_equal(
            data[1], np.asarray([3.1, 4.1])))

    def test_convert_to_numpy_ndarray(self):
        d1 = np.asarray([[1, 3.1], [2, 4.1]])
        d2 = np.asarray([[8, 12]])
        columns, data = statistics._convert_to_numpy([d1, d2])
        self.assertIsNotNone(data)
        self.assertEqual(columns, ['0', '1'])
        self.assertTrue(np.array_equal(
            data[0], np.asarray([1, 2, 8])))
        self.assertTrue(np.array_equal(
            data[1], np.asarray([3.1, 4.1, 12])))
        self.assertEqual(data[0].dtype, 'float64')
        self.assertEqual(data[1].dtype, 'float64')

    def test_update_data_metrics_empty(self):
        window = metrics_pb2.MetricWindow()
        statistics.update_data_metrics({}, window, [])

        self.assertEqual(len(window.data_streams[str(
            metrics_pb2.DataStream.DataSource.INPUT_FEATURES)].metrics), 0)
        self.assertEqual(len(window.data_streams[str(
            metrics_pb2.DataStream.DataSource.OUTPUTS)].metrics), 0)

    def test_update_data_metrics(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        features = {
            'f1': [1, 1, 2, 0],
            'f2': [3.5, 4.5, 5.5, 0],
            'f3': ['a', 'b', 'c', 'c'],
            'f4': [0, float('nan'), float('inf'), 2],
            'f5': [True, True, False, None]}
        outputs = [[0.1], [0.2], [0.1], [0.4]]

        statistics.update_data_metrics(
            metric_updaters, window, [
                PredictionRecord(
                    features=features, outputs=outputs)])

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        window_dict = MessageToDict(window)

        input_metrics_json = window_dict['dataStreams'][str(
            metrics_pb2.DataStream.DataSource.INPUT_FEATURES)]['metrics']
        output_metrics_json = window_dict['dataStreams'][str(
            metrics_pb2.DataStream.DataSource.OUTPUTS)]['metrics']

        for metric in input_metrics_json.values():
            if 'distributionValue' in metric:
                del metric['distributionValue']['sketchKll10']

        for metric in output_metrics_json.values():
            if 'distributionValue' in metric:
                del metric['distributionValue']['sketchKll10']

        #pp = pprint.PrettyPrinter()
        # pp.pprint(input_metrics_json)
        # pp.pprint(output_metrics_json)

        self.assertEqual(input_metrics_json,
                         {'02ada935d60a': {'dimensions': {'feature_name': 'f5'},
                                           'distributionValue': {'sketchImpl': 'KLL10'},
                                           'name': 'distribution',
                                           'type': 'DISTRIBUTION'},
                             '076aa29f76cf': {'dimensions': {'feature_name': 'f4'},
                                              'name': 'integer_values',
                                              'ratioValue': {'counter': 2.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '222d0b1dfa42': {'dimensions': {'feature_name': 'f2'},
                                              'name': 'missing_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             '23777f8d6c5b': {'dimensions': {'feature_name': 'f3'},
                                              'name': 'string_values',
                                              'ratioValue': {'counter': 4.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '2df60f25840a': {'dimensions': {'feature_name': 'f3'},
                                              'distributionValue': {'sketchImpl': 'KLL10'},
                                              'name': 'distribution',
                                              'type': 'DISTRIBUTION'},
                             '31cdc4047da9': {'dimensions': {'feature_name': 'f5'},
                                              'name': 'missing_values',
                                              'ratioValue': {'counter': 1.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '342246abc789': {'dimensions': {'feature_name': 'f1'},
                                              'name': 'missing_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             '38b5e7971c3f': {'dimensions': {'feature_name': 'f1'},
                                              'distributionValue': {'sketchImpl': 'KLL10'},
                                              'name': 'distribution',
                                              'type': 'DISTRIBUTION'},
                             '3aa8ce8a745e': {'counterValue': {'counter': 4.0},
                                              'name': 'instance_count',
                                              'type': 'COUNTER'},
                             '4283d6f1fd2b': {'dimensions': {'feature_name': 'f5'},
                                              'name': 'boolean_values',
                                              'ratioValue': {'counter': 3.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '4a9116752484': {'dimensions': {'feature_name': 'f4'},
                                              'name': 'float_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             '5f5ec237ea4f': {'dimensions': {'feature_name': 'f1'},
                                              'name': 'integer_values',
                                              'ratioValue': {'counter': 4.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '62480aeb7da2': {'dimensions': {'feature_name': 'f1'},
                                              'name': 'float_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             '6add4609813c': {'gaugeValue': {'gauge': 5.0},
                                              'name': 'column_count',
                                              'type': 'GAUGE'},
                             '709339fc41ee': {'dimensions': {'feature_name': 'f1'},
                                              'name': 'zero_values',
                                              'ratioValue': {'counter': 1.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '72dc8927bd35': {'dimensions': {'feature_name': 'f2'},
                                              'name': 'zero_values',
                                              'ratioValue': {'counter': 1.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             '8bcee9cf32e3': {'dimensions': {'feature_name': 'f4'},
                                              'distributionValue': {'sketchImpl': 'KLL10'},
                                              'name': 'distribution',
                                              'type': 'DISTRIBUTION'},
                             'c236202ee147': {'dimensions': {'feature_name': 'f4'},
                                              'name': 'zero_values',
                                              'ratioValue': {'counter': 1.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             'd00eadf9e4cf': {'dimensions': {'feature_name': 'f2'},
                                              'name': 'integer_values',
                                              'ratioValue': {'counter': 1.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             'd082b0be0bf4': {'dimensions': {'feature_name': 'f3'},
                                              'name': 'missing_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             'df1ea8f7032a': {'dimensions': {'feature_name': 'f4'},
                                              'name': 'missing_values',
                                              'ratioValue': {'counter': 2.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             'e2844d940cc2': {'dimensions': {'feature_name': 'f2'},
                                              'name': 'float_values',
                                              'ratioValue': {'counter': 3.0, 'total': 4.0},
                                              'type': 'RATIO'},
                             'e675c4eab4f7': {'dimensions': {'feature_name': 'f3'},
                                              'name': 'empty_values',
                                              'ratioValue': {'total': 4.0},
                                              'type': 'RATIO'},
                             'f1d8c84f680a': {'dimensions': {'feature_name': 'f2'},
                                              'distributionValue': {'sketchImpl': 'KLL10'},
                                              'name': 'distribution',
                                              'type': 'DISTRIBUTION'}})
        self.assertEqual(output_metrics_json,
                         {'094ce9a486c0': {'gaugeValue': {'gauge': 1.0},
                                           'name': 'column_count',
                                           'type': 'GAUGE'},
                          '15f3585b5a2b': {'dimensions': {'output_name': '0'},
                                           'name': 'missing_values',
                                           'ratioValue': {'total': 4.0},
                                           'type': 'RATIO'},
                          '2d4c320b727b': {'dimensions': {'output_name': '0'},
                                           'name': 'integer_values',
                                           'ratioValue': {'total': 4.0},
                                           'type': 'RATIO'},
                          '350dc33d58cf': {'dimensions': {'output_name': '0'},
                                           'name': 'zero_values',
                                           'ratioValue': {'total': 4.0},
                                           'type': 'RATIO'},
                          '3dea0616b753': {'dimensions': {'output_name': '0'},
                                           'name': 'float_values',
                                           'ratioValue': {'counter': 4.0, 'total': 4.0},
                                           'type': 'RATIO'},
                          '59abb90a51e4': {'dimensions': {'output_name': '0'},
                                           'distributionValue': {'sketchImpl': 'KLL10'},
                                           'name': 'distribution',
                                           'type': 'DISTRIBUTION'},
                          '8e1bc8013472': {'counterValue': {'counter': 4.0},
                                           'name': 'instance_count',
                                           'type': 'COUNTER'}})

    def test_update_data_metrics_perf(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        prediction_buffer = []
        for i in range(100):
            features = {}
            for j in range(50):
                features['f1_' + str(j)] = [i]
                features['f2_' + str(j)] = [i + 3.53242342]
                features['f3_' + str(j)] = [100 * 'abc' + str(i)]
                features['f4_' + str(j)] = [float('nan')]
                features['f4_' + str(j)] = [float('+inf')]
            outputs = [[0.1], [0.2], [0.1], [0.4]]
            prediction_buffer.append(
                PredictionRecord(
                    features=features,
                    outputs=outputs))

        #import cProfile
        #from pstats import Stats, SortKey

        start_ts = time.time()

        # with cProfile.Profile() as pr:
        for k in range(10):
            statistics.update_data_metrics(
                metric_updaters, window, prediction_buffer)
        #stats = Stats(pr)
        # stats.sort_stats(SortKey.CUMULATIVE).print_stats(25)

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        took = time.time() - start_ts

        print('update_data_metrics took (sec): ', round(took, 6))
        self.assertTrue(len(window.data_streams[str(
            metrics_pb2.DataStream.DataSource.INPUT_FEATURES)].metrics) > 0)
        self.assertTrue(len(window.data_streams[str(
            metrics_pb2.DataStream.DataSource.OUTPUTS)].metrics) > 0)
        self.assertTrue(took < 1)

    def test_truncate_strings(self):
        truncated = statistics._truncate_strings(
            ['abc', '1234567890abcdefgh', '1234567890abcdefghi'])
        self.assertEqual(
            truncated, [
                'abc', '1234567890abcdefgh', '1234567890...efghi'])

    def test_update_performance_metrics_binary(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        evaluation_buffer = [
            EvaluationRecord(
                label=True,
                prediction=True,
                segments=[
                    's1',
                    's2']),
            EvaluationRecord(
                label=True,
                prediction=True,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=True,
                prediction=False,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=False,
                prediction=True,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=False,
                prediction=False,
                segments=[
                    's1',
                    's2'])
        ]

        statistics.update_performance_metrics(
            metric_updaters, window, evaluation_buffer)

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        window_dict = MessageToDict(window)
        metrics_json = window_dict['dataStreams'][str(
            metrics_pb2.DataStream.DataSource.EVALUATION_BINARY)]['metrics']

        #pp = pprint.PrettyPrinter()
        # pp.pprint(metrics_json)

        self.assertEqual(metrics_json, {'2a8a320fc710': {'name': 'accuracy',
                                                         'ratioValue': {'counter': 3.0, 'total': 5.0},
                                                         'type': 'RATIO'},
                                        '2a915536a163': {'counterValue': {'counter': 1.0},
                                                         'name': 'binary_false_positives',
                                                         'type': 'COUNTER'},
                                        '3e98594499f3': {'counterValue': {'counter': 1.0},
                                                         'name': 'binary_false_negatives',
                                                         'type': 'COUNTER'},
                                        '4769fae29cea': {'counterValue': {'counter': 1.0},
                                                         'name': 'binary_true_negatives',
                                                         'type': 'COUNTER'},
                                        'a335baad03d4': {'distributionValue': {'sketchImpl': 'KLL10',
                                                                               'sketchKll10': {'H': '1',
                                                                                               'c': 0.6666666666666666,
                                                                                               'compactorsString': [{'items': ['s1',
                                                                                                                               's2',
                                                                                                                               's1',
                                                                                                                               's3',
                                                                                                                               's1',
                                                                                                                               's2']}],
                                                                                               'itemType': 'STRING',
                                                                                               'k': '10',
                                                                                               'maxSize': '11',
                                                                                               'size': '6'}},
                                                         'name': 'segment_matches',
                                                         'type': 'DISTRIBUTION'},
                                        'e98d593706c6': {'distributionValue': {'sketchImpl': 'KLL10',
                                                                               'sketchKll10': {'H': '1',
                                                                                               'c': 0.6666666666666666,
                                                                                               'compactorsString': [{'items': ['s1',
                                                                                                                               's2',
                                                                                                                               's1',
                                                                                                                               's3',
                                                                                                                               's1',
                                                                                                                               's3',
                                                                                                                               's1',
                                                                                                                               's3',
                                                                                                                               's1',
                                                                                                                               's2']}],
                                                                                               'itemType': 'STRING',
                                                                                               'k': '10',
                                                                                               'maxSize': '11',
                                                                                               'size': '10'}},
                                                         'name': 'segment_totals',
                                                         'type': 'DISTRIBUTION'},
                                        'ee427ea584e7': {'counterValue': {'counter': 2.0},
                                                         'name': 'binary_true_positives',
                                                         'type': 'COUNTER'}})

    def test_update_performance_metrics_categorical(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        evaluation_buffer = [
            EvaluationRecord(
                label='c1',
                prediction='c1',
                segments=[
                    's1',
                    's2']),
            EvaluationRecord(
                label='c1',
                prediction='c1',
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label='c1',
                prediction='c2',
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label='c1',
                prediction='c2',
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label='c2',
                prediction='c1',
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label='c2',
                prediction='c2',
                segments=[
                    's1',
                    's2']),
            EvaluationRecord(
                label='c3',
                prediction='c3',
                segments=[
                    's1',
                    's2']),
        ]

        statistics.update_performance_metrics(
            metric_updaters, window, evaluation_buffer)

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        window_dict = MessageToDict(window)
        metrics_json = window_dict['dataStreams'][str(
            metrics_pb2.DataStream.DataSource.EVALUATION_CATEGORICAL)]['metrics']

        data_stream = window.data_streams[str(
            metrics_pb2.DataStream.DataSource.EVALUATION_CATEGORICAL)]

        total = None
        sketches = {}
        for metric in data_stream.metrics.values():
            if metric.name == 'total':
                total = metric.counter_value.counter
            elif metric.name == 'class_true_positives':
                sketches['class_true_positives'] = KLLSketch()
                sketches['class_true_positives'].from_proto(
                    metric.distribution_value.sketch_kll10)
            elif metric.name == 'class_false_positives':
                sketches['class_false_positives'] = KLLSketch()
                sketches['class_false_positives'].from_proto(
                    metric.distribution_value.sketch_kll10)
            elif metric.name == 'class_false_negatives':
                sketches['class_false_negatives'] = KLLSketch()
                sketches['class_false_negatives'].from_proto(
                    metric.distribution_value.sketch_kll10)

        # c1 2f22765d
        # c2 6b1f5330
        # c3 a625406f
        self.assertEqual(total, 7.0)
        self.assertEqual(sketches['class_true_positives'].distribution(),
                         [['2f22765d', 2], ['6b1f5330', 1], ['a625406f', 1]])
        self.assertEqual(sketches['class_false_positives'].distribution(),
                         [['2f22765d', 1], ['6b1f5330', 2]])
        self.assertEqual(sketches['class_false_negatives'].distribution(),
                         [['2f22765d', 2], ['6b1f5330', 1]])

    def test_update_performance_metrics_numeric(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        evaluation_buffer = [
            EvaluationRecord(
                label=1.0,
                prediction=3.4,
                segments=[
                    's1',
                    's2']),
            EvaluationRecord(
                label=2.4,
                prediction=0.2,
                segments=[
                    's1',
                    's3'])
        ]

        statistics.update_performance_metrics(
            metric_updaters, window, evaluation_buffer)

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        window_dict = MessageToDict(window)
        metrics_json = window_dict['dataStreams'][str(
            metrics_pb2.DataStream.DataSource.EVALUATION_NUMERIC)]['metrics']

        #pp = pprint.PrettyPrinter()
        # pp.pprint(metrics_json)

        self.assertEqual(metrics_json, {'2789175b4787': {'counterValue': {'counter': 4.6},
                                                         'name': 'mae_sum',
                                                         'type': 'COUNTER'},
                                        '8c82f7b3ed54': {'counterValue': {'counter': 2.0},
                                                         'name': 'mse_n',
                                                         'type': 'COUNTER'},
                                        'fe4a651921fe': {'counterValue': {'counter': 10.599999999999998},
                                                         'name': 'mse_sum',
                                                         'type': 'COUNTER'}})

    def test_update_performance_metrics_segments(self):
        window = metrics_pb2.MetricWindow()
        metric_updaters = {}

        evaluation_buffer = [
            EvaluationRecord(
                label=True,
                prediction=True,
                segments=[
                    's1',
                    's2']),
            EvaluationRecord(
                label=True,
                prediction=True,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=True,
                prediction=False,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=False,
                prediction=True,
                segments=[
                    's1',
                    's3']),
            EvaluationRecord(
                label=False,
                prediction=False,
                segments=[
                    's1',
                    's2'])
        ]

        statistics.update_performance_metrics(
            metric_updaters, window, evaluation_buffer)

        for metric_updater in metric_updaters.values():
            metric_updater.finalize()

        data_stream = window.data_streams[str(
            metrics_pb2.DataStream.DataSource.EVALUATION_BINARY)]

        sketches = {}
        for metric in data_stream.metrics.values():
            if metric.name == 'segment_totals':
                sketches['segment_totals'] = KLLSketch()
                sketches['segment_totals'].from_proto(
                    metric.distribution_value.sketch_kll10)
            elif metric.name == 'segment_matches':
                sketches['segment_matches'] = KLLSketch()
                sketches['segment_matches'].from_proto(
                    metric.distribution_value.sketch_kll10)

        self.assertEqual(sketches['segment_totals'].distribution(),
                         [['s1', 5], ['s2', 2], ['s3', 3]])
        self.assertEqual(sketches['segment_matches'].distribution(), [
                         ['s1', 3], ['s2', 2], ['s3', 1]])
