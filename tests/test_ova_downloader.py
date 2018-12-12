import jenkins
import unittest
import requests
from ova_downloader import get_last_build_template_url, download_ova
from unittest.mock import patch
import os


class MockRequests:
    headers = {'content-length': '9'}

    @staticmethod
    def close():
        return

    @staticmethod
    def iter_content(block_size):
        return


class LastBuildUrl(unittest.TestCase):
    @patch.object(jenkins.Jenkins, 'get_job_info')
    def test_get_build(self, mocked_get_job_info):
        result = {'lastSuccessfulBuild': {'url': ''}}
        mocked_get_job_info.return_value = result
        self.assertTrue(get_last_build_template_url)

    @patch.object(jenkins.Jenkins, 'get_job_info')
    def test_key_error_get_build(self, mocked_get_job_info):
        result = {'lastSuccessfulBuild': {}}
        mocked_get_job_info.return_value = result
        with self.assertRaises(KeyError):
            get_last_build_template_url()


class DownloadOva(unittest.TestCase):

    @patch('ova_downloader.tqdm')
    @patch('ova_downloader.get_last_build_template_url')
    @patch('ova_downloader.requests.get')
    def test_fail_to_download_ova(self, mocked_get, mock_last_build, mock_tqdm):
        mock_last_build.return_value = ''
        mocked_get.get.return_value = MockRequests
        cont_length = int(mocked_get.get.return_value.headers.get('content-length'))
        mock_tqdm.return_value = [bytes(str(i), 'utf8') for i in range(cont_length)]
        with self.assertRaises(EnvironmentError):
            download_ova(dir_path=os.getcwd())

    @patch('ova_downloader.get_last_build_template_url')
    @patch('ova_downloader.requests.get')
    def test_env_error(self, mocked_get, mock_last_build):
        mock_last_build.return_value = ''
        mocked_get.get.return_value = MockRequests
        with self.assertRaises(EnvironmentError):
            download_ova(dir_path='{}/folder_not_exist'.format(os.getcwd()))

    @patch('ova_downloader.tqdm')
    @patch('ova_downloader.get_last_build_template_url')
    @patch('ova_downloader.requests.get')
    def test_download_ova_passed(self, mocked_get, mock_last_build, mock_tqdm):
        mock_last_build.return_value = ''
        mocked_get.return_value = MockRequests
        cont_length = int(mocked_get.return_value.headers.get('content-length'))
        mock_tqdm.return_value = (bytes(str(i), 'utf8') for i in range(cont_length))
        self.assertIsNone(download_ova(dir_path=os.getcwd()))


if __name__ == '__main__':
    unittest.main()

