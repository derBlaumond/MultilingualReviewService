from concurrent import futures
import grpc
import reviewservice_pb2
import reviewservice_pb2_grpc

class ReviewService(reviewservice_pb2_grpc.ReviewServiceServicer):
    def GetReviews(self, request, context):
        # Replace this mock data with your real database or API logic
        reviews = [
            reviewservice_pb2.Review(author="Alice", text="Great product!"),
            reviewservice_pb2.Review(author="Bob", text="Not bad."),
        ]
        return reviewservice_pb2.GetReviewsResponse(reviews=reviews)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reviewservice_pb2_grpc.add_ReviewServiceServicer_to_server(ReviewService(), server)
    server.add_insecure_port("[::]:8080")
    print("ReviewService is running on port 8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
