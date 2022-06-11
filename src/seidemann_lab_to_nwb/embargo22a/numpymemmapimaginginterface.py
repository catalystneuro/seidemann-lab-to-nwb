from pydantic import FilePath
from roiextractors import NumpyMemmapImagingExtractor
from roiextractors.extraction_tools import VideoStructure

from nwb_conversion_tools.datainterfaces.ophys.baseimagingextractorinterface import BaseImagingExtractorInterface
from nwb_conversion_tools.utils.types import FilePathType

class NumpyMemmapImagingInterface(BaseImagingExtractorInterface):
    """Data Interface for raw imaging data."""

    IX = NumpyMemmapImagingExtractor

    def __init__(
        self,
        file_path: FilePathType,
        sampling_frequency: float,
        dtype: str,
        rows: int,
        columns: int,
        num_channels: int,
        frame_axis: int,
        rows_axis: int,
        columns_axis: int,
        num_channels_axis: int,
        offset: int = 0,
    ):

        video_structure = VideoStructure(
            rows=rows,
            columns=columns,
            num_channels=num_channels,
            rows_axis=rows_axis,
            columns_axis=columns_axis,
            num_channels_axis=num_channels_axis,
            frame_axis=frame_axis,
        )

        self.imaging_extractor = NumpyMemmapImagingExtractor(
            file_path=file_path,
            video_structure=video_structure,
            sampling_frequency=sampling_frequency,
            dtype=dtype,
            offset=offset,
        )

        self.verbose = True
        self.source_data = dict(
            file_path=file_path,
            sampling_frequency=sampling_frequency,
            dtype=dtype,
            rows=rows,
            columns=columns,
            num_channels=num_channels,
            frame_axis=frame_axis,
            rows_axis=rows_axis,
            columns_axis=columns_axis,
            num_channels_axis=num_channels_axis,
            offset=offset,
        )
