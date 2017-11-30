#!/usr/bin/python
import pytest

@pytest.fixture(scope="session")
def log_global_env_facts(f):

    if pytest.config.pluginmanager.hasplugin('junitxml'):
        my_junit = getattr(pytest.config, '_xml', None)

        my_junit.add_global_property('Test_set', 'Ping Tests')


@pytest.mark.usefixtures(log_global_env_facts)
def start_and_prepare_env():
    pass
