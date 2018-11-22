import logging
import shutil

from ats.easypy.plugins.bases import BasePlugin



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CopyReport(BasePlugin):
    def __init__(self, directory, report_directory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._source = directory
        self._dest = report_directory

    def post_job(self, job): 
        logger.info('The directory to copy: {}; destination: {}'.format(self._source, self._dest))
        shutil.copytree(self._source, f'{job.runtime.directory}/{self._dest}')
        print(f'{job.runtime.archive}')
