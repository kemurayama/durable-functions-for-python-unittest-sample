#coding:utf-8

from unittest import main
from unittest import TestCase
from unittest.mock import patch

import azure.durable_functions as df

from DurableFunctionsOrchestrator import orchestrator_function

# side_effect function for returning various values depending on args.
def hello_side_effect(hello:str, location:str):
    return f'Hello {location}!'
    
class DurableFunctionsOrchestratorTestCase(TestCase):

    def test_orchestrator_function(self):
        
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = hello_side_effect
            result = list(orchestrator_function(mock))

            self.assertEqual(3,len(result))
            self.assertEqual('Hello Tokyo!',result[0])
            self.assertEqual('Hello Seattle!',result[1])
            self.assertEqual('Hello London!',result[2])
            
if __name__ == "__main__":
    main()
            