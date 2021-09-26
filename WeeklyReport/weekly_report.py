from trycourier import Courier

def send_weekly_email(user_email, user_firstname, revenue_before, revenue_after):
        client = Courier(auth_token="dk_prod_XAD3QDVD0SM6Q9NF9V0QPAAZG7NC")
        resp = client.send(
            event="TRG9F2S9Q5MQJVNVVJGQQ4DKYM5N",
            recipient="985353f4-2813-4406-a91d-a72981cee7c3",
            profile={
                    "email": user_email,
            },
            data={
                "first_name": user_firstname,
                "before_week_value": revenue_before,
                "after_week_value": revenue_after
            },
        )
        print(resp['messageId'])

if __name__ == "__main__":
        print("running hardcoded example...")
        send_weekly_email("wilk.nathan@gmail.com", "Nathan", 0, 1000)
