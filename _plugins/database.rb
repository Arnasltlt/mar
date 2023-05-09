require 'json'
require 'airtable'
require 'active_support/all'
require 'net/http'
require 'uri'
require 'dotenv'

Dotenv.load

# Set your API token
api_token = ENV['AIRTABLE_API_TOKEN']

# Set your base and table IDs
base_id = ENV['BASE_ID']
table_id = ENV['TABLE_ID']

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
File.open("_data/produktai.json", "w") do |f|
  data = records.map { |record| record["fields"] }
  f.write(data.to_json)
end
