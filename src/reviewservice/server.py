import grpc
import asyncio
from concurrent import futures
import demo_pb2, demo_pb2_grpc
from database import reviews_collection    #reviewservice.database -> .database -> database

# gRPC Server implementation
class ReviewServiceServicer(demo_pb2_grpc.ReviewServiceServicer):
    """
    Implements the gRPC service defined in reviewservice.proto.
    """

    # Submit Review method
    def SubmitReview(self, request, context):
        
        try:
            
            review_data = {
                "product_id": request.review.productId,
                "user_id": request.review.user_id,
                "rating": request.review.rating,
                "content": request.review.comment,
                #"language": request.review.language,
                #"translations": {}
            }
            result = reviews_collection.insert_one(review_data)
            review_id = str(result.inserted_id)

            # Response
            return demo_pb2.SubmitReviewResponse(
                message="Review added successfully",
                id=review_id
            )
        except Exception as e:
            context.set_details(f"Failed to add review: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return demo_pb2.SubmitReviewResponse()

    # Get Reviews method
    async def GetReviews(self, request, context):
        try:

            reviews = await asyncio.wait_for(reviews_collection.find({"product_id": request.product_id}), timeout=10)
            # reviews_list = []

            # for review in reviews:
            #     #translations = review.get("translations", {})
            #     reviews_list.append(
            #         demo_pb2.Review(
            #             id=str(review["_id"]),
            #             product_id=review["product_id"],
            #             user_id=review["user_id"],
            #             rating=review["rating"],
            #             content=review["content"] #translations.get(request.language, review["content"]),
            #             #language=request.language,
            #             #translations=translations
            #         )
            #     )

            return demo_pb2.GetReviewsResponse(reviews) # reviews=reviews_list
        except asyncio.TimeoutError:
            return []
        except Exception as e:
            context.set_details(f"Failed to fetch reviews: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return demo_pb2.GetReviewsResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    demo_pb2_grpc.add_ReviewServiceServicer_to_server(ReviewServiceServicer(), server)
    server.add_insecure_port("[::]:8080")
    print("Starting gRPC reviewservice server on port 8080...")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    serve()