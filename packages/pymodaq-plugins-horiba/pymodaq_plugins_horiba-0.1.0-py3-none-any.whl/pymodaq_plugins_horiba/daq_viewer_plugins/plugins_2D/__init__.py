import importlib
from pathlib import Path
from pymodaq.daq_utils import daq_utils as utils
logger = utils.set_logger('viewer2D_plugins', add_to_console=False)

for path in Path(__file__).parent.iterdir():
    try:
        if '__init__' not in str(path):
            importlib.import_module('.' + path.stem, __package__)
    except Exception as e:
        logger.warning("{:} plugin couldn't be loaded due to some missing packages or errors: {:}".format(path.stem, str(e)))
        pass


