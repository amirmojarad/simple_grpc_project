# generate python code from protos/party.proto and add them into src directory 
python3 -m grpc_tools.protoc -I./protos --python_out=src --grpc_python_out=src ./protos/party.proto