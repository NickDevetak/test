My test


DATABASE_URL='postgresql://localhost/cucumber'

APP_SETTINGS='config.StagingConfig'

python app.py

scenario_times = {}
scenario_times = Hash.new()
scenario_times['results'] = Array.new()

Around() do |scenario, block|
  start = Time.now
  block.call
  #scenario_times["#{scenario.feature.file}::#{scenario.name}"] = Time.now - start
  run_time = Time.now - start
  scenario_times['results'] << { "feature" => "#{scenario.feature.file}", "run_time" => "#{run_time}"}
end

at_exit do
  uri = URI.parse("http://127.0.0.1:5000")
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Post.new('/upload',  initheader = {'Content-Type' =>'application/json'})
  request.body = scenario_times.to_json
  response = http.request(request)
  puts response.body
end

python manage.py db migrate

python manage.py db upgrade


heroku run python manage.py db upgrade --app shrouded-springs-5349
