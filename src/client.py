import time
import grpc
import party_pb2
import party_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = party_pb2_grpc.PartyStub(channel)
        print("Party Started and you have been invited")
        your_name = input("What's your name?\n")
        message = input("Knock Knock The Door!\n")
        if "knock" in message.lower():
            response = stub.OpenDoor(party_pb2.KnockKnockRequest(name=your_name))
            print("Knock Knock... !: ")
            time.sleep(2)
            print(response.open)
        message = input("Say Hello to host!\n")
        if "hello" in message:
            response = stub.Hello(party_pb2.HelloRequest(name=your_name))
            print("Hello Dear!")
            time.sleep(1)
            print(response.hi_welcome)

             

if __name__ == '__main__':
    run()