# ShellHacks All-in-one super APP
Docs for API endpoints

# Get the current price of a coin
## POST https://shellcoin.appspot.com/coinprice
## Form-data: {'coin' : 'ETH'}
## Output:
```json
{
    "ETH": 2938.34875549166
}
```

# Get the current technical indicators for a coin
## POST https://shellcoin.appspot.com/technical
## Form-data: {'coin' : 'ETH'}
## Output:
```json
{
    "bearish": 3,
    "bullish": 0,
    "neutral": 1
}
```

# Gives a price prediction for **ETH** trained with GCP AutoML
## POST https://shellcoin.appspot.com/ethprediction
## Form-data: nothing
## Output:
```json
{
    "value": 2926.66
}
```


# Create a Divide And Conquer Bot works with all crypto currencies (By Nathan)
## POST https://shellcoin.appspot.com/dncbot
## Form-data Ex: {'coin' : 'ETH', 'investment':5000}
## Output:
```json
{
    "transactions": [
        {
            "buy": 2937.79,
            "coin": "ETH",
            "investment": 2500.0,
            "sell": 3803.96
        },
        {
            "buy": 2376.67,
            "coin": "ETH",
            "investment": 25.0,
            "sell": 2392.95
        },
        {
            "buy": 2392.95,
            "coin": "ETH",
            "investment": 24.75,
            "sell": 2409.22
        },
        ...
        ...
        ...
```


# Get the last 7 day prices for a coin
## POST https://shellcoin.appspot.com/oldprices
## Form-data: {'coin' : 'ETH'}
## Output:
```json
{
    "Data": {
        "Aggregated": false,
        "Data": [
            {
                "close": 3435.76,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3541.73,
                "low": 3370.5,
                "open": 3398.82,
                "time": 1631923200,
                "volumefrom": 279872.2,
                "volumeto": 968755868.2
            },
            {
                "close": 3328.85,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3456.34,
                "low": 3282.08,
                "open": 3435.76,
                "time": 1632009600,
                "volumefrom": 222702.65,
                "volumeto": 749411817.66
            },
            {
                "close": 2966.51,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3344.34,
                "low": 2926.56,
                "open": 3328.85,
                "time": 1632096000,
                "volumefrom": 925768.52,
                "volumeto": 2854105768.19
            },
            {
                "close": 2760.2,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3103.63,
                "low": 2677.64,
                "open": 2966.51,
                "time": 1632182400,
                "volumefrom": 906870.89,
                "volumeto": 2632590191.67
            },
            {
                "close": 3078.88,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3090.16,
                "low": 2738.86,
                "open": 2760.2,
                "time": 1632268800,
                "volumefrom": 525831.56,
                "volumeto": 1546061749.14
            },
            {
                "close": 3154.62,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3177.43,
                "low": 3037.12,
                "open": 3078.88,
                "time": 1632355200,
                "volumefrom": 336516.23,
                "volumeto": 1048023991.37
            },
            {
                "close": 2930.86,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 3160.27,
                "low": 2745.73,
                "open": 3154.62,
                "time": 1632441600,
                "volumefrom": 727870.33,
                "volumeto": 2116848129.48
            },
            {
                "close": 2941.08,
                "conversionSymbol": "",
                "conversionType": "direct",
                "high": 2968.99,
                "low": 2805.35,
                "open": 2930.86,
                "time": 1632528000,
                "volumefrom": 327776.53,
                "volumeto": 952405495
            }
        ],
        "TimeFrom": 1631923200,
        "TimeTo": 1632528000
    },
    "HasWarning": false,
    "Message": "",
    "RateLimit": {},
    "Response": "Success",
    "Type": 100
}
```
