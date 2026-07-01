Read the Apache access log located at:

`/app/access.log`

Generate a JSON report and save it to:

`/app/report.json`

The report must contain exactly these fields:

* `total_requests`
* `unique_ips`
* `top_path`

Success criteria:

1. Read the input log from `/app/access.log`.
2. Write the output to `/app/report.json`.
3. Set `total_requests` to the total number of log entries.
4. Set `unique_ips` to the number of distinct client IP addresses.
5. Set `top_path` to the most frequently requested URL path.
6. Produce valid JSON containing exactly the required fields.
