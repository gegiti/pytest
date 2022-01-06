import pytest

'''To run test - python -m py.test'''

@pytest.fixture
def connect(param1):
	# Setup
	yield param1
	# Cleanup


@pytest.fixture
def upload(param2):
	# Setup
	yield param2
	# Cleanup


@pytest.fixture
def create_setup(connect, upload):
	# Setup
	yield connect + " " + upload
	# Cleanup


setups = {
	"v1.0": [
			"Hello",
			"World",
		],
	"v2.1": [
			"Good",
			"Day",
		],
}


def pytest_generate_tests(metafunc):
	if "create_setup" in metafunc.fixturenames:
		argnames = ["param1", "param2"]
		argvalues = [setups[v] for v in setups]
		ids = [v for v in setups]
		metafunc.parametrize(argnames, argvalues, ids=ids)
