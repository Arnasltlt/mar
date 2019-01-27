require 'json'
require 'airtable'
require 'active_support/all'
# require 'active_support/all'

# Pass in api key to client
@client = Airtable::Client.new("keylBaAiyLHi0fD6a")

# Pass in the app key and table name

@table = @client.table("appcYcJWTWr6eedym", "produktai_en")
@records = @table.records

# Change the filename here below but make sure it's in the _data folder.
File.open("_data/produktai_en.json", "w") do |f|
    data = @records.map { |record| record.attributes }
    f.write(data.to_json)
end
