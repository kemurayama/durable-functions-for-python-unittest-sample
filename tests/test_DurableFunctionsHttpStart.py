# coding:utf-8

import unittest.main as unitmain
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, MagicMock, patch

import azure.functions as func
import azure.durable_functions as df

from DurableFunctionsHttpStart import main

class DurableFunctionsHttpStartTestCase(IsolatedAsyncioTestCase):

    async def test_durablefunctionsorchestrator_trigger(self):
        function_name = 'DurableFunctionsOrchestrator'
        instance_id = 'f86a9f49-ae1c-4c66-a60e-991c4c764fe5'
        starter = MagicMock()

        mock_request = func.HttpRequest(
            method='GET',
            body=None,
            url=f'http://localhost:7071/api/orchestrators{function_name}',
            route_params={'functionName': function_name},
            params={'name': 'Test'}
        )

        mock_response = func.HttpResponse(
            body = None,
            status_code= 200,
            headers={
                "Retry-After": 10
            }
        )
        
        with patch('azure.durable_functions.DurableOrchestrationClient',spec=df.DurableOrchestrationClient) as a_mock:
            a_mock.start_new = AsyncMock()
            a_mock().start_new.return_value = instance_id
            a_mock().create_check_status_response.return_value = mock_response
            response = await main(mock_request, starter)

            print(a_mock.mock_calls)
            self.assertIsNotNone(response.headers["Retry-After"])
            self.assertEqual(10,response.headers["Retry-After"])

if __name__ == "__main__":
    unitmain()