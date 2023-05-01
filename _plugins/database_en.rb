require 'json'
require 'net/http'
require 'uri'
require 'active_support/all'

# Set your API token
api_token = "pata073YBLZzHKMOU.1e0002896f1944d532a3e10e90c008a35d401ecbc56752986f2d7d229ed0d418"

# Set your base and table IDs
base_id = "appcYcJWTWr6eedym"
table_id = "produktai_en"

# Prepare the request
uri = URI.parse("https://api.airtable.com/v0/#{base_id}/#{table_id}")
request = Net::HTTP::Get.new(uri)
request["Authorization"] = "Bearer #{api_token}"
request["Content-Type"] = "application/json"

# Send the request
response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
  http.request(request)
end

# Parse the response
records = JSON.parse(response.body)["records"]

# Save the records to a JSON file
File.open("_data/produktai_en.json", "w") do |f|
  data = records.map { |record| record["fields"] }
  f.write(data.to_json)
end
