# Unique Email Counter

This web service accepts `http` requests and returns responses based on the condition outlined [here](https://fetch-hiring.s3.amazonaws.com/email.html).

## Prerequisites

- Docker

## Instructions
To run this program locally on your device, please follow these instructions:

- Run `git clone https://github.com/aa-ag/uniqueemails`.
- Run `cd uniqueemails`
- Run `docker-compose up`
- Open `http://127.0.0.1:5000/` | You should see a `status: ok`
- Enjoy! Now you can, for example, input different lists via Postman; here's the format: 

```
POST: /dedup_emails
Content-Type: "application/json"

Payload
{
    "csvEmails": "emailemail@gmail.com, email.email@gmail.com, email..email@gmail.com, emailemail+SPAMspamSPAMfetchrewards@gmail.com, email..................email+ljkasdlfknavlkn575775757@gmail.com"
}

Output
{
    "totalNumberOfUniqueEmails: 1
}
```

### Contact

For any questions, please contact [me](https://www.linkedin.com/in/aa-ag/).