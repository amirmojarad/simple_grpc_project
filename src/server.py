from concurrent import futures
import grpc
import party_pb2_grpc
import  party_pb2


class Party(party_pb2_grpc.PartyServicer):

    def OpenDoor(self, request, context):
        return party_pb2.OpenReply(open="SERVER ~> Door Opened! for %s" % request.name)

    def Hello(self, request, context):
        return party_pb2.HiWelcomeReply(hi_welcome="SERVER ~> Hi! Welcome! %s" % request.name)


def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        party_pb2_grpc.add_PartyServicer_to_server(Party(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server is Down ZzZzZ")

if __name__ == "__main__":
    serve()