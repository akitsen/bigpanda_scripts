## akitsen_template.json
This is an improved template based on the default.

#### Property: `status`
 - `Source`: email subject line
 - `Default Value`: warning 
 - `Status Map` : 
   - ```
       "status_map": {
                  "critical": [
                      "major",
                      "down",
                      "bad",
                      "very bad"
                  ],
                  "ok": [
                      "ok",
                      "clear"
                  ],
                  "warning": [
                      "warning",
                      "degraded"
                  ]
              }
       ```

#### Property: `host`
 - `Source`: email body
 - `Default Value`: 'general issue'
 - `Extraction` : `^.*host is ([a-zA-Z0-9\-\.\_]+).*$|^host:\s([a-zA-Z0-9\-\.\_]+)$`

#### Property: `region`
 - `Source`: email body
 - `Default Value`: 'us-west-1'
 - `Extraction` : `^[r|R]egion:\s([a-zA-Z0-9\-\.\_]+).*$`

#### Property: `email_body`
 - `Source`: email body
 - `Extraction` : `([\\s\\S]*)`