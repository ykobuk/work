import unittest
from unittest import mock
import paramiko
from unittest.mock import patch

from vaclient import VAClient


class FakeTransport:
    def __init__(self):
        self.active = True
        self.o_session = True

    def is_active(self):
        return self.active

    def open_session(self):
        return self

    def recv(self, lol):
        return 'hello world'


class FakeChannel:

    def __init__(self, closed=True):
        self.closed = closed

    @property
    def channel(self):
        return self

    def recv_exit_status(self):
        return 0

    def readlines(self):
        return 'channel stdout'


class FakeSSHClient:
    def __init__(self):
        self.transport = FakeTransport
        # self.raise_exception = raise_exception
        # self.excaption_name = excaption_name

    def connect(self, *args):
        pass

    def set_missing_host_key_policy(self, policy):
        pass

    def exec_command(self, cmd, get_pty=True):
        return (FakeChannel(),
                FakeChannel(),
                FakeChannel())

    def get_transport(self):
        return FakeTransport()

    def close(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


class TestPar(unittest.TestCase):
    def test_connect_is_created(self):
        with mock.patch.object(paramiko,
                               'SSHClient',
                               mock.Mock(return_value=FakeSSHClient())):

            con = VAClient(ip='192.168.242.22')
            self.assertTrue(con.connect())


if __name__ == '__main__':
    unittest.main()

