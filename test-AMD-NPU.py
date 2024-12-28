# import onnxruntime

# # Add user imports
# # ...

# # Load inputs and perform preprocessing
# # ...

# # Create an inference session using the Vitis AI execution provider
# session = onnxruntime.InferenceSession(
#               '[model_file].onnx',
#                providers=["VitisAIExecutionProvider"],
#                provider_options=[{"config_file":"/path/to/vaip_config.json"}])

# input_shape = session.get_inputs()[0].shape
# input_name = session.get_inputs()[0].name

# # Load inputs and do preprocessing by input_shape
# input_data = [...]
# result = session.run([], {input_name: input_data})


print()