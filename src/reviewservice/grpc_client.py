import grpc
from reviewservice import reviewservice_pb2, reviewservice_pb2_grpc

def run():
    # Create a channel and stub
    with grpc.insecure_channel("localhost:8080") as channel:
        stub = reviewservice_pb2_grpc.ReviewServiceStub(channel)

        # Test AddReview
        review = reviewservice_pb2.Review(
            product_id=123,
            user_id=456,
            rating=5,
            content="This is a gRPC test review!",
            language="en"
        )
        response = stub.AddReview(reviewservice_pb2.AddReviewRequest(review=review))
        print("AddReview Response:", response)

        # Test GetReviews
        get_response = stub.GetReviews(reviewservice_pb2.GetReviewsRequest(product_id=123, language="en"))
        print("GetReviews Response:", get_response)

if __name__ == "__main__":
    run()
