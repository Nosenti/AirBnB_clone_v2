import MySQLdb
import unittest


class TestDatabaseOperations(unittest.TestCase):
    def test_add_state(self):
        # Setup: connect to the database and get initial count
        db = MySQLdb.connect(user='hbnb_test',
                             passwd='hbnb_test_pwd', db='hbnb_test_db')
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Action: simulate adding a new state
        cursor.execute("INSERT INTO states (name) VALUES ('California')")
        db.commit()

        # Test: check the number of states after insertion
        cursor.execute("SELECT COUNT(*) FROM states")
        new_count = cursor.fetchone()[0]
        self.assertEqual(new_count, initial_count + 1)

        # Cleanup: remove the added state (optional)
        cursor.execute("DELETE FROM states WHERE name='California'")
        db.commit()
        cursor.close()
        db.close()


if __name__ == '__main__':
    unittest.main()
