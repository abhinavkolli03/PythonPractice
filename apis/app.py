from openexchange import OpenExchangeClient
import time

APP_ID = "a7134478b7a942989e5cd9ef682f8204"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)
print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")