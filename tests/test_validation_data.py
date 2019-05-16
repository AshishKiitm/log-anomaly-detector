"""Validates if training was successful."""
import pytest
from anomaly_detector.anomaly_detector import AnomalyDetector
from anomaly_detector.config import Configuration

CONFIGURATION_PREFIX = "LAD"


@pytest.fixture()
def detector():
    """Initialize configurations before testing."""
    config = Configuration(CONFIGURATION_PREFIX)
    anomaly_detector = AnomalyDetector(config)
    return anomaly_detector


def test_end2endtraining(detector):
    """Test anomaly detection training on public dataset."""
    assert detector.train() == 0