
## USAGE
```python
from ora import Ora, Spinner
from colorama import Fore

ora = Ora(spinner=Spinner.DOTS)

# start spinning
ora.spin()

# optional
# ora.color = Fore.CYAN
# ora.text = "loading"


# do stuff here

ora.stop()

```
