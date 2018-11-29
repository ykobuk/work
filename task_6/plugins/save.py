import logging
import shutil

from ats.easypy.plugins.bases import BasePlugin


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CopyReport(BasePlugin):
    def __init__(self, directory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._source = None
        self._dest = None

    def post_job(self, job):
        self._source = job.testbed.custom['directory']
        self._dest = job.testbed.custom['report_directory']
        logger.info('The directory to copy: {}; destination: {}'.format(self._source, self._dest))
        shutil.copytree(self._source, '{}/{}'.format(job.runtime.directory, self._dest))
