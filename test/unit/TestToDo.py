# from pprint import pprint
import warnings
import unittest
import boto3
from moto import mock_dynamodb2
import sys
import os
import json
from unittest.mock import Mock


@mock_dynamodb2
def mock_table(self):
    print ('+ Mocking table')
    """Generate a fake table to simulate exceptions in conditionals"""
    from src.todoList import get_table
    from botocore.exceptions import ClientError
    
    self.table = Mock(get_table(self.dynamodb))
    self.dbexception = ClientError({'Error': {'Code': 'MockedException',
    'Message': 'This is a Mock'}}, os.environ['DYNAMODB_TABLE'])
    print ('+ Exception ready')


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    
    def setUp(self):
        print ('---------------------')
        print ('Start: setUp')
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<socket.socket.*>")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="callable is None.*")
        warnings.filterwarnings(
            "ignore",
            category=DeprecationWarning,
            message="Using or importing.*")
        """Create the mock database and table"""
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.is_local = 'true'
        self.uuid = "123e4567-e89b-12d3-a456-426614174000"
        self.text = "Aprender DevOps y Cloud en la UNIR"

        from src.todoList import create_todo_table
        self.table = create_todo_table(self.dynamodb)
        print("TABLE_STATUS: {}".format(self.table.table_status))
        self.dbexception = None
        print ('End: setUp')


    def tearDown(self):
        print ('---------------------')
        print ('Start: tearDown')
        """Delete mock database and table after test is run"""
        try:
            self.table.delete()
            print ('Table deleted succesfully')
        except Exception as ex:  # Don't let it crash if table was mocked
            print(ex)
            
        self.dynamodb = None
        print ('End: tearDown')


    def test_table_exists(self):
        print ('---------------------')
        print ('Start: test_table_exists')
        from src.todoList import get_table
        self.assertTrue(self.table)  # check if we got a result
        
        print('Table name: ' + self.table.name)
        tableName = os.environ['DYNAMODB_TABLE'];
        
        # check if the table name is 'ToDo'
        self.assertIn(tableName, self.table.name)
        tabletest = get_table(self.dynamodb)
        print('Tabletest = {}'.format(tabletest))
        print ('End: test_table_exists')


    # @unittest.mock.patch.dict(os.environ, {"ENDPOINT_OVERRIDE": "MOCKED_ENDPOINT"})
    def test_table_exists_error(self):
            print ('---------------------')
            print ('Start: test_table_exists_error')
            from src.todoList import get_table
            try:
                get_table(None)
            except Exception as ex:
                print(ex)
            print ('End: test_table_exists_error')


    def test_put_todo(self):
        print ('---------------------')
        print ('Start: test_put_todo')
        # Testing file functions
        from src.todoList import put_item
        # Table local
        response = put_item(self.text, self.dynamodb)
        print ('Response put_item:' + str(response))
        self.assertEqual(200, response['statusCode'])
        print ('End: test_put_todo')


    def test_put_todo_error(self):
        print ('---------------------')
        print ('Start: test_put_todo_error')
        # Testing file functions
        from src.todoList import put_item
        # Table mock
        self.assertRaises(Exception, put_item("", self.dynamodb))
        
        # Mocked table to test ClientError exception
        mock_table(self)
        self.table.put_item.side_effect = self.dbexception
        self.assertRaises(Exception, put_item("", self.dynamodb))
        print ('End: test_put_todo_error')


    def test_get_todo(self):
        print ('---------------------')
        print ('Start: test_get_todo')
        from src.todoList import get_item
        from src.todoList import put_item

        # Testing file functions
        # Table mock
        responsePut = put_item(self.text, self.dynamodb)
        print ('Response put_item:' + str(responsePut))
        idItem = json.loads(responsePut['body'])['id']
        print ('Id item:' + idItem)
        self.assertEqual(200, responsePut['statusCode'])
        responseGet = get_item(
                idItem,
                self.dynamodb)
        print ('Response Get:' + str(responseGet))
        self.assertEqual(self.text, responseGet['text'])
        print ('End: test_get_todo')


    def test_get_todo_error(self):
        print ('---------------------')
        print ('Start: test_get_todo_error')
        from src.todoList import get_item
        
        # Mock table to test exception "ClientError"
        mock_table(self)
        self.table.get_item.side_effect = self.dbexception
        self.assertRaises(Exception, get_item('foo', self.dynamodb))
        print ('End: test_get_todo_error')
        

    
    def test_list_todo(self):
        print ('---------------------')
        print ('Start: test_list_todo')
        from src.todoList import put_item
        from src.todoList import get_items

        # Testing file functions
        # Table mock
        put_item(self.text, self.dynamodb)
        result = get_items(self.dynamodb)
        print ('Response GetItems' + str(result))
        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['text'] == self.text)
        print ('End: test_list_todo')


    def test_update_todo(self):
        print ('---------------------')
        print ('Start: test_update_todo')
        from src.todoList import put_item
        from src.todoList import update_item
        from src.todoList import get_item
        updated_text = "Aprender más cosas que DevOps y Cloud en la UNIR"
        # Testing file functions
        # Table mock
        responsePut = put_item(self.text, self.dynamodb)
        print ('Response PutItem' + str(responsePut))
        idItem = json.loads(responsePut['body'])['id']
        print ('Id item:' + idItem)
        result = update_item(idItem, updated_text,
                            "false",
                            self.dynamodb)
        print ('Result Update Item:' + str(result))
        self.assertEqual(result['text'], updated_text)
        print ('End: test_update_todo')


    def test_update_todo_error(self):
        print ('---------------------')
        print ('Start: test_update_todo_error')
        from src.todoList import put_item
        from src.todoList import update_item
        updated_text = "Aprender más cosas que DevOps y Cloud en la UNIR"
        # Testing file functions
        # Table mock
        responsePut = put_item(self.text, self.dynamodb)
        print ('Response PutItem' + str(responsePut))
        self.assertRaises(Exception, update_item(updated_text, "", "false",
                            self.dynamodb))
        self.assertRaises(TypeError, update_item("", self.uuid, "false",
                            self.dynamodb))
        self.assertRaises(Exception, update_item(updated_text, self.uuid, "",
                            self.dynamodb))
        
        # Mock table to test exception "ClientError"
        mock_table(self)
        self.table.update_item.side_effect = self.dbexception
        self.assertRaises(Exception, update_item(updated_text, self.uuid, "",
                            self.dynamodb))

        print ('End: test_update_todo_error')

    def test_delete_todo(self):
        print ('---------------------')
        print ('Start: test_delete_todo')
        from src.todoList import delete_item
        from src.todoList import put_item
        from src.todoList import get_items
        # Testing file functions
        # Table mock
        responsePut = put_item(self.text, self.dynamodb)
        print ('Response PutItem' + str(responsePut))
        idItem = json.loads(responsePut['body'])['id']
        print ('Id item:' + idItem)
        delete_item(idItem, self.dynamodb)
        print ('Item deleted succesfully')
        self.assertTrue(len(get_items(self.dynamodb)) == 0)
        print ('End: test_delete_todo')


    def test_delete_todo_error(self):
        print ('---------------------')
        print ('Start: test_delete_todo_error')
        from src.todoList import delete_item
        # Testing file functions
        self.assertRaises(TypeError, delete_item("", self.dynamodb))
        
        # Mock table to test exception "ClientError"
        mock_table(self)
        self.table.delete_item.side_effect = self.dbexception
        self.assertRaises(Exception, delete_item("", self.dynamodb))
        print ('End: test_delete_todo_error')


if __name__ == '__main__':
    unittest.main()