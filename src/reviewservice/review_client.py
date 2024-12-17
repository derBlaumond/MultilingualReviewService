import grpc
from reviewservice import demo_pb2, demo_pb2_grpc

def run():
    # Create a channel and stub
    with grpc.insecure_channel("localhost:8080") as channel:
        stub = demo_pb2_grpc.ReviewServiceStub(channel)

        # Test AddReview
        review = demo_pb2.Review(
            product_id=123,
            user_id=456,
            rating=5,
            content="This is a gRPC test review!",
            language="en"
        )
        response = stub.AddReview(demo_pb2.AddReviewRequest(review=review))
        print("AddReview Response:", response)

        # Test GetReviews
        get_response = stub.GetReviews(demo_pb2.GetReviewsRequest(product_id=123, language="en"))
        print("GetReviews Response:", get_response)

if __name__ == "__main__":
    run()
