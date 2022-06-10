## Implementation

- User and DB classes are being separate for providing abstraction to database connectivity
- With seaprate DB class the Database can be changed from MongoDb to other DB's
- Implementing the DB class methods for other DB's is easier and without making changes to User class
- Unit testing covers User, DB classes

## Further enhancementss

- Persistent runtime even after logout, so the same execution serves longer
- Converting `runtime` method to class object, can be used as web service object where every connection to the server will return `runtime` instance.
