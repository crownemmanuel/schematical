import os
import schematical
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        schematical.app.config['TESTING'] = True
        self.app = schematical.app.test_client()

    def test_new_update(self):
        """Test that a non-registered user can send an update
           with status and location and it is registered in the system.
        """
        # Set up the variables used in the update
        condition = "HURT"
        location = "WorldBank,MC202"
        user = "+12024928443"

        # Create the mesage to be sent based on the defined format.
        sample_update = "!%s @%s" % (condition, location)

        # Send the update to the application using HTTP POST
        rv = self.app.post('/updates', data = {'user': user,
                                              'msg': sample_update} )

        # Verify the object is successfully saved but looking for the 201 status code.
        msg = "Expected the status to be '%s' but got '%s'" % (201, rv.status_code)
        assert 201 == rv.status_code, msg

        # Check the new entry appears in the list of updates.
        received = self.app.get('/updates')

        # Verify that the user, condition and location for the last update
        # is present in the list of updates.
        for attribute in [user, condition, location]:
            msg = "Expected '%s' to be in the received data: '%s'" % (attribute, received.data)
            assert attribute in received.data, msg

 
if __name__ == '__main__':
    unittest.main()
