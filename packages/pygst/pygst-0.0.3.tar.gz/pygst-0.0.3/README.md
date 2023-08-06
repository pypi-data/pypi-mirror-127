# pygst (Python global stock time)

This lib will tell you what is current market status of your stock.

Holiday is coming soon.

## Example

```
from pygst import get_market_status, MarketStatus

status = get_market_status("AAPL")
if status == MarketStatus.PRE or status == MarketStatus.POST:
    print("Extended time")
else:
    print(f"{status.name.lower()} time")

```
