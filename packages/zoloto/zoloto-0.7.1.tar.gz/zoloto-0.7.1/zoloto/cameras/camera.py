from pathlib import Path
from typing import Any, Generator, Optional

from cv2 import CAP_PROP_BUFFERSIZE, VideoCapture
from numpy import ndarray

from zoloto.marker_type import MarkerType

from .base import BaseCamera
from .mixins import IterableCameraMixin, VideoCaptureMixin, ViewableCameraMixin


def find_camera_ids() -> Generator[int, None, None]:
    """
    Find and return ids of connected cameras.

    Works the same as VideoCapture(-1).
    """
    for camera_id in range(8):
        capture = VideoCapture(camera_id)
        opened = capture.isOpened()
        capture.release()
        if opened:
            yield camera_id


class Camera(VideoCaptureMixin, IterableCameraMixin, BaseCamera, ViewableCameraMixin):
    def __init__(
        self,
        camera_id: int,
        *,
        marker_size: Optional[int] = None,
        marker_type: MarkerType,
        calibration_file: Optional[Path] = None,
    ) -> None:
        super().__init__(
            marker_size=marker_size,
            marker_type=marker_type,
            calibration_file=calibration_file,
        )
        self.camera_id = camera_id
        self.video_capture = self.get_video_capture(self.camera_id)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.camera_id}>"

    def get_video_capture(self, camera_id: int) -> VideoCapture:
        cap = VideoCapture(camera_id)
        cap.set(CAP_PROP_BUFFERSIZE, 1)
        return cap

    def capture_frame(self) -> ndarray:
        # Hack: Double capture frames to fill buffer.
        self.video_capture.read()
        return super().capture_frame()

    def close(self) -> None:
        super().close()
        self.video_capture.release()

    @classmethod
    def discover(cls, **kwargs: Any) -> Generator["Camera", None, None]:
        for camera_id in find_camera_ids():
            yield cls(camera_id, **kwargs)


class SnapshotCamera(VideoCaptureMixin, BaseCamera):
    """
    A modified version of Camera optimised for single use.

    - Doesn't keep the camera open between captures
    """

    def __init__(
        self,
        camera_id: int,
        *,
        marker_size: Optional[int] = None,
        marker_type: MarkerType,
        calibration_file: Optional[Path] = None,
    ) -> None:
        super().__init__(
            marker_size=marker_size,
            marker_type=marker_type,
            calibration_file=calibration_file,
        )
        self.camera_id = camera_id

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.camera_id}>"

    def get_video_capture(self, camera_id: int) -> VideoCapture:
        return VideoCapture(camera_id)

    def capture_frame(self) -> ndarray:
        self.video_capture = self.get_video_capture(self.camera_id)
        frame = super().capture_frame()
        self.video_capture.release()
        return frame

    @classmethod
    def discover(cls, **kwargs: Any) -> Generator["SnapshotCamera", None, None]:
        for camera_id in find_camera_ids():
            yield cls(camera_id, **kwargs)
