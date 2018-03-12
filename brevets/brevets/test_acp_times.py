import nose
import acp_times as acp
start_time = "2017-01-01T00:00:00+00:00"

#OPEN_TESTS
def test_open_time():
	assert acp.open_time(100,300,start_time) == "2017-01-01T02:56:00+00:00"

	assert acp.open_time(250,300,start_time) == "2017-01-01T07:27:00+00:00"

#CLOSE_TESTS
def test_close_time():
	assert acp.close_time(100,200,start_time) == "2017-01-01T06:40:00+00:00"

	assert acp.close_time(600,600,start_time) == "2017-01-03T16:00:00+00:00"

#INVALID_INPUT
def test_negative():
	assert acp.close_time(-100,200,start_time) == "2017-01-01T00:00:00+00:00"

def test_largeControle():
	assert acp.close_time(300,200,start_time) == "2017-01-01T00:00:00+00:00"

def test_zero():
	assert acp.close_time(0,200,start_time) == "2017-01-01T01:00:00+00:00"
