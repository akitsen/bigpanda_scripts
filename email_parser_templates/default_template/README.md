## base_template.json
This is the base template with no additional coverage.

#### Property: `status`
 - `Source`: email subject line
 - `Default Value`: warning 
 - `Status Map`
   - `critical` : 'major','very bad'
   - `ok` : 'ok','clear'
   - `warning` : 'warning'

#### Property: `host`
 - `Source`: email body
 - `Default Value`: 'general issue'
 - `Extraction` : `host is (.*)`

#### Property: `region`
 - `Source`: email body
 - `Default Value`: 'us-west-1'
 - `Extraction` : `region: (.*)`

#### Property: `email_body`
 - `Source`: email body
 - `Extraction` : `([\\s\\S]*)`