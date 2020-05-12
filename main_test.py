from unittest.mock import Mock

import main


def test_clock_angle():
    main.app.testing = True
    client = main.app.test.test_client()
    
    r = client.get('/calcAngle?hour=3&minute=45')
    assert r.status_code == 200
    assert '157' in r.data.decode('utf-8')
