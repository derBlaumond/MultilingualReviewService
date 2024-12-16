import grpc
from concurrent import futures
from reviewservice import reviewservice_pb2, reviewservice_pb2_grpc
from reviewservice.database import reviews_collection

# gRPC Server implementation
class ReviewServiceServicer(reviewservice_pb2_grpc.ReviewServiceServicer):
    """
    Implements the gRPC service defined in reviewservice.proto.
    """

    # Add Review method
    def AddReview(self, request, context):
        try:
            review_data = {
                "product_id": request.review.product_id,
                "user_id": request.review.user_id,
                "rating": request.review.rating,
                "content": request.review.content,
                "language": request.review.language,
                "translations": {}
            }
            result = reviews_collection.insert_one(review_data)
            review_id = str(result.inserted_id)

            # Response
            return reviewservice_pb2.AddReviewResponse(
                message="Review added successfully",
                id=review_id
            )
        except Exception as e:
            context.set_details(f"Failed to add review: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return reviewservice_pb2.AddReviewResponse()

    # Get Reviews method
    def GetReviews(self, request, context):
        try:
            reviews = reviews_collection.find({"product_id": request.product_id})
            reviews_list = []

            for review in reviews:
                translations = review.get("translations", {})
                reviews_list.append(
                    reviewservice_pb2.Review(
                        id=str(review["_id"]),
                        product_id=review["product_id"],
                        user_id=review["user_id"],
                        rating=review["rating"],
                        content=translations.get(request.language, review["content"]),
                        language=request.language,
                        translations=translations
                    )
                )

            return reviewservice_pb2.GetReviewsResponse(reviews=reviews_list)
        except Exception as e:
            context.set_details(f"Failed to fetch reviews: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return reviewservice_pb2.GetReviewsResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    reviewservice_pb2_grpc.add_ReviewServiceServicer_to_server(ReviewServiceServicer(), server)
    server.add_insecure_port("[::]:8080")
    print("Starting gRPC reviewservice server on port 8080...")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    serve()