# MultilingualReviewService

As the Backend Developer for ReviewService, my primary responsibilities are to develop a fully
functional ReviewService API, integrate it with MongoDB, and ensure seamless communication with the
TranslationService.

Tools needed:
FastAPI 
Python
httpx
MongoDB

Guide how to test the reviewservice locally without frontend and translationservice integration.

1)Install MongoDB Compass. To start mongodb server go in command line
C:\Program Files\MongoDB\Server\8.0\bin>
and run the command 
.\mongod --dbpath C:\Users\Mi\Desktop\MongoDB
2)now you can create a connection in MongoDB Compass on localhost:27017
3)to start the script go to the app folder and run
uvicorn src.reviewservice.main:app --reload
4)to run the tests navigate to C:\Users\Mi\Desktop\MultilingualReviewService> and run
pytest src/reviewservice/tests
*tests fail due to no incorrect integration with translationservice. Othervise everything works perfectly.

To test grpc pipelines:

1)Install MongoDB Compass. To start mongodb server go in command line
C:\Program Files\MongoDB\Server\8.0\bin>
and run the command 
.\mongod --dbpath C:\Users\Mi\Desktop\MongoDB
2)now you can create a connection in MongoDB Compass on localhost:27017
3)in the first terminal start the server with the command 
python -m src.reviewservice.grpc_server
4)in the other terminal start the client with the command 
python src/reviewservice/grpc_client.py
5)You will instantly get the post-request result:
AddReview Response: message: "Review added successfully"
id: "676075343e2cae229deb85f8"

and get-request result:
GetReviews Response: reviews {
  id: "676075343e2cae229deb85f8"
  product_id: 123
  user_id: 456
  rating: 5
  content: "This is a gRPC test review!"   
  language: "en"
}

