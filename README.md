# EduGen

> gcloud auth login

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
* Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.

> gcloud auth application-default print-access-token

ERROR: (gcloud.auth.application-default.print-access-token) Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.

> gcloud auth application-default login

Credentials saved to file: [C:\Users\Igor\AppData\Roaming\gcloud\application_default_credentials.json]


> gcloud auth application-default print-access-token

Your application is authenticating by using local Application Default Credentials. The texttospeech.googleapis.com API requires a quota project, which is not set by default. To learn how to set your quota project, see https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds .

> gcloud auth application-default set-quota-project YOUR_PROJECT

> certutil -decode SOURCE_BASE64_TEXT_FILE DESTINATION_AUDIO_FILE
