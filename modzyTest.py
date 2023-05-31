
from modzy import ApiClient
from modzy._util import file_to_bytes
client = ApiClient(base_url="<portal link here>", api_key="<key here>")
sources = {}
#Add any number of inputs
sources["my-input"] = {
    "input": file_to_bytes('sauteed-2-premium-pan-overhead.jpeg'),
}
#Once you are ready, submit the job
job = client.jobs.submit_file("zi2wvziln1", "0.0.2", sources)
print(f"job: {job}")

