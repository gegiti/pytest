
'''
def test_<name>(<fixture>):
	# Take action
	# Assert the required effect.
'''


def test_testing(create_setup):
	assert False, create_setup


def test_testing2(create_setup):
	assert False, create_setup + "!"


def test_testing3(create_setup):
	assert True, "Not Printed"

