import pytest
from unittest.mock import Mock, patch
from app import get_audio_stream

# Mock pytube's Video object and Stream object
class MockStream:
    def get_audio_only(self):
        return "audio_stream"

class MockVideo:
    streams = MockStream()

@pytest.mark.parametrize("progress_value, expected_progress", [
    pytest.param(0, 20, id="progress_starts_at_0"),
    pytest.param(10, 20, id="progress_starts_at_10"),
    pytest.param(50, 20, id="progress_starts_at_50"),
])
def test_get_audio_stream_happy_path(progress_value, expected_progress):
    # Arrange
    video = MockVideo()
    progress_bar = Mock()
    progress_bar.progress = Mock()

    # Act
    audio_stream = get_audio_stream(video, progress_bar)

    # Assert
    assert audio_stream == "audio_stream"
    progress_bar.progress.assert_called_once_with(expected_progress)

@pytest.mark.parametrize("exception, expected_exception", [
    pytest.param(AttributeError, AttributeError, id="attribute_error_on_get_audio_only"),
    pytest.param(RuntimeError, RuntimeError, id="runtime_error_on_get_audio_only"),
])
def test_get_audio_stream_error_cases(exception, expected_exception):
    # Arrange
    video = MockVideo()
    video.streams.get_audio_only.side_effect = exception
    progress_bar = Mock()
    progress_bar.progress = Mock()

    # Act / Assert
    with pytest.raises(expected_exception):
        get_audio_stream(video, progress_bar)
    progress_bar.progress.assert_not_called()
