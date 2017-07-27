# tap-appsflyer

This is a [Singer](https://singer.io) tap that produces JSON-formatted 
data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from AppFlyer's [Raw Data Reports V5 API](https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

### Obtaining your `app_id` and `app_token`

* `app_id` can be found on your [My Apps](https://hq1.appsflyer.com/apps/myapps).  It's displayed under the name of your application.
* `app_token` can be found on the application's [API Access](https://hq1.appsflyer.com/dashboard/apiaccess/your-app-id-here) page under "Your API Key".

---

Copyright &copy; 2017 ezCater, Inc.