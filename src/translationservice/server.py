from concurrent import futures
import grpc
import translationservice_pb2
import translationservice_pb2_grpc

class TranslationService(translationservice_pb2_grpc.TranslationServiceServicer):
    def Translate(self, request, context):
        # Replace with actual translation logic (e.g., Google Translate API)
        translated_text = f"{request.text} (translated to {request.target_language})"
        return translationservice_pb2.TranslateResponse(translated_text=translated_text)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    translationservice_pb2_grpc.add_TranslationServiceServicer_to_server(TranslationService(), server)
    server.add_insecure_port("[::]:8080")
    print("TranslationService is running on port 8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
