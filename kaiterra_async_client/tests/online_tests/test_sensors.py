#!/usr/bin/env python3

import os
import aiohttp
import aiounittest
from kaiterra_async_client.tests import skip_online_tests
from kaiterra_async_client import KaiterraAPIClient, Units

def create_client(session):
    if 'KAITERRA_APIV1_URL_KEY' not in os.environ:
        raise Exception('Missing Kaiterra API key in environment variable KAITERRA_APIV1_URL_KEY')
    api_key = os.environ['KAITERRA_APIV1_URL_KEY']

    return KaiterraAPIClient(session, api_key=api_key, preferred_units=[Units.DegreesFahrenheit])

@skip_online_tests
class GetSensorDataTests(aiounittest.AsyncTestCase):
    """
    Tests for retrieving sensor data.
    """

    async def test_simple(self):
        async with aiohttp.ClientSession() as session:
            client = create_client(session)
            readings = await client.get_latest_sensor_readings([
                '/lasereggs/00000000-0001-0001-0000-00007e57c0de',
                '/lasereggs/00000000-ffff-0001-ffff-00007e57c0de',
            ])
            self.assertEqual(2, len(readings))

            # First sensor exists, and should have readings
            self.assertIsNotNone(readings[0])
            self.assertIn('rpm25c', readings[0])
            self.assertIsNone(readings[1])

    async def test_validate_sensor_ids(self):
        async with aiohttp.ClientSession() as session:
            client = create_client(session)
            # Malformed UDID
            with self.assertRaises(ValueError):
                await client.get_latest_sensor_readings(['/lasereggs/0000000-0001-0001-0000-00007e57c0de'])

            # Should be a list, not a string
            with self.assertRaises(ValueError):
                await client.get_latest_sensor_readings('/lasereggs/00000000-0001-0001-0000-00007e57c0de')
