import unittest
import logging
from unittest.mock import patch, Mock
import sys
import numpy as np
import time
import pandas as pd

import graphsignal
from graphsignal import metrics_pb2
from graphsignal.windows import *
from graphsignal.sketches.kll import KLLSketch

logger = logging.getLogger('graphsignal')


class WindowsTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(api_key='k1', debug_mode=True)

    def tearDown(self):
        graphsignal.shutdown()

    def test_update_gauge(self):
        window = metrics_pb2.MetricWindow()
        metric_updater = get_metric_updater(
            {}, window.data_streams['1'], 'test')

        metric_updater.update_gauge(1.1)
        metric_updater.update_gauge(1.2)
        self.assertEqual(metric_updater._metric_proto.gauge_value.gauge, 1.2)

    def test_update_counter(self):
        window = metrics_pb2.MetricWindow()
        metric_updater = get_metric_updater(
            {}, window.data_streams['1'], 'test')

        metric_updater.update_counter(4)
        metric_updater.update_counter(2.01)
        self.assertEqual(
            metric_updater._metric_proto.counter_value.counter, 6.01)

    def test_update_ratio(self):
        window = metrics_pb2.MetricWindow()
        metric_updater = get_metric_updater(
            {}, window.data_streams['1'], 'test')

        metric_updater.update_ratio(0, 5)
        metric_updater.update_ratio(1, 30)
        self.assertEqual(
            metric_updater._metric_proto.ratio_value.counter, 1)
        self.assertEqual(
            metric_updater._metric_proto.ratio_value.total, 35)

    def test_update_distribution(self):
        window = metrics_pb2.MetricWindow()
        metric_updater = get_metric_updater(
            {}, window.data_streams['1'], 'test')

        data = [1.1, 1.1, 2, 2, 3, 3, 3, 4.0001, 4.0001]
        metric_updater.update_distribution(data)

        data = [1.1, 5000]
        metric_updater.update_distribution(data)

        metric_updater.finalize()

        self.assertEqual(metric_updater._sketch.count(), 11)

        k2 = KLLSketch()
        k2.from_proto(
            metric_updater._metric_proto.distribution_value.sketch_kll10)
        self.assertEqual(k2.count(), 11)

    def test_canonical_string(self):
        self.assertEqual(
            canonical_string('abc'), 'abc')
        self.assertEqual(
            canonical_string({'b': 2, '0': '0', 'a': 1}),
            '0=0,a=1,b=2')
        self.assertEqual(
            canonical_string([1, 2.3, 'a']),
            '1,2.3,a')
