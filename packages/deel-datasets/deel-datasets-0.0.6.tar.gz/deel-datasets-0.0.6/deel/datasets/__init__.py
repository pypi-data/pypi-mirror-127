# -*- encoding: utf-8 -*-
import logging
from typing import Any, Optional

import pkg_resources

logger = logging.getLogger(__name__)

from .providers.exceptions import DatasetNotFoundError  # noqa: E402
from .settings import Settings  # noqa: E402


def load(
    dataset: str,
    mode: Optional[str] = None,
    version: str = "latest",
    force_update: bool = False,
    with_info: bool = False,
    settings: Settings = None,
    **kwargs
) -> Any:

    """
    Load the given dataset using the given arguments.

    Args:
        dataset: Dataset to load.
        mode: Mode to use. The `"path"` mode is always available and will
            simply returns the path to the local dataset. Each dataset have its
            own sets of available modes.
        version: Version of the dataset.
        force_update: Force update of the local dataset if possible.
        with_info: Returns information about the dataset alongside the actual
            dataset(s).
        settings: Settings to use to load the dataset.
        **kwargs: Extra arguments for the given dataset and mode.

    Returns:
        The dataset in the format specified by `mode`.

    Raises:
        DatasetNotFoundError: If the `dataset` does not exist.
        ImportError: If the plugin could not be loaded.
    """

    dataset_object = None
    for entry_point in pkg_resources.iter_entry_points("plugins.deel.dataset"):
        if entry_point.name == dataset:
            try:
                dataset_class = entry_point.load()
                dataset_object = dataset_class(version, settings)
                break
            except ImportError as e:
                logger.info("Dataset {} plugin loading failed".format(dataset))
                raise e

    if dataset_object is None:

        # If the module or class is not found, and the mode is not path (or None),
        # we throw:
        if mode is not None and mode != "path":
            raise DatasetNotFoundError(dataset)

        # Default mode is then path:
        if mode is None:
            mode = "path"

            # Warn user, because they might expect something else if 'mode' was not set:
            logger.warning(
                (
                    "Dataset plugin for {} not found. "
                    "Path to the local dataset will be returned."
                ).format(dataset)
            )

        from .dataset import Dataset

        # Otherwize we can use the default dataset class:
        dataset_object = Dataset(dataset, version, settings)

    # If the dataset object is required, we must download it:
    if mode == "dataset":

        # If this is not a volatile dataset:
        if isinstance(dataset_object, Dataset):
            dataset_object.load(mode="path", force_update=force_update, **kwargs)

        return dataset_object

    # Create the dataset object and load:
    return dataset_object.load(
        mode=mode, force_update=force_update, with_info=with_info, **kwargs
    )
